import pytest
from model.member import Member
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of members", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 3
f = "data/members.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_strings_for_text_fields(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_strings_for_phones(maxlen):
    symbols = string.digits + "(" + ")" + "+" + "-" + " "
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Member(firstname="", lastname="", phone="", phone2="",
                    mobile="", work="", email="",email2="", email3="")] \
    + [Member(firstname=random_strings_for_text_fields("name", 7), lastname=random_strings_for_text_fields("lastname", 7), phone=random_strings_for_phones(20),
              phone2=random_strings_for_phones(10),
              mobile=random_strings_for_phones(15), work=random_strings_for_phones(10), email=random_strings_for_text_fields("email", 12),
              email2=random_strings_for_text_fields("email12", 12), email3=random_strings_for_text_fields("email", 12))
       for i in range(n)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))