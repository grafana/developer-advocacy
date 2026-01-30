import sys
import re
import os
import csv
import argparse
from datetime import date
from collections import Counter
from math import gcd
from functools import reduce

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is optional

try:
    import pymysql
    from pymysql import Error
except ImportError:
    pymysql = None
    Error = None

def count_leading_whitespace(line):
    """Return the number of leading spaces and tabs in a line."""
    match = re.match(r'^( +|\t+)+', line)
    if not match:
        return 0, 0
    whitespace = match.group(0)
    spaces = whitespace.count(' ')
    tabs = whitespace.count('\t')
    return spaces, tabs


def read_file_lines(file_path):
    """
    Read file lines, trying UTF-8 first, then falling back to latin-1.
    Returns (lines, encoding_used) or raises an exception if unreadable.
    """
    # Try UTF-8 first (most common for source code)
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.readlines(), 'utf-8'
    except UnicodeDecodeError:
        pass

    # Fall back to latin-1 (can decode any byte sequence)
    try:
        with open(file_path, 'r', encoding='latin-1') as f:
            return f.readlines(), 'latin-1'
    except Exception:
        raise

def detect_space_per_indent(file_path, lines):
    """Detect space-per-indent for a file using only spaces.
    
    Takes pre-read lines to avoid re-reading the file.
    """
    non_empty_lines = [line for line in lines if line.strip()]

    space_indents = []

    in_multiline_comment = False

    for line in non_empty_lines:
        stripped = line.strip()

        # Handle start/end of multiline comments
        if in_multiline_comment:
            if "*/" in stripped:
                in_multiline_comment = False
            continue
        if stripped.startswith("/*"):
            if "*/" not in stripped:
                in_multiline_comment = True
            continue

        # Skip single-line comments
        if stripped.startswith("//") or stripped.startswith("#"):
            continue

        spaces, tabs = count_leading_whitespace(line)
        if spaces > 0 and tabs == 0:
            space_indents.append(spaces)

    if not space_indents:
        return None

    indent_size = reduce(gcd, space_indents)
    if indent_size == 1:
        indent_size = 2  # Treat single-space indentation as 2 spaces
    return indent_size if indent_size > 0 else None

def is_comment_line(line, in_multiline_comment):
    """Determine if a line is a comment, handling C-style multiline comments."""
    stripped = line.strip()

    # Handle ongoing multiline comment
    if in_multiline_comment:
        if "*/" in stripped:
            return True, False  # comment line, multiline comment ends
        return True, True      # still inside comment

    # Check for comment starts
    if stripped.startswith("/*"):
        return True, "*/" not in stripped  # starts comment, may or may not close
    if stripped.startswith("//") or stripped.startswith("#"):
        return True, False

    return False, in_multiline_comment

def get_db_connection(host=None, port=None, user=None, password=None, database=None):
    """Create and return a database connection."""
    if pymysql is None:
        raise ImportError("pymysql is not installed. Install it with: pip install pymysql")
    
    # Get connection parameters from arguments or environment variables
    host = host or os.getenv('DB_HOST', 'localhost')
    port = port or int(os.getenv('DB_PORT', '3306'))
    user = user or os.getenv('DB_USER', 'root')
    password = password or os.getenv('DB_PASSWORD', '')
    database = database or os.getenv('DB_NAME', 'tabs-or-spaces')
    
    try:
        connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as e:
        print(f"Error connecting to database: {e}", file=sys.stderr)
        raise

