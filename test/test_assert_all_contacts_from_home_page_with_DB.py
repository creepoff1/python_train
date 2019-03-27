import re
from model.member import Member


def test_assert_all_members_from_home_page_with_db (app, db):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="First name", lastname="Last name", address="Address", home="+375 1721111 11",
                                   mobile="+3752(91111112)", work="+3751721-111-13", phone2="+375172111114", email="test1@test.com", email2="test2@test.com",
                                   email3="test3@test.com"))
    else:
        pass
    members_from_home_page = app.member.get_member_list()
    members_from_db = db.get_member_list_as_at_ui()
    assert sorted(members_from_db, key=Member.id_or_max) == sorted(members_from_home_page, key = Member.id_or_max)
    assert len(members_from_home_page) == len(members_from_db)

    members_from_home_page_sorted = sorted(members_from_home_page, key = Member.id_or_max)
    members_from_db_sorted = sorted(members_from_db, key=Member.id_or_max)
    for x in range(len(members_from_home_page_sorted)):
        assert members_from_home_page_sorted[x].lastname == members_from_db_sorted[x].lastname.strip()
        assert members_from_home_page_sorted[x].firstname == members_from_db_sorted[x].firstname.strip()
        assert members_from_home_page_sorted[x].address == members_from_db_sorted[x].address.strip()
        assert merge_emails_like_on_home_page(members_from_home_page_sorted[x]) == merge_emails_like_on_home_page(members_from_db_sorted[x])
        assert merge_phones_like_on_home_page(members_from_home_page_sorted[x]) == merge_phones_like_on_home_page(members_from_db_sorted[x])





def clear(s):
    return re.sub('[()\n -]', "", s)

def merge_phones_like_on_home_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [member.all_phones_from_home_page]))))

def merge_emails_like_on_home_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [member.all_emails_from_home_page]))))