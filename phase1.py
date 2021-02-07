import os
import pyrebase
import time
import json
from requests import get
import datetime 
import os
import pinterest
import telebot
app_id="5051142199337596183"
access_token="AtNFqUPaUfimVA9jgzdnWvUt5bP8Fcg7PGBitmpGGUMRdYC1FwQ3ADAAACs5Ri_HYurAxNoAAAAA"
link = pinterest.oauth2.authorization_url(app_id,'https://api.pinterest.com')
api = pinterest.Pinterest(token=access_token)
config = {
  
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
bot = telebot.TeleBot("1039445462:AAFP-JurlD0OT6VSZqdL0Fqt5LbErzBr7Fw")
def send_log(log):
    log=str(log)
    chat_id ="-278653089"
    bot.send_message(chat_id,log)
    print("message sent")
global category
todo=[]
followed=[]
Done = []
settings = {}
finaldictscraper = {}
pinconnt = {}
categorydict={}
doneboards = []
history ={}
catandimages= {}
y={}
global categoryforpin
desc = []
cate = []
ctlink = []
donepins = {}
completedcategories = []
global title,description,draflink,address,allcats,pincounter
pincounter = 0
play = 0

def createpin(title,description,linkvenue,address,cat,imgurl):
        print("phase1.create pin start")
        global uname,donepins,pincounter,y
        path = os.getcwd()
        #cat = str(cat.replace(' ','-'))
        cat = str(cat.replace('-',' '))
        cat=cat.strip()
        path1=path.replace("scripts","image")
        path1=path1+"\semp.png"
        venuename=title.strip()
        venueaddress=address
        categoryname=cat
        des="Venue Name:    "+venuename+" Venue Address:    "+venueaddress+"."+" This venue is listed in the category "+categoryname+"."+"    You’ll find this image on their Event Scene venue profile. Please follow the link to view the full profile and more details about this Adelaide venue. Function venues in Adelaide South Australia"
        print(venueaddress)
        print(imgurl)
        print(cat)
        print(des)
        #print(linkvenue)
        boards=json.loads(db.child('Pinterest').child('createdboards').get().val())
        #api.pin().create('303711637310524976', des, linkvenue, image_url=imgurl)
        cat=boards[cat]
        print(cat)
        log={}
        log={'category':cat,'destination link':des,'linkvenue':linkvenue,'image_url':imgurl}
        api.pin().create(cat, des, linkvenue, image_url=imgurl)
        try:
            send_log(log)
        except Exception as e:
            send_log(e)
        print("phase1.createpin() fin")


def catextractionforboard():
        global categorydict,doneboards
        print('phase1.catextractionforboard() start')
        cats = categorydict.keys()
        try:
                for cat in cats:
                        if(cat not in doneboards):
                                #board_edit(cat)
                                #doneboards.append(cat)
                                db.child('Pinterest').child('doneboards').set(json.dumps(doneboards))
        except Exception as e:
                print("Exception in phase1.catextractionforboard",e)
        print("phase1.catextraction() fin")
def extractionforpin(cat):
        global finaldictscraper,title,description,draftlink,address,catandimages,donepins,play
        print('phase1.extractionforpin() start')
        counter = 0
        links = finaldictscraper.keys()        
        coonter = settings['pinsupdaily']
        coonter = int(coonter)
        sleeper = settings['timeintervalpin']
        z=[]
        y={}
        catandimages1 =json.loads(db.child('Pinterest').child('catandimages').get().val())
        catandimages={}
        keys=list(catandimages1.keys())
        for key in keys:
            k=key
            k=k.replace('~','/')
            k=k.replace(';','.')
            catandimages[k]=catandimages1[key]
        notFound=True
        for link in links:
                        if (cat in catandimages[link].keys()):
                                title = finaldictscraper[link]['title']
                                descript = finaldictscraper[link]['description']
                                linkvenue = finaldictscraper[link]['link']
                                address = finaldictscraper[link]['address']
                                try:
                                        z = donepins[cat]
                                except:
                                        print("108")
                                        pass
                                if(linkvenue not in z):
                                                print("111")
                                                img = catandimages[link][cat]
                                                createpin(title,descript,linkvenue,address,cat,img)
                                                z.append(linkvenue)
                                                donepins[cat] = z
                                                db.child('Pinterest').child('donepins').set(json.dumps(donepins))
                                                notFound = False
                                                play += 1
                                                break                         
        if (notFound == True):
            print("Not found",notFound)
            db.child('Pinterest').child('completedcategories').set(json.dumps(cat))
        else:
                pass
        return notFound
def onthiscategory():
        print("phase1.onthiscategory() started")
        global categorydict,completedcategories
        cats = categorydict.keys()
        for cat in cats:
                if(cat not in completedcategories):
                        a = extractionforpin(cat)
                        if(a == True):
                                pass
                        else:
                            return True
        print("phase1.onthiscategory() fin")    
def catandimglink(catandimages,finaldictscraper):
                print("phase1.catandimglink() started") 
                lnks = finaldictscraper.keys()
                counter = 0
                for link in finaldictscraper:
                        z={}
                        listimg = finaldictscraper[link]['images']
                        listcats = finaldictscraper[link]['categories']
                        for cat in listcats:
                                        z[cat]=listimg[counter%len(listimg)]
                                        counter+=1
                        catandimages[link]=z
                catandimages1={}
                keys=list(catandimages.keys())
                for key in keys:
                    k=key
                    k=k.replace('/','~')
                    k=k.replace('.',';')
                    catandimages1[k]=catandimages[key]
                db.child('Pinterest').child('catandimages').set(json.dumps(catandimages1))
                print("phase1.catandimglink() finished")
                
def start():
        print("phase1.start() started")
        global settings,finaldictscraper,categorydict,uname,doneboards,completedcategories,donepins
        try:
                completedcategories=json.loads(db.child('Pinterest').child('completedcategories').get().val())
                        
        except:
                pass
        date=(datetime.datetime.now()).strftime('%m-%d-%y')
        try:
                pintime = json.loads(db.child('Pinterest').child('pinCount').get().val())
                pincounter = pintime[date]['pincount']                                                
        except:
                pass
        settings = json.loads(db.child('Pinterest').child('Settings').get().val())
        categorydict=json.loads(db.child('Pinterest').child('categorydict').get().val())
        categorydict=json.loads(db.child('Pinterest').child('categorydict').get().val())
        allcats = categorydict.keys()
        finaldictscraper1 =json.loads(db.child('Pinterest').child('finaldictscraper').get().val())
        finaldictscraper={}
        keys=list(finaldictscraper1.keys())
        for key in keys:
            k=key
            k=k.replace('~','/')
            k=k.replace(';','.')
            finaldictscraper[k]=finaldictscraper1[key]
        dict = json.loads(db.child('Pinterest').child('Settings').get().val())
        uname = dict['uname']
        catandimages1 =json.loads(db.child('Pinterest').child('catandimages').get().val())
        catandimages={}
        keys=list(catandimages1.keys())
        for key in keys:
            k=key
            k=k.replace('~','/')
            k=k.replace(';','.')
            catandimages[k]=catandimages1[key]

        doneboards =json.loads(db.child('Pinterest').child('doneboards').get().val())
        donepins=json.loads(db.child('Pinterest').child('donepins').get().val())
        catandimglink(catandimages,finaldictscraper)
        print("phase1.start() finished")

        
        
        
                
        
        
        
