# -*- coding: utf-8 -*-
from model.member import Member


def test_add_member(app):
    app.member.create(Member(firstname="Oleg", lastname="Bulygin", phone="89315969795"))


def test_add_empty_member(app):
    app.member.create(Member(firstname="", lastname="", phone=""))