describe('Compra de producto', () => {

  it('Debe agregar un producto e iniciar el checkout', () => {

    // Abrir la aplicación
    cy.visit('https://www.saucedemo.com/')

    // Login
    cy.get('#user-name').type('standard_user')
    cy.get('#password').type('secret_sauce')
    cy.get('#login-button').click()

    // Verificar que ingresó correctamente
    cy.contains('Products')

    // Agregar mochila al carrito
    cy.get('#add-to-cart-sauce-labs-backpack').click()

    // Ir al carrito
    cy.get('.shopping_cart_link').click()

    // Verificar que el producto está en el carrito
    cy.get('.inventory_item_name')
      .should('have.text', 'Sauce Labs Backpack')

    // Iniciar checkout
    cy.get('#checkout').click()

    // Verificar que estamos en la pantalla de Checkout
    cy.contains('Checkout: Your Information')

  })

})