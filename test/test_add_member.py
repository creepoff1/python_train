# -*- coding: utf-8 -*-
from model.member import Member
import pytest
import random
import string



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
       for name in range(5)]


@pytest.mark.parametrize("member", testdata, ids=[repr(x) for x in testdata])
def test_add_member(app, member):
    old_members = app.member.get_member_list()
    app.member.create(member)
    assert len(old_members) + 1 == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members.append(member)
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)