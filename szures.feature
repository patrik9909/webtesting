Feature: showing off behave

  Scenario: szures
     Given The haldorado page  is  opened
      When the "termékek" is opened
      And the "gyártóra szűrés" button is clicked
      And the "haldorádó" manufacturer is choosen
      Then the results  should be displayed