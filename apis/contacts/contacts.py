################################################################
# Casey Collins, Adam Gwilliam, Zach Arnold
# contacts.py
# Keep track of the user's contacts (name, phone, email)
################################################################

import sqlite3
from sys import argv
import sys

db_siri = sqlite3.connect('apis/contacts/siri.db')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

db_siri.row_factory = dict_factory
db = db_siri.cursor()

def returnContact(row):
    entry = db.execute("SELECT * from contacts where name = '%s'" % name)
    entry = entry.fetchone()

    if entry == None:
        print "Sorry but no contact with that name could be found."
        print "Would you like to add them to your contacts?",
        response = raw_input()
        if response.lower() == "yes":
            addContact("")
        sys.exit()
    else:
        return entry
    
def addContact(name):
    # Store a contact in a sqlite table for later use
    if name == "":
        print "Please enter contact name: ",
        name = raw_input()

    print "Please enter contact phone number: ",
    number = raw_input()

    print "Please enter contact email: ",
    email = raw_input()

    db.execute("INSERT INTO contacts VALUES ( '%s', '%s', '%s')" % (name, number, email))
    
    db_siri.commit()
    print "I have added " + name + " to your contacts!"

def call(contact):
    entry = returnContact(contact)
    
    print "Calling " + entry["name"] + " at " + entry["number"] + "..."
    print "If I was a phone I would place a call for you. Sadly, I am not"

def text(contact):
    entry = returnContact(contact)
    
    print "Texting " + entry["name"] + " at " + entry["number"] + "..."
    print "Check your phone. If you received a text from me, that would be crazy. I didn't send it."

def email(contact):
    entry = returnContact(contact)
    
    print "Emailing " + entry["name"] + " at " + entry["email"] + "..."
    print "Unfortunately email is coming in version 2.0"

def view(contact):
    entry = returnContact(contact)
    
    if entry == None:
        print "Sorry I couldn't find anyone by that name"
    
    else:
        print "Here is the contact info you requested for: " + entry["name"]
        print "The number for this contact is " + entry["number"]
        print "Their email is " + entry["email"]
    



command = argv[1].lower()
if len(argv) > 2:
    name = (" ".join(argv[2:])).title()
else:
    name = ""

if command == "add":
    addContact(name)
elif command == "text":
    text(name)
elif command == "call":
    call(name)
elif command == "view":
    view(name)
elif command == "email":
    email(name)
