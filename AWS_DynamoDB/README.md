<h1 align="center">Texas Inventionworks and DynamoDB</h1>
<p align="center">
  <img src="https://github.com/user-attachments/assets/7bf3c49f-d705-495c-81aa-7a67a30cf121" />
  <img src="https://github.com/user-attachments/assets/729391e0-509d-47b7-95d2-38799b397d65" />
</p>

## Intro to DynamoDB

DynamoDB is an AWS-hosted and managed database service that integrates very nicely with all of the other AWS Services. We can store large amounts of data here to pull, run statistics, and trigger Lambdas on.

# The Exercise

In this exercise, you will face a very realistic scenario that will help you...

1. Learn how to query data from a Dynamo table
2. Practice getting and processing information from tables in Python
3. Learn how to make your own Dynamo Table and write to it

Before moving on to **The Scenario**, take some time to look through the code in this folder and try to understand what is going on.

# The Scenario

Scott wants to find the distribution of scores across all attempts made for the Bambu P1P Online Training Quiz.

You tell him that you can get all the data stored in a DynamoDB table and give him a cool graphic that will show him the distribution.

He also gives you a few short bonus tasks that would make him very happy.

1. How many people missed question 2 on the Bambu Online Training Quiz? (Hint: use the code expression below to get all of the data for that question)

```code
response = table.scan(
    ProjectionExpression='#col1',
    ExpressionAttributeNames={
        '#col1': '29884637: What storage device do we use to store our G-code files for the Bambu Lab P1P printers?'
    }
)

```

2. What percentage of students missed that question?

# Your Task

Write code under the _TODO_ sections of the **dynamoDB.py** code to populate a DynamoDB table with the names, attempts, and scores of the students who HAVE completed the Bambu Online Quiz but HAVE NOT completed the Bambu In-Person quiz.

Also complete the two bonus tasks (They are pretty short)

# Setup Steps
