#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Query for pets db"""

import sqlite3
import sqlite3 as lite, sys


def main():
    conn = None
    try:
        conn = lite.connect('pets.db')
        while True:
            c = conn.cursor()
            user_id = int(input("Enter a Person ID or -1 to exit: "))
            if user_id == -1:
                break

            cur_query = "SELECT person.first_name, person.last_name, person.age FROM person WHERE id = ?"

            with conn:
                c.execute(cur_query, (user_id,))
                cur_person_data = c.fetchone()

            if cur_person_data is not None:
                print("%s %s %s years old" % (cur_person_data[0], cur_person_data[1], cur_person_data[2]))

                c.execute("DROP TABLE IF EXISTS person_pet_ids;")

                c.execute(
                    "CREATE TABLE person_pet_ids as SELECT pet_id FROM person_pet WHERE person_id = ?", (user_id,))

                c.execute(
                    "SELECT pet.name, pet.breed, pet.age, pet.dead FROM pet JOIN person_pet_ids ON person_pet_ids.pet_id = pet.id;")

                data = c.fetchall()

                for cur_data in data:
                    if cur_data[3] == 1:
                        out = ("owned", "was")
                    else:
                        out = ("owns", "is")

                    print("%s %s %s %s, a %s, that %s %d years old" % (
                        cur_person_data[0], cur_person_data[1], out[0], cur_data[0], cur_data[1], out[1], cur_data[2]))

        conn.commit()
    except lite.Error as e:
        print("Error")
    finally:
        if conn:
            conn.close()


main()
