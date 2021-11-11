Feature: showing off behave

  Scenario: kereses
     Given The haldorado page is  opened
      When the „okuma”  is typed in the search input field
      And the search button is clicked
      Then the results should be displayed
      And the results should contain the „okuma” word