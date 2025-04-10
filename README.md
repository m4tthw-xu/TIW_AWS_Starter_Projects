# Core AWS Services:

1. **AWS Lambda**
2. **AWS Dynamo**
3. **AWS Hosting and Deployment** (EC2, ElasticBeanstalk)
4. **Others**

To work on these projects, you will need to set up the AWS CLI and sign into AWS with your IDE of choice. Since you are developing locally (on your own computer) you will need to use the AWS CLI to get our TIW secret API keys from AWS Secrets Manager.

## Setting up the AWS CLI

1. Visit https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
Download and install the MacOS or the Windows installer.

In your IDE, execute

```code
aws --version
```

to see your AWS CLI version and see that is correctly installed.

2. Execute
```code
aws configure
```
and copy-paste your AWS Access Key and AWS Secret Access Key to 'sign in' to AWS.

3. Set your Default region name to 
```code
us-east-1
```
and then keep pressing "Enter" until the prompts stop.

**You now have the AWS CLI set up with your TIW AWS Account!**

