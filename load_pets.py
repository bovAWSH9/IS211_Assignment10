#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Load Pets into db"""

import sqlite3
import sqlite3 as lite, sys


def main():
    conn = None
    try:
        conn = lite.connect('pets.db')
        with conn:
            c = conn.cursor()
            """insert into person table"""
            c.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(1,'James','Smith',41);")
            c.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(2, 'Diana', 'Greene', 23);")
            c.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(3, 'Sara', 'White', 27);")
            c.execute("INSERT INTO person(id, first_name,last_name,age) VALUES(4, 'William','Gibson', 23);")

            """insert into pet table"""
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(1, 'Rusty', 'Dalmation',4,1);")
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(2, 'Bella', 'Alaskan Malamute',4,1);")
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(3, 'Max', 'Cocker Spaniel',1,0);")
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(4, 'Rocky', 'Beagle',7,0);")
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(5, 'Rufus', 'Cocker Spaniel',1,0);")
            c.execute("INSERT INTO pet(id, name, breed, age, dead) VALUES(6, 'Spot', 'Bloodhound',2,1);")

            """insert into person pet table"""
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1,1);")
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1,2);")
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(2,3);")
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(1,4);")
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(3,5);")
            c.execute("INSERT INTO person_pet(person_id, pet_id) VALUES(4,6);")

        conn.commit()
    except lite.Error as e:
        print("Error")
    finally:
        if conn:
            conn.close()


main()
