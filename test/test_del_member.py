from model.member import Member
from random import randrange
import random

def test_delete_some_member(app, db, check_ui):
    if len(db.get_member_list()) == 0:
        app.member.create(Member(firstname="test", lastname="test", home="88888888888", phone2='77777777', mobile='566666', work='555555',
                                email='g@g.ru',email2='r@f.ru', email3='gg@gg.ru'))
    old_members = db.get_member_list()
    member = random.choice(old_members)
    app.member.delete_member_by_id(member.id)
    new_members = db.get_member_list()
    assert len(old_members) -1 == len(new_members)
    old_members.remove(member)
    assert old_members == new_members
    if check_ui:
        contact_list = db.get_member_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Member.id_or_max) == sorted(app.member.get_member_list(), key=Member.id_or_max)


