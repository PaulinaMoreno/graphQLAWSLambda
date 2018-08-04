import sys
import json
import requests
from requests_aws_sign import AWSV4Sign
from boto3 import session
sys.path.append(".") 
from schema import User

user_data = []
friendShip_data = []

def setup():
    
    global user_data

    user01 = User(
        userID="1000",
        name="Roxie Joddens",
        email="rjoddens7@51.la",
        phone="+358-119-977-5220",
        friends=[],
    
    )

    user02 = User(
        userID="1001",
        name="Aundrea Izard",
        email="aizard8@biglobe.ne.jp",
        phone="+4084687956",
        friends=[],
    )

    user03 = User(
        userID="1002",
        name="Teddy Bolan",
        email="tbologan@gmail.com",
        phone="+4084689120",
        friends=[],
    )

    user04 = User(
        userID="1003",
        name="Avril Joyson",
        email="ajoysoni@tmall.com",
        phone="+4086884546",
        friends=[],
    )

    user01.friends.append(user02)
    user01.friends.append(user04)

    user02.friends.append(user04)
    user02.friends.append(user03)

    user03.friends.append(user02)
    

    user_data.append(user01)
    user_data.append(user02)
    user_data.append(user03)
    user_data.append(user04)

def set_friendship_value(u,f):
    u.friends.append(f)

def get_friendship(friends):
    for f in friends:
        print(f.userID)

def get_all_users():
    return user_data

