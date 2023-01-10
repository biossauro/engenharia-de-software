/// <reference types="cypress" />
// npm rum cypress

describe("SUIT de Teste: testando as funcionalidades do site anydice.com", () => {
  // 1
  it("Cenário de Teste: Rolando 1d20 e Somando 5", () => {
    cy.accessAnyDice();
    cy.inputDice("output 1d20 + 5");
    cy.checkText(":nth-child(20) > :nth-child(1)", "25");
  });

  // 2
  it("Cenário de Teste: Acessando a Documentação", () => {
    cy.accessAnyDice();
    cy.seeDocumentation();
    cy.clickAndWait("#documentationPage > :nth-child(2)");
    cy.scrollTo("bottom");
    cy.checkText("#documentationPage > :nth-child(20)", "Functions");
  });

  // 3
  it("Cenário de Teste: Gerando Erro de Sintaxe", () => {
    cy.accessAnyDice();
    cy.inputDice("#codeInput", `output 1d20 as "ataque de espada longa"`);
    cy.checkText("#errorDisplay > h3", "syntax error");
  });

  // 4
  it("Cenário de Teste: Usando Funções", () => {
    cy.accessAnyDice();
    cy.inputDice(testFunction);
    cy.scrollTo("bottom");
    cy.checkText(":nth-child(10) > caption", "10d");
  });

  // 5
  it("Cenário de Teste: Rolando Dados Arbitrários", () => {
    cy.accessAnyDice();
    cy.inputDice(`output d{{}-1..1} named "Fudge die"`);
    cy.checkText("caption", "Fudge die");
  });

  // 6
  it("Cenário de Teste: Checando Resultados", () => {
    cy.accessAnyDice();
    cy.inputDice(`output 2d6 + 3 named "espadas curtas"`);
    cy.clickAndWait("#exportDisplay-selector");
    cy.checkText("#exportDisplay > textarea", "espadas curtas");
  });

  // 7
  it("Cenário de Teste: Rolando Dados", () => {
    cy.accessAnyDice();
    cy.inputDice(`output 1d8 + 13 named "arco longo"`);
    cy.clickAndWait("#rollerDisplay-selector");
    cy.clickAndWait("#rollerButton");
    cy.checkText("#rollerOutput", "arco longo");
  });
});

const testFunction = `function: pokerole N dice {
  SUCCESSES: [count {{}4, 5, 6} in Nd6]
  result: SUCCESSES
 }
 
 loop N over {{}1..10} {
  output [pokerole N dice] named "[N]d"
 }`;
