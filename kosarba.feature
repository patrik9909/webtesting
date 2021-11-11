Feature: showing off behave

  Scenario: kosarba helyezes
     Given The Haldorado  homepage is opened
      When the username  is typed in the username field
      And the password  is typed in the password field
      And the "Bejelentkezés"  button is  clicked
      And the „okuma” is typed in the search input field
      And the first result is clicked
      And the "kosárba" button is clicked
      Then the item should be displayed in the basket