from psycopg2 import pool

class Database:

    # This value belongs to ALL objects of type Database
    connection_pool = None

    # This does NOT get executed automatically as with the __init__ method
    @staticmethod
    def initialise():
        Database.connection_pool = pool.SimpleConnectionPool(1, 10,  #maxconn...number of initial connections, max number of connections pool can handle
                                    host = "localhost", 
                                    database="learning", 
                                    user = "postgres", 
                                    password = "P@ssw0rd")
    ###  SAME
    #  @classmethod
    # def initialise(cls):
    #     cls.connection_pool = pool.SimpleConnectionPool(1, 10,  #maxconn...number of initial connections, max number of connections pool can handle
    #                                 host = "localhost", 
    #                                 database="learning", 
    #                                 user = "postgres", 
    #                                 password = "P@ssw0rd")


class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None
 
    def __enter__(self):
        self.connection = connection_pool.getconn()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        connection_pool.putconn(self.connection)
