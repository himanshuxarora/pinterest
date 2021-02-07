import os
import pyrebase
import time
import json
import datetime 
import phase1
import follow
import pinterest
import flask
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()
global settings
settings={}
config = {
  
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
api_creds=db.child('Pinterest').child('api_creds').get().val()
#app_id=api_creds['app_id']
#access_token=api_creds['token']
app_id="5051142199337596183"
access_token="AtNFqUPaUfimVA9jgzdnWvUt5bP8Fcg7PGBitmpGGUMRdYC1FwQ3ADAAACs5Ri_HYurAxNoAAAAA"
link = pinterest.oauth2.authorization_url(app_id,'https://api.pinterest.com')
api = pinterest.Pinterest(token=access_token)
botrun=db.child('Pinterest').child('ShouldStartBot').get().val()

def main():
                global settings
                phase1.start()
                pinconnt = {}
                flwconnt = {}
                unflwconnt = {}
                botrun=db.child('Pinterest').child('ShouldStartBot').get().val()
                while(botrun==True):
                        cred = json.loads(db.child('Pinterest').child('Settings').get().val())
                        settings = cred 
                        print("BOTRUN=",botrun)
                        time.sleep(5)
                        pinup = int(settings['pinsupdaily'])
                        print("pins to be created",pinup)
                        try:
                                date=(datetime.datetime.now())
                                datey =(datetime.datetime.now()).strftime('%m-%d-%y')
                                pn = json.loads(db.child('Pinterest').child('pinCount').get().val())
                                pC = pn 
                                pList = list(pC.keys())
                                a = pList[-1]
                                a=datetime.datetime.strptime(a, '%m-%d-%y')
                                c = date - a
                        except Exception as e:
                                print('exception1 of feeder.main()')
                                print(e)
                                quit()
                                c = datetime.timedelta(days=1)
                                pass
                
                        y={}
                        z={}
                        x={}
                        try:
                                Po=json.loads(db.child('Pinterest').child('pinCount').get().val())
                                pinconnt = Po
                        except:
                                print('exception2 of feeder.main()')
                                pass
                        try:
                                mycounter = int(pinconnt[datey])
                                print("Today's pins are=",mycounter)
                        except:
                                print('exception3 of feeder.main()')
                                mycounter = 0
                                pass
                        if(True):
                                        print("Mycounter",mycounter,"pinup",pinup)
                                        while(mycounter < pinup):
                                                botrun=db.child('Pinterest').child('ShouldStartBot').get().val()
                                                if(botrun==True):
                                                        print("BOTRUN=",botrun)
                                                        try:
                                                                valu=phase1.onthiscategory()
                                                                if(valu==True):
                                                                    mycounter += 1
                                                                    print(pinconnt,"dfdfd",mycounter,"sdsd",datey)
                                                                    pinconnt[str(datey)] = mycounter
                                                                    db.child('Pinterest').child('pinCount').set(json.dumps(pinconnt))
                                                                print("pin created",valu)
                                                                print("sleeping for 20 minutes")
                                                                for i in range(0,724):
                                                                        print(i)
                                                                        time.sleep(1)
                                                                print("Sleep time finished")
                                                                print(mycounter,pinup)
                                                                lo = json.loads(db.child('Pinterest').child('pinCount').get().val())
                                                                time.sleep(int(settings['timeintervalpin']))
                                                        except Exception as e:
                                                                print('exception4 of feeder.main()')
                                                                print("Exception is",e)
                                                                pass
                                                        
                        else:
                                print('in else of feeder.main()')
                                print(c)
main()
'''
app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/startbot', methods=['GET'])
def startbot():
        global botrun
        print("Bot has been started")
        botrun=True
        main()
        return "Bot started"
@app.route('/stopbot', methods=['GET'])
def stopbot():
        global botrun
        print("Bot has been stopped")
        botrun=False
        return "Bot stopped"
@app.route('/createboards', methods=['GET'])
def createboards():
    createdboards=json.loads(db.child('Pinterest').child('createdboards').get().val())
    allboards=json.loads(db.child('Pinterest').child('allboards').get().val())
    list1=list(createdboards.keys())
    createdboardss=[]
    new=0
    all=0
    for ab in list1:
        ab=ab.replace("-"," ")
        ab=ab.strip()
        ab=ab.upper()
        createdboardss.append(ab)
    for b in allboards:
        b=str(b)
        b=b.strip()
        b1=b.upper()
        if(b1 in createdboardss):
            print(b," board already exists:",b)
        else:
            try:
                board=api.board().create(b)
                id=board["data"]["id"]
                createdboards[b]=""
                db.child('Pinterest').child('createdboards').set(json.dumps(createdboards))
                print("new board created:",b)
                for i in range(0,723):
                    time.sleep(1)
                    print("i",i)
            except Exception as e:
                print("exception",e)
                pass
        
    return "Boards created"        
port = int(os.environ.get('PORT', 8000))
app.run(host='0.0.0.0',port=port)
#app.run()
'''
