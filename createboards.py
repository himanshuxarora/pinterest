import pyrebase
import time
import json
import pinterest
config = {
 
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
app_id="5051142199337596183"
access_token="AtNFqUPaUfimVA9jgzdnWvUt5bP8Fcg7PGBitmpGGUMRdYC1FwQ3ADAAACs5Ri_HYurAxNoAAAAA"
link = pinterest.oauth2.authorization_url(app_id,'https://api.pinterest.com')
api = pinterest.Pinterest(token=access_token)
#a=api.boards()
'''
print(board,type(board))
time.sleep(720)
data=a["data"]
dic={}
for i in data:
    id=i["id"]
    category=i["url"]
    category=category.split("eventscene/")[1].split("/")[0]
    print(category,id)
    dic[category]=id
db.child('Pinterest').child('createdboards').set(json.dumps(dic))
'''
createdboards=json.loads(db.child('Pinterest').child('createdboards').get().val())
allboards=json.loads(db.child('Pinterest').child('allboards').get().val())
list1=list(createdboards.keys())
createdboardss=[]
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
list1.sort()
allboards.sort()
print(len(list1))
print("\n\n\n\n")
print(len(allboards))
