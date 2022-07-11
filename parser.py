
import sqlite3
conn = sqlite3.connect(r'newdb.db')
cur = conn.cursor()

# cur.execute("""create table  headers(stars text,name text,description text);""")
cur.execute("delete from headers where 1=1")
conn.commit()
data= open('output.json',encoding='utf-8').read().replace("\n\n",'\n').replace("\n\n",'\n').split("@@@@@@@@@@@@@@@@@@@\n")
for (i,rest) in enumerate( data ):
    data[i]=rest.split("#####\n")
    for (j,row)in enumerate(data[i]):
        data[i][j]=row.split("\n")
score,all,emptyHead,hotel,less2=0,0,0,0,0

def isHotel(arr):
    for a in arr:
        if a.find('отель')!=-1 or a.find('Отель')!=-1 or a.find('hotel')!=-1 or a.find('Hotel')!=-1:
            return True
    return False



for rest in data:
    if(len(rest)<2):
        continue
    if (len(rest[0])<3 or isHotel(rest[1])):
        continue
    # stars text,name text,description text
    print(rest[0],len(rest[0]))
    # print((rest[0][0],rest[0][1],rest[0][2]))
    cur.executemany("INSERT INTO headers VALUES(?, ?, ?);", [(rest[0][0],rest[0][1],rest[0][2])])
    conn.commit()


# cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
# conn.commit()

    # score+= int(len(rest[0])<2 and isHotel(rest[1]))
    # hotel+=int(isHotel(rest[1]))
    # emptyHead+=int(len(rest[0])<2)
    # if(int(len(rest[0])<2)):
    #     print(rest)
    
    # all+=1
# print(emptyHead)
# print(hotel)
# print(score)
# print(all)
# print(less2)


