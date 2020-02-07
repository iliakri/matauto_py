import psycopg2
from allure import step
from model.worker import Worker


class DbFixture:

    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)

    def get_workers(self):
        list_workers = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, clock_num from worker")
            for row in cursor:
                (id, name, clock_num) = row
                list_workers.append(Worker(id=str(id), name=name, clock_num=clock_num))
        finally:
            cursor.close()
        return list_workers

    @step('DB connection close')
    def destroy(self):
        self.connection.close()

    def get_workers_id_by_workshop(self, workshop_id):
        workers_id = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select worker_id from workshop_worker where workshop_id = {workshop_id}")
            for row in cursor:
                worker_id = row[0]
                workers_id.append(worker_id)
                # list.append(Worker(worker_id=worker_id))
        finally:
            cursor.close()
        return workers_id

    def get_production_id_by_transporter(self, transporter_id):
        productions = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select production_id from transporter_production where transporter_id={transporter_id}")
            for row in cursor:
                production_id = row[0]
                productions.append(production_id)
        finally:
            cursor.close()
        return productions

    def get_id_from_db(self, object):
        list_id = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select id from public.{object}")
            for row in cursor:
                transporter_id = row[0]
                list_id.append(transporter_id)
        finally:
            cursor.close()
        list_id.sort()
        return list_id
