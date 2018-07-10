import sys
sys.path.append(".") 
user_data = []
friendShip_data = []


def setup():
    
    from schema import User, FriendShip
    global user_data
    global friendShip_data
    luke = User(
        userID="1000",
        name="Luke Skywalker",
        email="lukeskywalker@gmail.com",
        phone="+4084665573",
        friends=[],
    
    )

    vader = User(
        userID="1001",
        name="Darth Vader",
        email="darkvader@gmail.com",
        phone="+4084687956",
        friends=[],
    )

    han = User(
        userID="1002",
        name="Han Solo",
        email="hansolito@gmail.com",
        phone="+4084689120",
        friends=[],
    )

    leia = User(
        userID="1003",
        name="Leia Organa",
        email="leiaorg@gmail.com",
        phone="+4086884546",
        friends=[],
    )

    luke.friends.append(leia)
    luke.friends.append(han)

    han.friends.append(leia)
    han.friends.append(luke)

    leia.friends.append(luke)
    leia.friends.append(han)

    user_data.append(leia)
    user_data.append(han)
    user_data.append(vader)
    user_data.append(luke)


def set_friendship_value(f):
    print (f.userID)
    friendShip_data.append(f)
def delete_friendship_value(u):
    for f in friendShip_data:
        if f.userID == u.userID and f.friendID == u.friendID:
            friendShip_data.remove(f)
def get_friendship_value():
    for f in friendShip_data:
        print(f.userID, f.friendID)
def get_user(userID):
    for user in user_data:
        if user.userID == userID:
            return user
def get_all_users():
    return user_data

def get_friends(user):
    return map(get_user, user.friends)

