# -*- coding: utf-8 -*-
import pytest
from model.member import Member
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_member(app):
    app.session.login(username="admin", password="secret")
    app.member.create_member(Member(firstname="Oleg", lastname="Bulygin", phone="89315969795"))
    app.session.logout()

def test_add_empty_member(app):
    app.session.login(username="admin", password="secret")
    app.member.create_member(Member(firstname="", lastname="", phone=""))
    app.session.logout()

