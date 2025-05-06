const XLSX = require("xlsx");

const file1 = XLSX.readFile("file1.xlsx"); // replace with your excel file containing all users
const file2 = XLSX.readFile("file2.xlsx"); // replace with your excel file containing active users

const sheet1 = file1.Sheets[file1.SheetNames[0]];
const sheet2 = file2.Sheets[file2.SheetNames[0]];

const data1 = XLSX.utils.sheet_to_json(sheet1, { defval: null });
const data2 = XLSX.utils.sheet_to_json(sheet2, { defval: null });

const keyColumn = "login";

// Convert Sheet2 to a Set for quick lookups
const sheet2Logins = new Set(data2.map(row => row[keyColumn]));

// Filter out rows that exist in Sheet1 but not in Sheet2
const missingRows = data1.filter(row => !sheet2Logins.has(row[keyColumn]));

// Prepare output with the same headers as Sheet1
if (missingRows.length > 0) {
  const headers = Object.keys(data1[0]);

  // Convert NULL values back to original format (keeping FALSE and empty cells separate)
  const results = [
    headers,
    ...missingRows.map(row =>
      headers.map(header =>
        row[header] === null ? "" : row[header]
      )
    )
  ];

  // Create a new workbook and sheet for the missing rows
  const newWorkbook = XLSX.utils.book_new();
  const newWorksheet = XLSX.utils.aoa_to_sheet(results);

  // Append the sheet to the workbook
  XLSX.utils.book_append_sheet(newWorkbook, newWorksheet, "inactive-users");

  // Write the output to a new Excel file
  XLSX.writeFile(newWorkbook, "inactive-users.xlsx");

  console.log("Comparison complete! See 'inactive-users.xlsx' for results.");
} else {
  console.log("No missing rows found.");
}
