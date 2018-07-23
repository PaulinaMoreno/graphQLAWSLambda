import graphene
import sys
sys.path.append(".") 
from data import get_user
class User(graphene.ObjectType):
    userID = graphene.String()
    name = graphene.String()
    email = graphene.String()
    phone = graphene.String()
    friends = graphene.List(lambda: User)

    def resolve_friends(self, info):
        return [get_user(f) for f in self.friends]

class Query(graphene.ObjectType):
    user = graphene.Field(User, userID=graphene.String())

    def resolve_user(self, info, userID):
        return get_user(userID)

schema = graphene.Schema(query=Query)
