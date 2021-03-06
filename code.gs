function sortData() {
  const app = SpreadsheetApp;
  const ss = app.getActiveSpreadsheet();
  const sheet = ss.getActiveSheet();

  const lastRow = sheet.getLastRow();
  const lastCol = sheet.getLastColumn();

  let range = sheet.getRange(2, 1, lastRow -1, lastCol);

  range.sort({column:6, ascending: false});
}

function sendMail() {

  const app = SpreadsheetApp;
  const ss = app.getActiveSpreadsheet();

  const mail = "...";
  const name = "..."
  const body = "...;
  file = DriveApp.getFileById(ss.getId());

  MailApp.sendEmail({
    to: mail,
    subject: name,
    htmlBody: body,
    attachments: file
  });
}
