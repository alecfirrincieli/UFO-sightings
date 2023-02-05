



import csv
filepath = "ufo-sightings.csv"
ufosightings = [] 

with open("ufo-sightings.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames)
    
    for row in reader:
        ufosightings.append(row)

    



#How many sightings were there in total?
        
ufosightings_count = 0

for row in ufosightings:
    ufosightings_count += 1
    
print('There were ',str(ufosightings_count), ' ufo sightings.' )


#How many sightings were there in the US?  


sightings_us = [row for row in ufosightings if row['country'] == 'us']

print('There were',len(sightings_us), 'in the US.')




'''
Finds the "fireball" sighting(s) that lasted more than ten seconds in US.  '''

#First, define a Python function that checks if a given duration (seconds) is "valid"
def is_valid_duration(duration_as_string):
    try:
        duration = float(duration_as_string)
        
    except ValueError:
        
        return False
        
    else:
        return float(duration)
    
fball = [row for row in sightings_us if(is_valid_duration(row['duration (seconds)']) > 10) and row['shape'] == 'fireball']


#for row in fball:

  #print(row['datetime'], row['state'])



'''
Sorts the above list by duration and gives the datetime and duration of the
longest sighting?  


'''
fballsorted = sorted(fball, key = lambda x: float(x['duration (seconds)']), reverse=True)


print('The longest fireball sighting in US was at', fballsorted[0]['datetime'],'and lasted', fballsorted[0]['duration (seconds)'],'seconds')





'''
Finds whhat state had the longest lasting "fireball"
'''

state = fballsorted[0]['state']

print(state,'had the longest lasting fireball sighting in US')


#

'''
 
Filters out these extraneous records (sightings of 0 seconds)
and gets the shortest sighting overall now.  

'''

notzero = [row for row in ufosightings if (is_valid_duration(row['duration (seconds)']) > 0)]

min_duration_info = min(notzero, key = lambda x:x['duration (seconds)'])

min_duration = float(min_duration_info['duration (seconds)'])

print("The shortest overall sighting was", str(min_duration), "seconds")



#Gives the top 3 shapes sighted and how many sightings were there for each

sightings_shapes = [row['shape'] for row in ufosightings]

count = {}

for shape in sightings_shapes:
    count[shape] = count.get(shape, 0) + 1


count_items = count.items()

for key, value in count_items:
    count_items_sorted = sorted(count_items, key = lambda x: x[1], reverse = True)
    
top3shapes = []

for i in range(3):
    top3shapes.append(count_items_sorted[i])
    
print('The top three shapes spotted were',top3shapes)