def insert_analysis_result(connection, test_date, repo_owner, repo_name, results):
    """Insert analysis results into the database."""
    cursor = connection.cursor()
    
    # Map indentation_type to match ENUM values
    indentation_type = results['indentation_type']
    
    insert_query = """
        INSERT INTO analysis_results (
            test_date, repo_owner, repo_name, indentation_type,
            files_processed, lines_processed, deepest_indentation_level,
            average_indentation_level, files_tabs_only, files_spaces_only,
            files_mixed, avg_spaces_per_indent
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        ON DUPLICATE KEY UPDATE
            indentation_type = VALUES(indentation_type),
            files_processed = VALUES(files_processed),
            lines_processed = VALUES(lines_processed),
            deepest_indentation_level = VALUES(deepest_indentation_level),
            average_indentation_level = VALUES(average_indentation_level),
            files_tabs_only = VALUES(files_tabs_only),
            files_spaces_only = VALUES(files_spaces_only),
            files_mixed = VALUES(files_mixed),
            avg_spaces_per_indent = VALUES(avg_spaces_per_indent),
            updated_at = CURRENT_TIMESTAMP
    """
    
    values = (
        test_date,
        repo_owner,
        repo_name,
        indentation_type,
        results['files_processed'],
        results['lines_processed'],
        results['deepest_indentation_level'],
        results['average_indentation_level'],
        results['files_tabs_only'],
        results['files_spaces_only'],
        results['files_mixed'],
        results['avg_spaces_per_indent']
    )
    
    try:
        cursor.execute(insert_query, values)
        connection.commit()
        return cursor.rowcount
    except Error as e:
        print(f"Error inserting into database: {e}", file=sys.stderr)
        connection.rollback()
        raise
    finally:
        cursor.close()

def output_csv(results, repo_owner=None, repo_name=None, test_date=None):
    """Output results as CSV to stdout."""
    writer = csv.writer(sys.stdout)
    
    # Write header
    writer.writerow([
        'test_date', 'repo_owner', 'repo_name', 'files_processed', 'files_skipped',
        'lines_processed', 'indentation_type', 'avg_spaces_per_indent',
        'deepest_indentation_level', 'average_indentation_level',
        'files_tabs_only', 'files_spaces_only', 'files_mixed'
    ])
    
    # Write data row
    writer.writerow([
        test_date or '',
        repo_owner or '',
        repo_name or '',
        results['files_processed'],
        results.get('files_skipped', 0),
        results['lines_processed'],
        results['indentation_type'],
        results['avg_spaces_per_indent'] if results['avg_spaces_per_indent'] is not None else '',
        results['deepest_indentation_level'],
        results['average_indentation_level'],
        results['files_tabs_only'],
        results['files_spaces_only'],
        results['files_mixed']
    ])

