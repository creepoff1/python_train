from model.member import Member
from random import randrange

def test_mod_some_member(app):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test", lastname="test", phone="88888888888", phone2='77777777', mobile='566666', work='555555'))
    old_members = app.member.get_member_list()
    index = randrange(len(old_members))
    member = Member(firstname='Gleb', lastname='Voinov', phone='89005006040', phone2='777777777', mobile='55556666', work='555555')
    member.id = old_members[index].id
    app.member.mod_member_by_index(index, member)
    assert len(old_members) == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members[index] = member
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)
