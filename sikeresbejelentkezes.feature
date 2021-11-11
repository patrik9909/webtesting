Feature: showing off behave

  Scenario: sikeres bejelentkezés
     Given The Haldorado page is opened
      When the username is typed in the username input field
      And the password is typed in the password input field
      And the "Bejelentkezés" button is clicked
      Then the homepage should be displayed