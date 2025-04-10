# Texas Inventionworks and AWS Lambda 

## Intro to Lambda
AWS Lambda is basically an always on mini computer that can execute a programming function anytime you want! You can run it when a defined event happens, or even on a timer.

TIW uses AWS Lambda to automatically sync the trainings between Canvas, the AWS Database (AWS DynamoDB), and Fabman. Another use case is to use a Lambda to periodically poll who has activated a MAC, and see, in real time, who is checked into a machine.

## The Exercise
In this exercise, you will face a very realistic scenario that will help you...

1. Setup developing with AWS tools locally
2. Learn how to get data from Fabman
3. Learn how to deploy your source code to a new Lambda
4. Learn how to run and see the results of your Lambda

Before moving on to **The Scenario**, take some time to look through the code in this folder and try to understand what is going on.

## The Scenario
Steve and Steven want to find all of the people named "Steve" and "Steven" to email every "Steve" and "Steven" an invitation for a "Steve'n Steve" party. They don't really know how to go about this, so they come to you for help. 

You know about this very handy Fabman API call that can get all of the information about every student in Fabman, and you can use this to find all of the people named "Steve" and "Steven". You plan to write and deploy a Lambda for them so that they can run it when they want to without bothering you anymore.




