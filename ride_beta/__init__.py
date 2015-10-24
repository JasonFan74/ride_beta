from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "ride_beta"}
app.config["SECRET_KEY"] = "TH3S3CR3T" #TODO...

db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from ride_beta.views import rides
    app.register_blueprint(rides)

register_blueprints(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()