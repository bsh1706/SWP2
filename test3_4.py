import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
        print(scdb)
        # print(type())
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    # for k in scdb:
    #     print(k['Score'])
    #     # print(type(k['Score']))
    # print(scdb)
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except IndexError as e:
                print("올바른 값을 입력해주세요.")

        elif parse[0] == 'del':
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)    
                    break
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == "find":
            for k in scdb:
                if k["Name"] == parse[1]:
                    print(k)
        elif parse[0] == "inc": # Score의 값이 str형태라 정수형태로 더해지지 않음
            for j in scdb:
                if j['Name'] == parse[1]:
                    j['Score'] += (parse[2])
                    print(j)
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
