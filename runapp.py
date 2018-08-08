# flask_sqlalchemy/app.py
from flask import Flask
from graphene import ObjectType, String, Schema
from flask_graphql import GraphQLView
from schema import schema
from data import setup

setup()
app = Flask(__name__)
app.debug = True


app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/')
def index():
	return "Go to /graphql"

if __name__ == "__main__":
	app.run()
