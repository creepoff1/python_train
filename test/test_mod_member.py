from model.member import Member

def test_mod_first_member(app):
    app.session.login(username="admin", password="secret")
    app.member.mod_first_member(Member(firstname='Gleb', lastname='Voinov', phone='89005006040'))
    app.session.logout()