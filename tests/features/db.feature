@db
Feature: Database comparison
  We would need to compare 2 database systems,
  1 source and 1 target,
  and try too validate and report any mismatches found.

  @smoke
  Scenario Outline: Database validation_new
    Given connection is established between source and target databases
    When user executes "<query1>" on source and "<query2>" on target databases
    And results from both database resultsets are compared
    Then user reports any mismatches
    Examples:
      | query1                        | query2                        |
      | SELECT * from db1.dbo.student | SELECT * from db2.dbo.student |
      | SELECT * from db1.dbo.student | SELECT * from db2.dbo.student |