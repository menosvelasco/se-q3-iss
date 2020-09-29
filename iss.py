#!/usr/bin/env python

__author__ = 'Manuel Velasco'

import requests


def astronaut_info():
    astronauts_names = requests.get("http://api.open-notify.org/astros.json")

    list_name = astronauts_names.json()["people"]

    print(f'number of astronaut {len(list_name)}')

    for value in list_name:
        print(f"{value['name']} on abort {value['craft']}")


def location_iss():
    loc_iss = requests.get("http://api.open-notify.org/iss-now.json")

    time_stamp = loc_iss.json()["timestamp"]
    lat_long = loc_iss.json()["iss_position"]
    print('current location:')
    print(f'latitude: {lat_long["latitude"]}')
    print(f'longitude: {lat_long["longitude"]}')
    print()
    print(f'time: {time_stamp}')
    return lat_long


def tur():
    a = location_iss()


def main():

    astronaut_info()

    tur()


if __name__ == '__main__':
    main()
