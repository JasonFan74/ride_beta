from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "ride_beta"}
app.config["SECRET_KEY"] = "TH3S3CR3T" #TODO...

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from ride_beta.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
    app.run()