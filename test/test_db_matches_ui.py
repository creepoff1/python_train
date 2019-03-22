from model.group import Group
from model.member import Member
from timeit import timeit
import re

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=re.sub('\s+', ' ', group.name.strip()))
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_group_ui_list_matches_with_group_bd_list(app, db):
    groups_name_from_db = db.get_list_of_groups_names_and_ids()
    assert sorted(groups_name_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_members_ui_list_matches_with_contact_bd_list(app, db):
    contact_list = db.get_member_list_with_merged_emails_and_phones()
    assert sorted(contact_list, key=Member.id_or_max) == sorted(app.member.get_member_list(), key=Member.id_or_max)