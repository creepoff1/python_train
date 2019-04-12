# -*- coding: utf-8 -*-
from model.contact import Info
import random
import string
import os.path
import jsonpickle
import getopt
import sys



try:
        opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
        getopt.usage()
        sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + "  " *10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Info(firstname="", middlename="", lastname="")] + [
        Info(firstname=random_string("FN", 10), middlename=random_string("MN", 10), lastname=random_string("LN", 10),
             address=random_string("ADDRESS", 10), homedid=random_string("HOME", 10))
        for i in range(n)
]


# testdata = [
#         Info(firstname=firstname, middlename=middlename, lastname=lastname)
#         for firstname in ["", random_string("FN", 10)]
#         for middlename in ["", random_string("MN", 20)]
#         for lastname in ["", random_string("LN", 20)]
# ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
