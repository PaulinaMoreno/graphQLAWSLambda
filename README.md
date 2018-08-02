
# Flask + Graphene + AWS lambda
This repository provide a simple project to build a **GraphQL API with Flask and Graphene**. Its content has been largely inspired by the references below but code has been modified and add extra steps to create an AWS Lambda function using Zappa

# Tutorial
The [Github Wiki](https://github.com/alexisrolland/flask-graphene-sqlalchemy/wiki) provides detailed design intentions in a step by step tutorial.

# References
* https://github.com/alexisrolland/flask-graphene-sqlalchemy
* [Star Wars API](https://swapi.co)

# Requirements
This project has been developed on **MacOs** with **Python 3.6**. It is using the following third party packages. To install them, open a terminal window, change directory to the project folder and execute the following command:

`$ pip3 install flask graphene flask-graphql`


# Run 
  Run the next query for test:
  `query UserNameAndFriendsQuery {
          user(userID: "1000"){
            userID
            name
            friends {
              name
            }
          }
        }
        `
  Result:
  ![query result](https://github.com/PaulinaMoreno/graphQLAWSLambda/blob/master/query.png)
# AWS Lambda + Zappa

## Installation and Configuration
Before you begin, make sure you are running Python 3.6 and you have a valid AWS account and your [AWS credentials file](https://blogs.aws.amazon.com/security/post/Tx3D6U6WSFGOK2H/A-New-and-Standardized-Way-to-Manage-Credentials-in-the-AWS-SDKs) is properly installed.

## Running the Initial Setup / Settings

**Zappa** can automatically set up your deployment settings for you with the `init` command:

    $ zappa init

This will automatically detect your application type (Flask/Django - Pyramid users [see here](https://github.com/Miserlou/Zappa/issues/278#issuecomment-241917956)) and help you define your deployment configuration settings. Once you finish initialization, you'll have a file named *zappa_settings.json* in your project directory defining your basic deployment settings. It will probably look something like this for most WSGI apps:

```javascript
{
    // The name of your stage
    "dev": {
        // The name of your S3 bucket
        "s3_bucket": "lmbda",

        // The modular python path to your WSGI application function.
        // In Flask and Bottle, this is your 'app' object.
        // Flask (your_module.py):
        // app = Flask()
        // Bottle (your_module.py):
        // app = bottle.default_app()
        "app_function": "your_module.app"
    }
}
```
Now, you're ready to deploy!

## Basic Usage

## Initial Deployments

Once your settings are configured, you can package and deploy your application to a stage called "dev" with a single command:

    $ zappa deploy dev
    Deploying..
    Your application is now live at: https://7k6anj0k99.execute-api.regionx.amazonaws.com/dev
