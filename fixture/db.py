import psycopg2
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
            cursor.execute("select id, name from worker")
            for row in cursor:
                (id, name) = row
                list.append(Worker(id=id, name=name))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

    def get_worker_id(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select worker_id from workshop_worker where workshop_id = 1")
            for row in cursor:
                worker_id = row[0]
                list.append(worker_id)
                #list.append(Worker(worker_id=worker_id))
        finally:
            cursor.close()
        return list

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