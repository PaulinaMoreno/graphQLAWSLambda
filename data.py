import boto3
import os
import json
import sys
from botocore.exceptions import ClientError
from botocore.errorfactory import BaseClientExceptions
from os.path import dirname, join


class DynamoDB:
    def __init__(self):
        self.connection = boto3.resource('dynamodb', region_name='us-west-2')

    def buildExpression(self, data):
        vals = {}
        exp = 'SET '
        attr_names = {}
        for key, value in data.items():
            vals[':{}'.format(key)] = value
            attr_names['{}'.format(key)] = key
            exp += '{} = :{},'.format(key, key)
        exp = exp.rstrip(",")
        return vals, exp

    def put_item(self,Table, Item, ConditionExpression ):
        try:
            table = self.connection.Table(Table)
            response_user_to_friend = table.put_item(
                Item,
                ConditionExpression
            )
            return response_user_to_friend
        except ClientError as e:
            raise e
    def delete_Items(self, Table, l_items, keyID_pr, KeyID_sec):
        try:
            table = self.connection.Table(Table)
            with table.batch_writer() as batch:
                for item in l_items:
                    print(item)
                    batch.delete_item(
                        Key={
                                keyID_pr: item[keyID_pr],
                                KeyID_sec: item[KeyID_sec]
                            }
                        )
                    print(batch)
            return True
        except ClientError as e:
            raise e

    def update(self, table, keyID, keyValue, dataParamethers):
        table = self.connection.Table(table)
        vals, update_expression = self.buildExpression(dataParamethers)
        try:
            ExpressionAttributeValues = vals,
            UpdateExpression = update_expression

            result = table.update_item(
                Key={
                    keyID: keyValue
                },
                ExpressionAttributeValues=vals,
                UpdateExpression=update_expression,
                ReturnValues='ALL_NEW',
        )
            responseJson = {
                "statusCode": 200,
                "headers": {"Content-Type": 'application/json'},
                "body": 'Update user on dynamodb'
            }
            return responseJson
        except Exception as err:
            responseJson = {
                "statusCode": 400,
                "headers": {"Content-Type": 'application/json'},
                "body": str(err)
            }
            print(err)
            return responseJson

