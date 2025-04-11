<h1 align="center">Texas Inventionworks and AWS Lambda</h1>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf3c49f-d705-495c-81aa-7a67a30cf121" />
  <img src="https://github.com/user-attachments/assets/082ff99f-0ba5-4b3f-9448-bf375477f505" />
</p>


## Intro to Lambda
AWS Lambda is basically an always-on mini computer that can execute a programming function anytime you want! You can run it when a defined event happens, or even on a timer.

TIW uses **AWS Lambda** to automatically sync the trainings between **Canvas**, the AWS Database (**AWS DynamoDB**), and **Fabman**. Another use case for an **AWS Lambda** to periodically poll who has activated a Fabman MAC, and see, in real time, who is checked into a machine.


# The Exercise
In this exercise, you will face a very realistic scenario that will help you...

1. Setup developing with AWS tools locally
2. Learn how to get data from Fabman
3. Learn how to deploy your source code to a new Lambda
4. Learn how to run and see the results of your Lambda

Before moving on to **The Scenario**, take some time to look through the code in this folder and try to understand what is going on.

# The Scenario
Steve and Steven want to find all of the people named "Steve" and "Steven" to email every "Steve" and "Steven" an invitation for a "Steve'n Steve" party. They don't really know how to go about this, so they come to you for help. 

You know about this very handy Fabman API call that can get all of the information about every student in Fabman, and you can use this to find all of the people named "Steve" and "Steven". You plan to write and deploy a Lambda for them so that they can run it when they want to without bothering you anymore.




