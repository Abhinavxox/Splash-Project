// Saves answers from study.html into a Google Sheet in your Drive.
//
// Setup, once:
// 1. script.google.com > New project. Paste this file.
// 2. Run setup() once and allow access. The sheet link appears in the execution log.
// 3. Deploy > New deployment > type Web app.
//    Execute as: Me. Who has access: Anyone. Deploy and copy the Web app URL.
// 4. Put that URL in study.html as SAVE_URL.

var COLUMNS = ['Received', 'role', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
  'meet', 'name', 'consent_use', 'consent_quote', 'consent_name'];

function setup() {
  var ss = SpreadsheetApp.create('Study responses, accessible learning material');
  ss.getSheets()[0].appendRow(COLUMNS);
  PropertiesService.getScriptProperties().setProperty('SHEET_ID', ss.getId());
  Logger.log('Responses sheet: ' + ss.getUrl());
}

function doPost(e) {
  var data = JSON.parse(e.postData.contents);
  if (data.consent_use !== 'yes') {
    return ContentService.createTextOutput('no consent');
  }
  var id = PropertiesService.getScriptProperties().getProperty('SHEET_ID');
  var sheet = SpreadsheetApp.openById(id).getSheets()[0];
  var row = COLUMNS.map(function (c) { return c === 'Received' ? new Date() : (data[c] || ''); });
  sheet.appendRow(row);
  return ContentService.createTextOutput('saved');
}
