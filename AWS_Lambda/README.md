# Texas Inventionworks and AWS Lambda 

AWS Lambda is basically a mini computer environment in the cloud that can execute a programming function when a defined event happens, or on a timer.

TIW uses AWS Lambda to automatically sync the trainings between Canvas, the AWS Database (AWS DynamoDB), and Fabman. Another use case is to use a Lambda to periodically poll who has activated a MAC, and see, in real time, who is checked into a machine.

In this exercise, you will go through a real, TIW use case for AWS Lambda, and learn how to deploy your Lambda.

1. Set up the AWS CLI
2. Pull the repository to your local environment
