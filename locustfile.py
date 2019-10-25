from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):

    @task(6)
    def sender_productions(l):
        data = {"unixtime": 0, "summ_out": 666666}
        l.client.post("/api/v1/sender/workshops/transporters/1/zones/5/productions", json=data)

    @task(4)
    def sender_hats(l):
        data = [{"zone_sub_id": 6, "hat_id": 30, "transporter_id": 1}]
        l.client.post("/api/v1/sender/workshops/1/hats", json=data)

    @task(2)
    def zones_status(l):
        l.client.get("/api/v1/workshops/transporters/1/zones/status")

    @task(2)
    def get_cameras(l):
        l.client.get("/api/v1/workshops/transporters/4/cameras")

    @task(1)
    def get_hats(l):
        l.client.get("/api/v1/workshops/1/hats/")

    @task(1)
    def get_list_workers(l):
        l.client.get("/api/v1/workshops/1/workers/pages?direction=ASC&field=id&page=1&per_page=10")

    @task(1)
    def get_list_report(l):
        l.client.get("/api/v1/workshops/transporters/1/workers/status?start_date=2019-10-14")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 2000
