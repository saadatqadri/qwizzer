Feature: Add Multiple Choice Question
As a professor
Given I want to test the students knowledge on a particular issue
I want to to add a multiple choice question

Scenario: Specify Title
	Given I see a display asking me to add a new question
	And a text box titled Title
	I can write in the title for my question

Scenario: Specify Question Text
	Given I see a display asking me to add a new question
	And a text box titled Question
	I can write in the text of my question

