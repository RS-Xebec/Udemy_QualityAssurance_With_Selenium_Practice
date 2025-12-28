Feature: Verify Registration functionality

  @sanity
  Scenario: Registration with valid data
  Given  User is on Registration Page
  When   User enters username 
  And    User enters email id
  And    User enters password
  And    User click on signup button
  Then   User should be registered successfully

  @sanity @smoke
  Scenario: Registration with duplicate username data
  Given  User is on Registration Page
  When   User enters duplicate username 
  And    User enters email id
  And    User enters password
  And    User click on signup button
  Then   User should be registered successfully

  @abcd
  Scenario: Registration with valid data
  Given  User is on Registration Page
  When   User enters username 
  And    User enters email id

