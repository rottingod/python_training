# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest
from model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    contact = Contact(name="Elena", middle_name="Igorevna", last_name="Plotnikova", nickname="rottingod",
                      company="python_training", address="Moscow",
                      home="89991234567", mobile="89991234567", email="rottingod@gmail.com")
    app.session.login(username="admin", password="secret")
    app.create_new_contact(contact)
    app.session.logout()

