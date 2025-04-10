from secrets import get_fabman_secret
from fabman import Fabman
import requests

def handler(event, __):
    """
    This is the Lambda handler -- this is the entry point where AWS Lambda looks for to run your code
    """

    fabman = Fabman(get_fabman_secret())
    members = fabman.get_members(q='steve')
    
    steves = []

    for member in members:
        steve = {
            'name': member.__getattribute__("firstName") + " " + member.__getattribute__("lastName"),
            'email': member.__getattribute__("emailAddress")
        }
        steves.append(steve)
    
    for i in range(len(steves)):
        print(steves[i]['name'] + " : " + steves[i]['email'])
    


if __name__ == "__main__":
    handler(None, None)