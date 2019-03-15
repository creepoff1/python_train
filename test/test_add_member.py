# -*- coding: utf-8 -*-
from model.member import Member



def test_add_member(app, json_members):
    member = json_members
    old_members = app.member.get_member_list()
    app.member.create(member)
    assert len(old_members) + 1 == app.member.count_member()
    new_members = app.member.get_member_list()
    old_members.append(member)
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)

