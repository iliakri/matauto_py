
class Worker:

    def __init__(self, id=None, name=None, clock_num=None):
        self.id = id
        self.name = name
        self.clock_num = clock_num

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.name, self.clock_num)
