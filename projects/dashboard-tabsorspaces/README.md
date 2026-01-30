# Dashboard Tabs or Spaces

A tool to analyze indentation preferences (tabs vs spaces) across GitHub repositories.

## Setup

### 1. Database Configuration

Create a `.env` file in the project root with your database credentials:

```bash
cp .env.example .env
# Edit .env with your actual database credentials
```

The `.env` file should contain:
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=tabs-or-spaces
```

### 2. Python Dependencies

Install required Python packages using pip:

```bash
pip install -r requirements.txt
```

Alternatively, you can install packages individually:

```bash
pip install mysql-connector-python python-dotenv
```

### 3. Database Schema

Create the database schema:

```bash
mysql -u username -h host -p < create_schema.sql
```

## Usage

### Quick Start - Run Complete Analysis

The easiest way to run the complete analysis workflow:

```bash
./run_analysis.sh
```

This script will:
1. Clone or pull the `EvanLi/Github-Ranking` repository
2. Create the `evaluated_projects` directory if needed
3. Run `fetch_repos.sh` to fetch the top 100 repositories
4. Analyze each repository using `tabsorspaces.py`

### Manual Usage

#### Analyze a single repository

```bash
./is_code.sh <target_code_directory> | python3 ./tabsorspaces.py --repo-owner <owner> --repo-name <repo>
```

#### Output CSV instead of database

```bash
./is_code.sh <target_code_directory> | python3 ./tabsorspaces.py --repo-owner <owner> --repo-name <repo> --csv --no-db
```

#### Fetch repositories manually

```bash
./fetch_repos.sh
```

## Scripts

- `run_analysis.sh` - Main wrapper script that runs the complete workflow
- `fetch_repos.sh` - Fetches the top 100 repositories from Github-Ranking
- `tabsorspaces.py` - Analyzes indentation in source files
- `is_code.sh` - Filters files to identify code files by MIME type
