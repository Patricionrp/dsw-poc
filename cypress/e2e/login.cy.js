describe('Compra de producto', () => {

    it('Debe agregar un producto e iniciar checkout', () => {

        cy.visit('/')

        cy.fixture('usuario').then((datos) => {

            cy.login(datos.usuario, datos.password)

        })

        cy.get('#add-to-cart-sauce-labs-backpack').click()

        cy.get('.shopping_cart_link').click()

        cy.get('#checkout').click()

        cy.contains('Checkout: Your Information')

    })

})