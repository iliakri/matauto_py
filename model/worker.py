
class Worker:

    def __init__(self, id=None, name=None, clock_num=None, workshop_id=None, worker_id=None):
        self.id = id
        self.name = name
        self.clock_num = clock_num
        self.workshop_id = workshop_id
        self.worker_id = worker_id

    def __repr__(self):
        return "%s" % self.worker_id
