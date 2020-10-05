#!/usr/bin/env python

__author__ = 'Manuel Velasco'

import requests
import turtle
import time


def astronaut_info():
    """list of the astronauts who are currently in space. Print their full names, the spacecraft they are currently on board, and the total number of astronauts in space."""

    astronauts_names = requests.get("http://api.open-notify.org/astros.json")

    list_name = astronauts_names.json()["people"]

    print(f'number of astronaut {len(list_name)}')

    for value in list_name:
        print(f"{value['name']} on abort {value['craft']}")


def location_iss():
    """ current geographic coordinates (lat/lon) of the space station, along with a timestamp"""

    loc_iss = requests.get("http://api.open-notify.org/iss-now.json")

    time_stamp = loc_iss.json()["timestamp"]
    lat_long = loc_iss.json()["iss_position"]
    print('current location:')
    print(f'latitude: {lat_long["latitude"]}')
    print(f'longitude: {lat_long["longitude"]}')
    print()

    return lat_long


def ctime_time():
    payload = {'lat': 39.7684, 'lon': -86.1581}
    r = requests.get(
        "http://api.open-notify.org/iss-pass.json", params=payload)
    t = r.json()['response'][0]['risetime']
    return time.ctime(t)


def indiana_location():
    city = ctime_time()

    i = turtle.Turtle()
    i.penup()
    lat_i = 39.7684
    long_i = -86.1581
    i.goto(long_i, lat_i)

    i.dot(15, "yellow")
    i.color('red')

    i.write(city, font=20)
    print(city)
    i.hideturtle()


def turtle_world():
    a = location_iss()
    print(a)
    map_gif = turtle.Screen()
    map_gif.setup(width=720, height=360)
    map_gif.bgpic("map.gif")

    map_gif.setworldcoordinates(-180, -90, 180, 90)

    map_gif.addshape('iss.gif')
    indiana_location()

    t = turtle.Turtle()
    t.shape('iss.gif')
    t.penup()
    t.goto(float(a["longitude"]), float(a["latitude"]))
    turtle.done()


def main():

    astronaut_info()

    turtle_world()


if __name__ == '__main__':
    main()
