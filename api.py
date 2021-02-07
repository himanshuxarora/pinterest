import flask
from feeder import main
import pyrebase
import json
import os
config={

}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/startbot', methods=['GET'])
def startbot():
    print("Bot has been started")
    botrun=True
    db.child('Pinterest').child('ShouldStartBot').set(True)
    main(botrun)
    return "<h1>Bot started"
@app.route('/stopbot', methods=['GET'])
def stopbot():
    print("Bot has been stopped")
    botrun=False
    db.child('Pinterest').child('ShouldStartBot').set(False)
    return "<h1>Bot stopped"
app.run()
