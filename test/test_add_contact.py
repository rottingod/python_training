# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    print(old_contacts)
    contact = Contact(name="Elena", middle_name="Igorevna", last_name="Plotnikova", nickname="rottingod",
                      company="python_training", address="Moscow",
                      home="89991234567", mobile="89991234567", email="rottingod@gmail.com")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    print(new_contacts)
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


