# ------------------------------------   Simple Data Base APP     -----------------------------------
# Author    : Ahmed Atef Ahmed
# file name : simple_DB.py
# ---------------------------------------------------------------------------------------------------

# import sqlite library
import sqlite3

# create and connect dataBase
db = sqlite3.connect("app.db")

# trans to cursor
cr = db.cursor()

# create dataBase Table
cr.execute("create table if not exists skills(name text , progress integer , user_id integer)")


# save changes and close
def commit_and_close():
    """ commit changes and close the database """
    db.commit()
    db.close()
    print("connection to database is closed")


# user_ID
uID = 2

input_message = """
what do you want to do?
"s" => show all skills.
"a" => add new skill.
"d" => delete a skill.
"u" => update skill progress.
"q" => quit the app.
chose option :      
"""

# take user choice
user_input = input(input_message).strip().lower()

# list of available commands
command_list = ['s', 'a', 'd', 'u', 'q']


# methods
def show_skills():
    cr.execute(f"select * from skills where user_id = '{uID}'")
    result = cr.fetchall()
    print(f"you have {len(result)} skills.")
    if len(result) > 0:
        print("showing skills with progress :")
    for row in result:
        print(f"user_skill=> {row[0]} , ", end=" ")
        print(f"user_progress=> {row[1]}%")

    commit_and_close()


def add_skill():
    sk = input("write skill name :").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = '{uID}'")
    result = cr.fetchone()

    if result is None:
        prog = input("write skill progress :").strip()
        cr.execute(f"insert into skills(name , progress , user_id) values('{sk}' , '{prog}' , '{uID}')")
    else:
        user = input("skill is already exists , Do you want to update the progress ? y / n")
        if user == 'n':
            pass
        elif user == 'y':
            sk = input("write skill name :").strip().capitalize()
            prog = input("write skill progress :").strip()
            cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uID}'")
        else:
            print("wrong choice.")

    commit_and_close()


def delete_skill():
    sk = input("write skill name :").strip().capitalize()
    cr.execute(f"delete from skills where name = '{sk}' and user_id='{uID}'")
    commit_and_close()


def update_skill_progress():
    sk = input("write skill name :").strip().capitalize()
    prog = input("write skill progress :").strip()
    cr.execute(f"update skills set progress = '{prog}' where name = '{sk}' and user_id = '{uID}'")
    commit_and_close()


# check of user input
if user_input in command_list:
    print(f"command \"{user_input}\" found")
    if user_input == 's':
        show_skills()
    elif user_input == 'a':
        add_skill()
    elif user_input == 'd':
        delete_skill()
    elif user_input == 'u':
        update_skill_progress()
    else:
        print("APP Is Closed")

else:
    print(f"sorry this \"{user_input}\" command is not found")