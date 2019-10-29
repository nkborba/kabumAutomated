Feature: Cart behavior

    Scenario: Purchase 1 item
        Given the Kabum Store
        When we log in
        When we add the product "SA400S37" to the cart
        When we open the cart
        When we add CEP
        When we add select payment type as "credito"
        When we insert credit card info
        Then we finish the purchase

    Scenario: Purchase 2 items, one with 2 units
        Given the Kabum Store
        When we log in
        When we add the product "SA400S37" to the cart
        When we add another product "YD1600BBAEBOX" to the cart
        When we open the cart
        When we add an unit of the last product
        When we add CEP
        When we add select payment type as "credito"
        When we insert credit card info
        Then we finish the purchase

    Scenario: Delete an item from the cart
        Given the Kabum Store
        When we log in
        When we add the product "SA400S37" to the cart
        When we add another product "YD1600BBAEBOX" to the cart
        When we open the cart
        When we count items inside the cart
        When we delete an item
        Then there is fewer items in the cart