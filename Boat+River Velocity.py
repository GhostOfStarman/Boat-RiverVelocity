#Andy Szeto
#7-17-2019
#Boat + River Velocity

import numpy as n


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

vYb = int(input('What is the speed of your boat? (mph) '))
vXr = int(input('What is the speed of the river current? (mph) '))

def current():
    boatV = n.array([0, vYb])
    riverV = n.array([vXr, 0])

    mag = n.sqrt((boatV[1]**2) + (riverV[0]**2))
    direction = n.degrees(n.arctan((riverV[0] / boatV[1])))

    rivDir = input('Which direction is the river current traveling? To your left or right? ').lower()
    if rivDir == 'right':
        print('\nThe boat is currently drifting ' + str(mag) + ' mph away from your current location, at an angle of ' + str(
            direction) + ' degrees East of North')
    elif rivDir =='left':
        print('\nThe boat is currently drifting ' + str(mag) + ' mph away from your current location, at an angle of ' + str(
            direction) + ' degrees West of North')

    distCross = int(input('\nHow far is the shore from your location (straight line)? '))
    displc = distCross * (n.tan(direction))
    print('You will end up ' + str(displc) + ' miles from your intended location')

    boatDist = n.sqrt((displc ** 2) + (distCross ** 2))
    print('Time taken : ' + str(boatDist / mag) + ' hours')

current()
