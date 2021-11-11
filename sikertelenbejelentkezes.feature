Feature: showing off behave

  Scenario: sikertelen bejelentkezés
     Given The Haldorado homepage is opened
      When the username is typed in the username field
      And the password is typed in the password field
      And the "Bejelentkezés" button is  clicked
      Then the error message should be displayed