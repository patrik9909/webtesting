Feature: showing off behave

  Scenario: Ar szerint növekvobe rendez
     Given The  haldorado page is opened
      When the "top termékek" is clicked
      And the "ár szerint növekvő" is choosen
      Then the "Ár szerint növekvő" should be displayed