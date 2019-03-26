import re
from random import randrange
from model.member import Member


def test_assert_all_members_from_home_page_with_db(app, db):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="First name", lastname="Last name",
                                   address="Address",
                                   home="+375 1721111 11",
                                   mobile="+3752(91111112)", work="+3751721-111-13", phone2="+375172111114",
                                   email="test1@test.com", email2="test2@test.com",
                                   email3="test3@test.com"
                                   ))
        members_quantity = app.member.count_member()
    else:
        pass
    members_from_home_page = app.member.get_member_list()
    members_from_db = db.get_member_list_as_at_ui()
    assert sorted(members_from_db, key=Member.id_or_max) == sorted(members_from_home_page, key=Member.id_or_max)

