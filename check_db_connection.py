import pymysql.cursors
# from fixture.db import DbFixture
from fixture.orm import ORMfixture
from model.group import Group

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")
# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    l = db.get_list_of_groups_with_contacts()
    for item in l:
        print(item)
    print(len((l)))
finally:
    pass # db.destroy()


