@EndToEndRegression
Feature: Customer search and purchase item from the application
		 In this feature a customer will come to my application, login, search, do payment and logout
	
    Background:	Given User Open Browser, enter URL and navigate to Login page #This is used when different scenarios have same number of steps.
		 
		
	@Smoke   #@defines tags so that we can execute only those tag scenarios. Basically we can control execution
	Scenario: New User(Unregistered User) comes to application, Search, Register and Purchase.
	    When  User enter data in search field
		And   User Click on Search button
		And   User Click on Add to Cart for first Search Result
		And   User click on my Cart button
		Then  User should get added item in Cart
		And   User should get price in front of the item name
	
	@Sanity @Regression
	Scenario: Registered user, Search Item and Purchase           #""  We can define data while writing scenario step, this is called step argument.This data will be used as input when we are writing actual automation steps by programming
		When  User enter "Mobile Phone" in search field           
		And   User Click on Search button
		And   User Click on Add to Cart for first Search Result
		And   User click on my Cart button
		Then  User should get added item in Cart
		And   User should get price in front of the item name
		
	
	@Performance
	Scenario: Registered User, Search , Add to Cart, Change Address and Payment
		When  User enter "Smart Tv" in search field
		And   User Click on Search button
		And   User Click on Add to Cart for first Search Result
		And   User click on my Cart button
		Then  User should get added item in Cart
		And   User should get price in front of the item name
		
		
	Scenario Outline: Verify login and logout functionality with multiple user data
	   When User enters username <"Username">
	   And  User enters password <"Password">
	   And  User clicks on signin button
	   Then User should be logged In
	   When User clicks on Signout link
	   Then user should be logged Out
	Examples: 
		|Username|Password|
		| User1  |Pass1   |
		| User2  |Pass2   |
		| User3  |Pass3   |
		|User4   |Pass4   |
	
	
	
	Scenario: Test email functionality of application
	   When User enters username "Hello"
	   And  User enters password "abcd"
	   And  User clicks on signin button         #""" is used for entering text body link in email
	   And  User clicks on compose button
	   And  User enter body text
	        """
			This is line 1
			This is line 2
			
			Regards Testing Student
			"""