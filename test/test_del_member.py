from model.member import Member
from random import randrange

def test_delete_some_member(app):
    if app.member.count_member() == 0:
        app.member.create(Member(firstname="test"))
    old_members = app.member.get_member_list()
    index = randrange(len(old_members))
    app.member.delete_member_by_index(index)
    assert len(old_members) - 1 == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members[index:index+1] = []
    assert old_members == new_members


