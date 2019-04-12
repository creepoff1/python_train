from sys import maxsize

class Group:

    def __init__(self, groupname=None, header=None, footer=None, id=None):
        self.groupname = groupname
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.groupname, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.groupname == other.groupname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize