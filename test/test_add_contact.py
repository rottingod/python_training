# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", middlename="Igorevna", lastname="Plotnikova", nickname="rottingod",
                      company="python_training", address="Moscow",
                      homephone="89991234567", mobilephone="89991234567", workphone="12345",
                      secondaryphone="12345678", email="rottingod@gmail.com")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


