import graphene
import sys
sys.path.append(".") 
from data import setup, get_all_users , set_friendship_value, delete_friendship_value, get_friendship_value
setup()
class User(graphene.ObjectType):
    userID = graphene.String()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    friends = graphene.List(lambda: User)

    def resolve_friends(self, info):
        return get_friendship_value(self.friends)

class FriendShip(graphene.ObjectType):
    userID = graphene.String()
    friendID = graphene.String()

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
    allUsers = graphene.List(User)
    def resolve_user(self, info, userID):
        return get_user(userID)
    def resolve_allUsers(self, info):
        return get_all_users()

class MyMutations(graphene.ObjectType):
    create_friend_relation = createFriendRelation.Field()
    delete_friend_relation = deleteFriendRelation.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)

