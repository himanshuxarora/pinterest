import os
import time
import json
import phase1
from datetime import timedelta
import datetime
import pyrebase
settings={}
biglist = []
smallist = []
flowinglist= []
followdict = {}
followcount = {}
unfollowcount = {}
countertofollow = 0
counterforunfollow = 0
config={

}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
def main():
        print("follow.main() started")
        global settings,biglist,flowinglist,followdict
        try:
                with open('biglist.txt','r') as big:
                        biglist = big.read()
        except:
                print("folow.exception1")
                pass
        try:
                with open('flowinglist.txt','r') as flw:
                        flowinglist = flw.read().split('\n')
        except:
                pass
        try: 
                fld=db.child('Pinterest').child('followdict').get().val()
                fld=fld.replace("'",'"')
                followdict=json.loads(fld)
        except Exception as e:
                print(e)
                print("folow.exception3")
                pass
        stet=db.child('Pinterest').child('Settings').get().val()
        settings=stet
        try:
                with open('biglist.txt','r') as oj:
                        biglist=oj.read().split('\n')
        except:
                pass                
def lister():
        print("follow.lister() started")
        global biglist,smallist,settings
        with open('biglist.txt','r') as o:
                biglist = o.read().split('\n')
        stet=db.child('Pinterest').child('Settings').get().val()
        settings=stet
        try:
                biglist = list(set(biglist))
        except:
                pass
                                                        
def follow():
        print("follow.follow() started")
        global smallist,flowinglist,peopletofollow,followdict,followcount,countertofollow
        try:
                fld1={}
                print("line207",person)
                fld=db.child('Pinterest').child('followdict').get().val()
                fld=fld.replace("'",'"')
                fld=json.loads(fld)
                followdict=fld
        except:
                pass
        try : 
                flw=db.child('Pinterest').child('followCount').get().val()
                followcount=flw
        except:
                pass
        with open('biglist.txt','r') as ig:
                        smallist=ig.read().split('\n')
        print("smalllist",smallist)
        z={}
        p={}
        notfound = True
        date=(datetime.datetime.now()).strftime('%m-%d-%y')                
        try:
                person = smallist.pop()
                personi = person
                print("person",person)
                #api.follow_user(person)
                #time.sleep(720)
                print("line307")
                followdict[person]= z
                try: 
                        db.child('Pinterest').child('followdict').set(followdict)
                        print('line319',type(followdict))
                        try:
                                countertofollow+= 1
                                flowinglist.append(personi)
                                p['followcounter'] =countertofollow
                                followcount[date] = z
                                db.child('Pinterest').child('followcounter').set(followcount)
                        except Exception as e:
                                print("except3",e)
                                pass
                                        
                except Exception as e:
                        print("except4",e)
                        pass                
        except:
                pass
                
        with open('smallist.txt','w') as ig:
                ig.write('\n'.join(smallist))
        print(len(flowinglist)) 
        with open('flowinglist.txt','w') as fl:
                fl.write('\n'.join(flowinglist))
        print("follow.follow() finished")
                
def unfollow():
        global flowinglist,peopletofollow,unfollowcount,followdict,counterforunfollow
        print("follow.unfollow() started")
        p={}
        with open('flowinglist.txt','r') as fl:
                flowinglist = fl.read().split('\n')
        print("flowinglist",flowinglist)
        fw=db.child('Pinterest').child('followdict').get().val()
        followdict=fw
        date=datetime.datetime.now()
        dtnow = date
        z={}              
        try:
                person = flowinglist.pop(0)
                print("person",person)
                dat = followdict[person]['time']
                dat = datetime.datetime.strptime(dat, '%m-%d-%y')
                dtunf = int(settings['daysafterunfollow'])
                dys = 24*dtunf
                if((dat+timedelta(hours=dys))<dtnow):
                        print("going to unfollow")
                        #api.unfollow_user(person)
                        #time.sleep(720)
                else:
                        flowinglist.append(person)
                with open('flowinglist.txt','w') as fp:
                        fp.write('\n'.join(flowinglist))
        except Exception as e:
                print("line464",e)
                with open('flowinglist.txt','w') as fp:
                        fp.write('\n'.join(flowinglist))
        print("follow.unfollow() finished")
