// Creates the outreach Google Form and a linked response sheet.
// Run once at script.google.com: paste, then Run > createStudyForm.
// The form and sheet links are printed in the execution log.

function createStudyForm() {
  var TEAM_EMAIL = 'TEAM_EMAIL_HERE';

  var form = FormApp.create('Help us build something that makes learning easier for blind and low vision students');
  form.setDescription(
    'We are four master\'s students in Applied Computing at the University of Windsor: Abhinav Pandey, Shrijana Karki, Aakriti Mainali and Khemraj Adhikari. ' +
    'We want to build something that genuinely helps blind and low vision students learn, from lecture slides and research papers to complex math, diagrams and braille devices like the Monarch. ' +
    'Before we build anything, we want to hear from you. Answer as much or as little as you like; a sentence or two is enough. If things already work well for you, please tell us that too.\n\n' +
    'Prefer to talk? We would love a 15 to 30 minute chat. Leave your contact at the end.');
  form.setCollectEmail(false);
  form.setLimitOneResponsePerUser(false);
  form.setProgressBar(true);
  form.setConfirmationMessage('Thank you. What you shared will help us build the right thing.');

  form.addMultipleChoiceItem()
    .setTitle('I am answering as')
    .setChoiceValues(['Accessibility services staff', 'Student who is blind or has low vision',
      'Student with another disability', 'Instructor', 'Other']);

  var paragraphs = [
    'What kinds of material are hardest to use? For example slides, PDFs, research papers, math, graphs, diagrams, videos or live lectures.',
    'Tell us about a recent time course material did not work. What happened?',
    'How long does it usually take to get an accessible version, and what happens while you wait?',
    'What do you or your students do today to get around these problems?',
    'Do screen readers, braille displays or devices like the Monarch have trouble with some material? Which kinds?',
    'What already works well?',
    'If we could build one thing that would help, what would you want it to do?'
  ];
  paragraphs.forEach(function (q) { form.addParagraphTextItem().setTitle(q); });

  form.addTextItem().setTitle('Would you, or students you support, be open to a short chat? How can we reach you?');

  form.addPageBreakItem().setTitle('Consent')
    .setHelpText('Taking part is voluntary. You can skip any question, and you can ask us to delete your answers at any time by emailing ' + TEAM_EMAIL + '. Your answers are used only for this University of Windsor course project.');

  form.addMultipleChoiceItem()
    .setTitle('I agree that the team may use my answers for this University of Windsor course project.')
    .setChoiceValues(['Yes', 'No'])
    .setRequired(true);

  form.addMultipleChoiceItem()
    .setTitle('May we quote your words in our report and presentation?')
    .setChoiceValues(['Yes, without my name', 'Yes, with my name or organization', 'No']);

  var sheet = SpreadsheetApp.create('Study responses, accessible learning material');
  form.setDestination(FormApp.DestinationType.SPREADSHEET, sheet.getId());

  Logger.log('Share this link: ' + form.getPublishedUrl());
  Logger.log('Edit the form: ' + form.getEditUrl());
  Logger.log('Responses sheet: ' + sheet.getUrl());
}
