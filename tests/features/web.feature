@web
Feature: Wikipedia Web Browsing
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  @sachin
  Scenario Outline: Basic Wikipedia Search1
    Given the wikipedia home page is displayed
    When the user searches for "<name>"
    Then results are shown for "<name>"
    Examples:
      | name             |
      | sachin tendulkar |
      | amitabh bachchan |


  @selenium
  Scenario Outline: Basic Wikipedia Search2
    Given the wikipedia home page is displayed
    When the user searches for "<name>"
    Then results are shown for "<name>"

    Examples:
      | name                  |
      | The Lord of the Rings |
      | Zodiac                |


