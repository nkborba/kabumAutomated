Feature: Cart behavior

    Scenario: Purchase 1 item
        Given the Kabum Store
        When I log in
        And I add the product "SA400S37" to the cart
        And I open the cart
        And I add CEP
        And I add select payment type as "credito"
        And I insert credit card info
        Then I should finish the purchase sucessfully

    Scenario: Purchase 2 items, one with 2 units
        Given the Kabum Store
        When I log in
        When I add the product to the cart
            |product        |
            |SA400S37       |
            |YD1600BBAEBOX  |
        When I open the cart
        When I add an unit of the last product
        When I add CEP
        When I add select payment type as "credito"
        When I insert credit card info
        Then I should finish the purchase sucessfully

    Scenario: Delete an item from the cart
        Given the Kabum Store
        When I log in
        When I add the product to the cart
            |product        |
            |SA400S37       |
            |YD1600BBAEBOX  |
        When I open the cart
        When I count items inside the cart
        When I delete an item
        Then there is fewer items in the cart
