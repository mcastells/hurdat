'''
@author: Marc Castells
'''
import datetime

class StormRecord:
    def __init__(self, data):
        for i in range(len(data)):
            data[i] = data[i].strip(',') # remove commas from each of the list elements
        date = data[0]
        year = int(date[0:4])
        month = int(date[4:6])
        day = int(date[6:8])
        hour = int(int(data[1])/100)
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.datetime = datetime.datetime(year, month, day, hour)
        self.record = data[2]
        self.category = data[3]
        lat = data[4]
        lon = data[5]
        self.lat = float(lat.strip('N')) if lat.find('N') >= 0 else -1 * float(lat.strip('S'))
        self.lon = float(lon.strip('E')) if lon.find('E') >= 0 else -1 * float(lon.strip('W'))
        self.maxwspeed = int(data[6])
        self.minpressure = int(data[7])
        self.NE34 = int(data[8])
        self.SE34 = int(data[9])
        self.SW34 = int(data[10])
        self.NW34 = int(data[11])
        self.NE50 = int(data[12])
        self.SE50 = int(data[13])
        self.SW50 = int(data[14])
        self.NW50 = int(data[15])
        self.NE64 = int(data[16])

class Storm:
    def __init__(self, data):
        for i in range(len(data)):
            data[i] = data[i].strip(',') # remove commas from each of the list elements
        self.id = data[0]
        self.name = data[1]
        self.record_count = int(data[2])
        self.records = []

def listFromFile(filename):
    storms = [] # initialize an empty list of Storms
    data = open(filename, 'r')
    line = data.readline() # read the first line of data
    while line: # repeat this loop as long as there is data to be read
        if line[0].isalpha(): # if the first letter of the row is a letter then it is defining a storm
            storm = Storm(line.split()) # parse the line of data into a Storm object
            for i in range(storm.record_count): # read a line of data for each record
                line = data.readline()
                stormRecord = StormRecord(line.split()) # parse the line of data into a StormRecord object
                storm.records.append(stormRecord) # add the StormRecord object to the storm's list of records
            storms.append(storm) # add the Storm object to the list
        line = data.readline() # this causes the while loop to continue as long as there is data to be read
    data.close()
    return storms