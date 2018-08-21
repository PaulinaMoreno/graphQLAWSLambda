import graphene
import sys
import requests
sys.path.append(".") 
from requests_aws_sign import AWSV4Sign
from boto3 import session
from resolvers import Resolver

class User(graphene.ObjectType):
    userID = graphene.String()
    #name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    userCreateDate = graphene.DateTime()
    userStatus = graphene.String()
    enabled = graphene.Boolean()
    # friends = graphene.List(lambda: User)
    

    # def resolve_friends(self, info):
    #     return userID
              

class FriendShip(graphene.ObjectType):
    userID = graphene.String()
    friendID = graphene.String()

# Used to Create new friendship
class createFriendRelation(graphene.Mutation):
    class Arguments:
        userID = graphene.String()
        friendID = graphene.String()

    ok = graphene.Boolean()
    friendship = graphene.Field(lambda: FriendShip)

    def mutate(self, info, userID, friendID):
        friendship = FriendShip(userID=userID, friendID=friendID)
        set_friendship_value(friendship)
        ok = True
        return createFriendRelation( friendship=friendship, ok=ok)   
class deleteFriendRelation(graphene.Mutation):
    class Arguments:
        userID = graphene.String()
        friendID = graphene.String()

    ok = graphene.Boolean()
    deletefriendship = graphene.Field(lambda: FriendShip)

    def mutate(self, info, userID, friendID):
        deletefriendship = FriendShip(userID=userID, friendID=friendID)
        delete_friendship_value(deletefriendship)
        ok = True
        return deleteFriendRelation( deletefriendship=deletefriendship, ok=ok)  

class Query(graphene.ObjectType):
    user = graphene.Field(User, userID=graphene.String())
    userFriends = graphene.List(User)

    def resolve_user(self, info, userID):
        return Resolver.get_user(userID)
    def resolve_userFriends(self, info, userID):
        return Resolver.get_all_users_friends(userID)

class MyMutations(graphene.ObjectType):
    create_friend_relation = createFriendRelation.Field()
    delete_friend_relation = deleteFriendRelation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)