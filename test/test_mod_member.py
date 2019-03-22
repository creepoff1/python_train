from model.member import Member
from random import randrange
from random import random

def test_mod_some_member(app, db, check_ui):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test", lastname="test", home="88888888888", phone2='77777777', mobile='566666', work='555555',
                                email='g@g.ru',email2='r@f.ru', email3='gg@gg.ru'))
    old_members = db.get_member_list()
    index = randrange(len(old_members))
    member = Member(firstname='Gleb', lastname='Voinov', home='89005006040', phone2='777777777',
                    mobile='55556666', work='555555', email='g@g.ru',email2='r@f.ru', email3='gg@gg.ru')
    member.id = old_members[index].id
    app.member.modify_member_by_id(member.id, member)
    new_members = db.get_member_list()
    assert len(old_members) == len(new_members)
    new_members = db.get_member_list()
    old_members[index] = member
    assert old_members == new_members
    if check_ui:
        contact_list = db.get_member_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Member.id_or_max) == sorted(app.member.get_member_list(), key=Member.id_or_max)
