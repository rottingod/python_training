# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    contact = Contact(name="Elena", middle_name="Igorevna", last_name="Plotnikova", nickname="rottingod",
                      company="python_training", address="Moscow",
                      home="89991234567", mobile="89991234567", email="rottingod@gmail.com")
    app.session.login(username="admin", password="secret")
    app.contact.create(contact)
    app.session.logout()
