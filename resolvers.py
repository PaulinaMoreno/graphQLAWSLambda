
import sys
import json
import requests
from requests_aws_sign import AWSV4Sign
from collections import namedtuple
from boto3 import session
sys.path.append(".") 
user_data = []
friendShip_data = []
BASE_API_ENDPOINT_USERS = 'https://7fjk47abx5.execute-api.us-west-2.amazonaws.com/dev'
region = 'us-west-2'
service = 'execute-api'
        
sess = session.Session()
credentials = sess.get_credentials()
auth=AWSV4Sign(credentials, region, service)
class Resolver():
    def __init__(self):
        pass

    def get_user_by_id(self, userID):
        GET_USER_URL = BASE_API_ENDPOINT_USERS+'/users/'+userID
        resp = requests.get(url=GET_USER_URL)
        response = self.json2obj(resp.content.decode("utf-8"))
        print(response)
        return response

    def _json_object_hook(self, d):
        return namedtuple('X', d.keys())(*d.values())

    def json2obj(self, data):
        return json.loads(data, object_hook=self._json_object_hook)



