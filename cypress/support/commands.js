Cypress.Commands.add('login', (usuario, password) => {

    cy.get('#user-name').type(usuario)
    cy.get('#password').type(password)
    cy.get('#login-button').click()

})