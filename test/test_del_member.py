
def test_delete_first_member(app):
    app.session.login(username="admin", password="secret")
    app.member.delete_first_member()
    app.session.logout()