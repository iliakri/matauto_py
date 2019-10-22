import requests
import json


class SenderHelper:

    def __init__(self, app):
        self.app = app

    def post_hats(self, workshop_id, zone_sub_id=0, hat_id=0, transporter_id=0):
        data = [{"zone_sub_id": zone_sub_id, "hat_id": hat_id, "transporter_id": transporter_id}]
        return requests.post(self.app.host + f'/sender/workshops/{workshop_id}/hats/', json=data)

    def post_productions(self, transporter_id, zone_sub_id, summ_out, unixtime=0, time_created=None):
        data = {"unixtime": unixtime, "time_created": time_created, "summ_out": summ_out}
        return requests.post(self.app.host +
                             f'/sender/workshops/transporters/{transporter_id}/zones/{zone_sub_id}/productions',
                             json=data)
