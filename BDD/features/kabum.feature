Feature: Cart behavior

    Scenario: Purchase 1 item
        Given the Kabum Store
        When I log in
        And I add the product to the cart
            |product        |
            |SA400S37       |
        And I open the cart
        And I add CEP
        And I add select payment type as "credito"
        And I insert credit card info
        Then I should finish the purchase sucessfully

    Scenario: Purchase 2 items, one with 2 units
        Given the Kabum Store
        And I log in
        And I add the product to the cart
            |product        |
            |SA400S37       |
            |YD1600BBAEBOX  |
        And I open the cart
        And I add an unit of the last product
        And I add CEP
        And I add select payment type as "credito"
        And I insert credit card info
        Then I should finish the purchase sucessfully

    Scenario: Delete an item from the cart
        Given the Kabum Store
        When I log in
        And I add the product to the cart
            |product        |
            |SA400S37       |
            |YD1600BBAEBOX  |
        And I open the cart
        And I count items inside the cart
        And I delete an item
        Then there is fewer items in the cart
