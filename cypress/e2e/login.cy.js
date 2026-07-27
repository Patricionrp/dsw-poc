describe('Compra de producto', () => {

  it('Debe agregar un producto e iniciar el checkout', () => {

    cy.visit('https://www.saucedemo.com/')

    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()

    
    cy.contains('Products')

    
    cy.get('#add-to-cart-sauce-labs-backpack').click()

    cy.get('.shopping_cart_link').click()

    cy.get('.inventory_item_name')
      .should('have.text', 'Sauce Labs Backpack')

    cy.get('#checkout').click()

    cy.contains('Checkout: Your Information')

  })

})