from model.group import Group

def test_mod_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.mod_first_group(Group(name="ee", header="st", footer="est"))