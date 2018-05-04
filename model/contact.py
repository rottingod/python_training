from sys import maxsize


class Contact:

    def __init__(self, name=None, middle_name=None, last_name=None, nickname=None, company=None, address=None,
                 home=None, mobile=None, email=None, id=None):
        self.name = name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nickname = nickname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name,self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.name == other.name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
