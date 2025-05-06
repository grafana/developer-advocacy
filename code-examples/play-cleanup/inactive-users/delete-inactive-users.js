const xlsx = require('xlsx');
const axios = require('axios');

require('dotenv').config();

async function deleteUsersFromSheet() {
  const workbook = xlsx.readFile("inactive-users.xlsx");
  const sheet = workbook.Sheets[workbook.SheetNames[0]];
  const data = xlsx.utils.sheet_to_json(sheet);

  const keyColumn = "userId";

  if (data.length === 0) {
    console.log('No data found.');
    return;
  }

  if (!data[0].hasOwnProperty(keyColumn)) {
    console.log(`Column ${keyColumn} not found`);
    return;
  }

  const baseUrl = "https://play.grafana.org/api/org/users/";
  const token = process.env.TOKEN;

  for (const row of data) {
    const userId = row.userId;
    if (userId) {
      const url = `${baseUrl}${encodeURIComponent(userId)}`;
      console.log(url);

      try {
        const response = await axios.delete(baseUrl, {
          headers: {
            'Authorization': `Bearer ${token}`,
          }
        });
        console.log(`Deleted user ${userId}: ${response.status}`);
      } catch (error) {
        console.error(`Error deleting user ${userId}: ${error.message}`);
      }
    }
  }
}

deleteUsersFromSheet();
