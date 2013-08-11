import requests
import random
import Queue


def getPic(lat, lng, res):
    
    loc = str(lat) + ',' + str(lng)
    resBox = str(res) + 'x' + str(res)
   
    pList = {'size': resBox, 'center': loc, 'sensor': "false", 'maptype': "satellite", 'zoom': 12}

    req = requests.get("http://maps.googleapis.com/maps/api/staticmap?", params = pList, stream = True)
    
    #TODO: implement saving system with name as lat/long or something
    """output = open('')"""

def main():
    #number of constituent pictures
    numPics = 200
    #side length of each picture
    side = 200

    #Queues that hold the lat/lng
    latQ = Queue.Queue(numPics)
    lngQ = Queue.Queue(numPics)
    
    #generate random lat/lng
    for i in range(numPics):
        randLat = round(random.random() * 90, 2)
        randLng = round(random.random() * 180, 2)

        print randLat

        negLat = random.getrandbits(1)
        negLng = random.getrandbits(1)

        if negLat == 1:
            randLat *= -1

        if negLng == 1:
            randLng *= -1


        latQ.put(randLat)
        lngQ.put(randLng)

    while !lngQ.empty():
        getPic(latQ.get(), lngQ.get(), side)   

if __name__ ==  '__main__':
    main()





