Feature: Transfer
Scenario: User is able to send express transfer to account
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "4" amount
And I send "express" transfer to "89092909246" with "1" amount
Then Transfer is accepted
And Account with pesel "89092909246" has "balance" equal to "2"
Scenario: User is able to get incoming transfer to account
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "1" amount
Then Transfer is accepted
And Account with pesel "89092909246" has "balance" equal to "1"
Scenario: User is able to send outgoing transfer to account
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "3" amount
And I send "outgoing" transfer to "89092909246" with "1" amount
Then Transfer is accepted
And Account with pesel "89092909246" has "balance" equal to "2"
Scenario: Transfer to invalid account
Given Account registry is empty
When I send "incoming" transfer to "89092909246" with "3" amount
Then Transfer is rejected
Scenario: Transfer with invalid type
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "invalid_type" transfer to "89092909246" with "3" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "0"
Scenario: Express transfer with insufficient balance
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "express" transfer to "89092909246" with "1" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "0"
Scenario: Outgoing transfer with insufficient balance
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "outgoing" transfer to "89092909246" with "1" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "0"
Scenario: Express transfer with negative amount
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "4" amount
And I send "express" transfer to "89092909246" with "-1" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "4"
Scenario: Incoming transfer with negative amount
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "-1" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "0"
Scenario: Outgoing transfer with negative amount
Given Account registry is empty
When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
And I send "incoming" transfer to "89092909246" with "3" amount
And I send "outgoing" transfer to "89092909246" with "-1" amount
Then Transfer is rejected
And Account with pesel "89092909246" has "balance" equal to "3"
