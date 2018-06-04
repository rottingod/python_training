from model.group import Group
from model.contact import Contact
import pymysql.cursors


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host,
                                          database=name,
                                          user=user,
                                          password=password,
                                          cursorclass=pymysql.cursors.DictCursor)
        self.connection.autocommit(True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                id = row['group_id']
                name = row['group_name']
                header = row['group_header']
                footer = row['group_footer']
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                select 
                    id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 
                from addressbook where deprecated='0000-00-00 00:00:00'
                """)
            for row in cursor:
                id = row['id']
                firstname = row['firstname']
                lastname = row['lastname']
                address = row['address']
                homephone = row['home']
                mobilephone = row['mobile']
                workphone = row['work']
                secondaryphone = row['phone2']
                email = row['email']
                email2 = row['email2']
                email3 = row['email3']
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                                    mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email=email,
                                    email2=email2, email3=email3))
        finally:
            cursor.close()
        return list
