from secrets import get_fabman_secret
from fabman import Fabman
import boto3
import matplotlib.pyplot as plt
import numpy as np

# Helper function to help us plot a distribution of numbers in a list
def plot_list(arr, x_title, y_title):
    plt.hist(arr, bins=20)
    plt.title('Distribution')
    plt.xlabel(x_title)
    plt.ylabel(y_title)
    plt.grid(True, alpha=0.3)
    plt.show()

# initilize the DynamoDB connection to AWS
ddb = boto3.resource('dynamodb')

# TODO: specify the DDB table we want to pull data from
table = ddb.Table('')

# TODO: do a table scan for all of the values in the 'score' column


# TODO: iterate through each of the items in the response, and extract the scores into a list of scores


# TODO: Plot the scores list (using the plot_list function), make sure to specify the x axis and y axis titles




