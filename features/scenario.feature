Feature: eBay.com regression

  Scenario: Verify that item can be added to the cart
    Given Navigate to Ebay
    When Type "book" into the search field
    And Click the "Search" button
    Then Click on the first item from the results
    Then Switch to newly opened tab
    And Click on "Add to Cart"
    Then Item added to the cart
