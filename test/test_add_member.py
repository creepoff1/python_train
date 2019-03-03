# -*- coding: utf-8 -*-
from model.member import Member


def test_add_member(app):
    old_members = app.member.get_member_list()
    member = Member(firstname="Oleg", lastname="Bulygin", phone="89315969795")
    app.member.create(member)
    new_members = app.member.get_member_list()
    assert len(old_members) + 1 == len(new_members)
    old_members.append(member)
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)


def test_add_empty_member(app):
    old_members = app.member.get_member_list()
    member = Member(firstname="", lastname="", phone="")
    app.member.create(member)
    new_members = app.member.get_member_list()
    assert len(old_members) + 1 == len(new_members)
    old_members.append(member)
    assert sorted(old_members, key=Member.id_or_max) == sorted(new_members, key=Member.id_or_max)