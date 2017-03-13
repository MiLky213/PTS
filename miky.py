import getpass

def login():    
    passw = getpass.getpass("Password: ")
    f = open("users.txt", "r")
    for line in f.readlines():
        us, pw = line.strip().split("|")
        if (passw in pw):
            print ("Login successful!")
            return True
    print ("Wrong username/password")
    return False


hrac = []
def points(name, num):
    log = login()
    if log == True:
        for i in range(len(hrac)):
            if hrac[i]['name'] == name:
                hrac[i]['body'] = num
                return
        hrac.append({"name":name, "body": num, "dospely": True})


def reduce(num):
    log = login()
    if log == True:
        for i in hrac:
            pocet = hrac[i]['body']
            hrac[i]['body'] = int(pocet - num)

def junior(name):
    log = login()
    if log == True:
        for i in range(len(hrac)):
            if hrac[i]['name'] == name:
                hrac[i]['dospely'] = False
                return
        
        
def ranking():
    log = login()
    if log == True:
        vysl = ""
        newlist = sorted(hrac, key=lambda k: k['body'])
        print("Tabulka:")
        for i in range(len(newlist)):
            print("Meno: " + newlist[i]['name'] + ", body: " + str(newlist[i]['body']))
            

def rankingJunior():
    log = login()
    if log == True:
        vysl = ""
        newlist = sorted(hrac, key=lambda k: k['body'])
        for i in range(len(newlist)):
            if newlist[i]['dospely'] == False:
                print("Meno: " + newlist[i]['name'] + ", body: " + str(newlist[i]['body']))

def quit():
    log = login()
    if log == True:
        exit()


