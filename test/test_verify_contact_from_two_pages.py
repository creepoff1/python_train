from model.member import Member
from random import randrange
import re


def test_verify_contact_from_two_pages(app, db):
    app.open_home_page()
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="Kate", lastname="Smith", address="12 Main str", home="123456789", mobile="123456788", work="12346777",
                               phone2="123-456-789", email="kate1@gmail.com", email2="kate2@gmail.com", email3="kate3@gmail.com"))
    index = randrange(len(app.member.get_member_list()))
    member_from_home_page = app.member.get_member_list()[index]
    member_from_edit_page = app.member.get_member_info_from_edit_page(index)
    assert member_from_home_page.lastname == member_from_edit_page.lastname.strip()
    assert member_from_home_page.firstname == member_from_edit_page.firstname.strip()
    assert member_from_home_page.address == member_from_edit_page.address.strip()
    assert member_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(member_from_edit_page)
    assert member_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(member_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                           [member.home, member.mobile, member.work, member.phone2]))))


def merge_emails_like_on_home_page(member):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                           [member.email, member.email2, member.email3]))))