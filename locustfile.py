from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet):

    @task(6)
    def sender_productions(l):
        data = {"unixtime": 0, "summ_out": 666666}
        l.client.post("/sender/workshops/transporters/1/zones/5/productions", json=data)

    @task(4)
    def sender_hats(l):
        data = [{"zone_sub_id": 6, "hat_id": 30, "transporter_id": 1}]
        l.client.post("/sender/workshops/1/hats", json=data)

    @task(2)
    def zones_status(l):
        l.client.get("/transporters/1/zones/status")

    @task(2)
    def get_cameras_by_transporter(l):
        l.client.get("/transporters/4/cameras")

    @task(1)
    def get_hats(l):
        l.client.get("/workshops/1/hats")

    @task(1)
    def get_list_workers(l):
        l.client.get("/workshops/1/workers/pages?direction=ASC&field=id&page=1&per_page=10")

    @task(1)
    def get_list_report(l):
        l.client.get("/transporters/1/workers/status?start_date=2019-12-14")

    @task(1)
    def get_workshops(l):
        l.client.get('/workshops')

    @task(1)
    def get_workshop_by_id(l):
        l.client.get('/workshops/1')

    @task(1)
    def get_normative(l):
        l.client.get('/transporters/1/normative')

    @task(1)
    def get_shift_by_transporter(l):
        payload = {'start_date': '2019-10-25'}
        l.client.get('/transporters/1/shifts/workers', params=payload)

    @task(1)
    def get_shift_by_id(l):
        l.client.get('/shifts/110')

    @task(1)
    def get_zones_by_transporter(l):
        l.client.get('/transporters/1/zones')

    @task(1)
    def get_productions_by_transporter(l):
        l.client.get('/transporters/1/productions')

    @task(1)
    def get_transporters_by_workshop(l):
        l.client.get('/workshops/1/transporters')

    @task(1)
    def get_transporters_by_id(l):
        l.client.get('/transporters/1')

    @task(1)
    def get_workers_by_workshop(l):
        l.client.get('/workshops/1/workers')

    @task(1)
    def get_workers_status(l):
        l.client.get('/transporters/1/workers/status')

    @task(1)
    def get_worker_by_workshop(l):
        l.client.get('/workshops/1/workers/74')


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 2)



