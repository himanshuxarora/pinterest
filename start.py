import pyrebase
import json
import os
config = {
  
}
#check in firebase to listen to even in which startbot is 1
#condition check if startbot 1 then proceed
firebase = pyrebase.initialize_app(config)
db = firebase.database()
def shouldstart(message):
        checker = message['data']
        print(checker)
        if checker==True:
                os.system('python3 feeder.py')
        else:
            pass
my_stream = db.child('Pinterest').child('ShouldStartBot').stream(shouldstart)
value=db.child('Pinterest').child('ShouldStartBot').get().val()
print("Botrun=",value)

		
