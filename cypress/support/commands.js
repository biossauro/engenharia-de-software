// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })

Cypress.Commands.add("accessAnyDice", () => {
  cy.visit("https://anydice.com/");
});

Cypress.Commands.add("checkText", (key, text) => {
  cy.get(key).should("contain.text", text);
});

Cypress.Commands.add("clickAndWait", (key) => {
  cy.get(key).click();
  cy.wait(1000);
});

Cypress.Commands.add("inputDice", (input) => {
  cy.get("#codeInput").clear().type(input);
  cy.clickAndWait("#calculateButton");
});

Cypress.Commands.add("seeDocumentation", () => {
  cy.get("#documentationPage-selector").click();
});
