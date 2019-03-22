# -*- coding: utf-8 -*-
from model.member import Member



def test_add_member(app, json_members, check_ui, db):
    member = json_members
    old_members = db.get_member_list()
    app.member.create(member)
    assert len(old_members) + 1 == app.member.count_member()
    new_members = db.get_member_list()
    old_members.append(member)
    assert old_members == new_members
    if check_ui:
        contact_list = db.get_member_list_with_merged_emails_and_phones()
        assert sorted(contact_list, key=Member.id_or_max) == sorted(app.member.get_member_list(), key=Member.id_or_max)

