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

    def get_worker(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, clock_num from worker")
            for row in cursor:
                (id, name, clock_num) = row
                list.append(Worker(id=str(id), name=name, clock_num=clock_num))
        finally:
            cursor.close()
        return list

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

    def get_productions_id(self):
        productions = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from production")
            for row in cursor:
                production_id = row[0]
                productions.append(production_id)
        finally:
            cursor.close()
        return productions

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

    def get_all_transporters_id(self, object):
        transporters = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(f"select id from {object}")
            for row in cursor:
                transporter_id = row[0]
                transporters.append(transporter_id)
        finally:
            cursor.close()
        transporters.sort()
        return transporters

    def get_shifts_id(self):
        shifts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from shift")
            for row in cursor:
                production_id = row[0]
                shifts.append(production_id)
        finally:
            cursor.close()
        return shifts
