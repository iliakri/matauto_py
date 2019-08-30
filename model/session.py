
class Session:

    def __init__(self, zone_id=None, hat_id=None, worker_id=None, last_detect=None):
        self.zone_id = zone_id
        self.hat_id = hat_id
        self.worker_id = worker_id
        self.last_detect = last_detect

    def __repr__(self):
        return "%s" % self.zone_id
        #return "%s:%s;%s;%s" % (self.zone_id, self.hat_id, self.worker_id, self.last_detect)

