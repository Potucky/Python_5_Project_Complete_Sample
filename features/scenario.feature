Feature: Validate header navigation buttons on eBay homepage

  As an eBay user
  I want to access key sections through the main header
  So that I can verify that navigation links work correctly

  Background:
    Given I Navigate to eBay

  @header @daily
  Scenario: Navigate to Daily Deals
    When I click on Daily Deals
    Then verify Daily Deals page loaded

  @header @brand
  Scenario: Navigate to Brand Outlet
    When I click on Brand Outlet
    Then verify Brand Outlet page loaded

  @header @gift
  Scenario: Navigate to Gift Cards
    When I click on Gift Cards
    Then verify Gift Cards page loaded

  @header @sell
  Scenario: Navigate to Sell page
    When I click on Sell
    Then verify Sell page loaded


  @header @signin
  Scenario: Navigate to Sign in / Register
    When I click on Sign in or Register
    Then verify Sign in page loaded

  @header @help
  Scenario: Navigate to Help & Contact
    When I click on Help & Contact
    Then verify Help & Contact page loaded