def analyze_files(file_paths):
    total_indent_levels = []
    total_lines = 0

    files_tabs = 0
    files_spaces = 0
    files_mixed = 0
    files_skipped = 0

    space_per_indent_counter = Counter()
    space_per_indent_sum = 0
    space_per_indent_count = 0

    file_indent_sizes = {}

    for file_path in file_paths:
        try:
            lines, _ = read_file_lines(file_path)
        except Exception as e:
            print(f"Warning: Skipping {file_path}: {e}", file=sys.stderr)
            files_skipped += 1
            continue

        file_has_tabs = False
        file_has_spaces = False
        file_has_mixed = False
        file_space_per_indent = None
        in_multiline_comment = False

        # Detect space-per-indent if file uses only spaces
        if any(line.startswith(' ') for line in lines) and not any('\t' in line for line in lines):
            file_space_per_indent = detect_space_per_indent(file_path, lines)
            if file_space_per_indent:
                space_per_indent_counter[file_space_per_indent] += 1
                space_per_indent_sum += file_space_per_indent
                space_per_indent_count += 1
                file_indent_sizes[file_path] = file_space_per_indent

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:
                continue  # skip empty lines

            # Skip comment lines
            is_comment, in_multiline_comment = is_comment_line(line, in_multiline_comment)
            if is_comment:
                continue

            spaces, tabs = count_leading_whitespace(line)
            total_lines += 1

            if spaces > 0 and tabs > 0:
                file_has_mixed = True
            elif tabs > 0:
                file_has_tabs = True
            elif spaces > 0:
                file_has_spaces = True

            # Calculate indentation level using detected space-per-indent if available
            if file_space_per_indent and spaces > 0:
                level = tabs + (spaces // file_space_per_indent)
            else:
                level = tabs + (spaces // 4)  # fallback
            total_indent_levels.append(level)

        # File-level counters
        if file_has_mixed:
            files_mixed += 1
        elif file_has_tabs and file_has_spaces:
            files_mixed += 1
        elif file_has_tabs:
            files_tabs += 1
        elif file_has_spaces:
            files_spaces += 1

    # Overall indentation type
    overall_type = "Mixed (tabs and spaces)" if files_mixed > 0 else (
        "Tabs" if files_tabs > 0 else "Spaces" if files_spaces > 0 else "None detected"
    )

    max_indent = max(total_indent_levels) if total_indent_levels else 0
    avg_indent = sum(total_indent_levels) / len(total_indent_levels) if total_indent_levels else 0
    avg_space_per_indent = space_per_indent_sum / space_per_indent_count if space_per_indent_count > 0 else None

    # Return results as a dictionary
    files_processed = len(file_paths) - files_skipped
    return {
        'files_processed': files_processed,
        'files_skipped': files_skipped,
        'lines_processed': total_lines,
        'indentation_type': overall_type,
        'deepest_indentation_level': max_indent,
        'average_indentation_level': round(avg_indent, 2),
        'files_tabs_only': files_tabs,
        'files_spaces_only': files_spaces,
        'files_mixed': files_mixed,
        'avg_spaces_per_indent': round(avg_space_per_indent, 2) if avg_space_per_indent is not None else None,
        'space_per_indent_counter': space_per_indent_counter
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Analyze indentation (tabs vs spaces) in source files and store results in database.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze files and store in database
  python tabsorspaces.py --repo-owner owner --repo-name repo file1.py file2.py

  # Analyze files from stdin and output CSV
  find . -name "*.py" | python tabsorspaces.py --repo-owner owner --repo-name repo --csv

  # Use environment variables for database connection
  DB_HOST=localhost DB_USER=user DB_PASSWORD=pass python tabsorspaces.py --repo-owner owner --repo-name repo file1.py

Environment variables for database connection:
  DB_HOST      Database host (default: localhost)
  DB_PORT      Database port (default: 3306)
  DB_USER      Database user (default: root)
  DB_PASSWORD  Database password (default: empty)
  DB_NAME      Database name (default: tabs-or-spaces)
        """
    )
    
    parser.add_argument('files', nargs='*', help='Source files to analyze (or read from stdin if not provided)')
    parser.add_argument('--repo-owner', required=True, help='Repository owner (e.g., "facebook")')
    parser.add_argument('--repo-name', required=True, help='Repository name (e.g., "react")')
    parser.add_argument('--test-date', type=str, help='Test date in YYYY-MM-DD format (default: today)')
    parser.add_argument('--csv', action='store_true', help='Output results as CSV to stdout')
    parser.add_argument('--db-host', help='Database host (overrides DB_HOST env var)')
    parser.add_argument('--db-port', type=int, help='Database port (overrides DB_PORT env var)')
    parser.add_argument('--db-user', help='Database user (overrides DB_USER env var)')
    parser.add_argument('--db-password', help='Database password (overrides DB_PASSWORD env var)')
    parser.add_argument('--db-name', help='Database name (overrides DB_NAME env var)')
    parser.add_argument('--no-db', action='store_true', help='Skip database insertion (useful with --csv)')
    
    args = parser.parse_args()
    
    # Collect file paths
    file_paths = []
    if args.files:
        file_paths = args.files
    else:
        # Read filenames from stdin (one per line)
        try:
            for line in sys.stdin:
                file_path = line.rstrip('\n\r')
                if file_path:  # Skip empty lines
                    file_paths.append(file_path)
        except KeyboardInterrupt:
            sys.exit(1)
    
    if not file_paths:
        parser.error("No files provided. Specify files as arguments or pipe them via stdin.")
    
    # Parse test date
    if args.test_date:
        try:
            test_date = date.fromisoformat(args.test_date)
        except ValueError:
            parser.error(f"Invalid date format: {args.test_date}. Use YYYY-MM-DD format.")
    else:
        test_date = date.today()
    
    # Analyze files
    try:
        results = analyze_files(file_paths)
    except Exception as e:
        print(f"Error analyzing files: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Insert into database unless --no-db is specified
    if not args.no_db:
        try:
            connection = get_db_connection(
                host=args.db_host,
                port=args.db_port,
                user=args.db_user,
                password=args.db_password,
                database=args.db_name
            )
            insert_analysis_result(connection, test_date, args.repo_owner, args.repo_name, results)
            connection.close()
        except ImportError as e:
            print(f"Warning: {e}", file=sys.stderr)
            print("Skipping database insertion. Install pymysql to enable database support.", file=sys.stderr)
        except Exception as e:
            print(f"Error inserting into database: {e}", file=sys.stderr)
            if not args.csv:
                sys.exit(1)
    
    # Output CSV if requested
    if args.csv:
        output_csv(results, args.repo_owner, args.repo_name, test_date.isoformat())
