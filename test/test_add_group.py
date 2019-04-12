from model.group import Group
import pytest



def test_add_group_db(app, db, check_ui, json_groups):
        group = json_groups
        with pytest.allure.step('Given a group list'):
                old_groups = db.get_group_list()
        with pytest.allure.step('When I add the group %s to the list' % group):
                app.group.create(group)
        with pytest.allure.step('Then the new group list is equal to the old list with added group'):
                new_groups = db.get_group_list()
                old_groups.append(group)
                assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
                if check_ui:
                        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
