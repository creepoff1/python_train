from model.group import Group
from random import randrange
import random


def test_modify_group_name_db(app, db, check_ui):
        if len(db.get_group_list()) == 0:
                app.group.create(Group(groupname="test"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        changed_group = Group(groupname="Group2")
        changed_group.id = group.id
        app.group.modify_group_by_id(group.id, changed_group)
        assert len(old_groups) == app.group.count()
        new_groups = db.get_group_list()
        old_groups.remove(group)
        old_groups.append(changed_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
                assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


