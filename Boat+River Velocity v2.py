#Andy Szeto
#7-17-2019
#Boat + River Velocity

import numpy as np


print('----------------------')
print('|  _ __   N  *__**_  |')
print('|  _*___     **      |')
print('|W       __   _ __* E|')
print('|  *__  /  \         |')
print('|   _   |__| S *__ _ |')
print('----------------------')

print("""You are on a boat crossing a river, the current
is strong. You have the ability to measure the speed of the current
(whose force is perpendicular to your boat). This program will enable you to calculate
the direction you are traveling, how far you will be displaced from your intended destination,
and the time duration of your trip\n""")

dirKeys = {'N': 360, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5, 'E': 90, 'ESE': 112.5, 'SE': 135,
               'SSE': 157.5, 'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5, 'W': 270, 'WNW': 292.5,
               'NW': 315, 'NNW': 337.5}

def compass():
    print('\nNow to determine wind conditions, we the current direction and speed')

    dirKeys = {'N': 360, 'NNE': 22.5, 'NE': 45, 'ENE': 67.5, 'E': 90, 'ESE': 112.5, 'SE': 135,
               'SSE': 157.5, 'S': 180, 'SSW': 202.5, 'SW': 225, 'WSW': 247.5, 'W': 270, 'WNW': 292.5,
               'NW': 315, 'NNW': 337.5}

    dirInput1 = input('Enter first direction: ').upper()
    dirInput2 = input('Enter second direction: ').upper()
    dirInput3 = input('Enter third direction: ').upper()

    dirVector = np.array([dirInput1, dirInput2, dirInput3])
    strDirVector = (str(dirVector[0] + dirVector[1] + dirVector[2]))

    for x in dirKeys:
            if (strDirVector == x):
                winDir = (dirKeys[x])
                wspdInput1 = int(input('\nWhat is the speed of the wind? (mph) '))
                windarr = np.array([wspdInput1, winDir])
                return (np.array(windarr))

            elif (strDirVector not in dirKeys):
                print('Directional Input Error\n ')
                break

##Boat and River Variables

vYb = int(input('What is the speed of your boat? (mph) '))
vXr = int(input('What is the speed of the river current? (mph) '))
boatV = np.array([0, vYb])
riverV = np.array([vXr, 0])


##Boat Vector
mag = np.sqrt((boatV[1]**2) + (riverV[0]**2))
direction = np.degrees(np.arctan((riverV[0] / boatV[1])))

rivDir = input('Which direction is the river current traveling? To your left or right? ').lower()
if rivDir == 'right':
    print('\nThe boat is currently drifting ' + str(mag) + ' mph away from your current location, at an angle of ' + str(
        direction) + ' degrees East of North')
elif rivDir =='left':
    print('\nThe boat is currently drifting ' + str(mag) + ' mph away from your current location, at an angle of ' + str(
        direction) + ' degrees West of North')

##Displacement

distCross = int(input('\nHow far is the shore from your location (straight line)? '))
displc = distCross *(np.tan(np.radians(direction)))

print('You will end up ' + str(displc) + ' miles from your intended location')

boatDist = np.sqrt((displc ** 2) + (distCross ** 2))
print('Time taken : ' + str(boatDist / mag) + ' hours')

##Wind Conditions

windVector = (compass())
windSpd = windVector[0]
windAngl = windVector[1]

print(windVector)

