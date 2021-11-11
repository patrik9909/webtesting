Feature: showing off behave

  Scenario: sikertelen bejelentkezés
     Given the Haldorádó page is opened
      When the username is typed in the username input  field
      And the password is typed in the password input  field
      And the "Bejelentkezés"  button is clicked
      And the „ Szia,(felhasználónév) ” button is clicked
      And And the „Kijelentkezés” button is clicked
      Then the „Bejelentkezés” button should be displayed