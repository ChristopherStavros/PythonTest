from psycopg2 import pool
                                           
class ConnectionPool:
    def __init__(self):
        connection_pool = pool.SimpleConnectionPool(1, 1,  #maxconn...number of initial connections, max number of connections pool can handle
                                            host = "localhost", 
                                            database="learning", 
                                            user = "postgres", 
                                            password = "P@ssw0rd")
    def __enter__(self):
        return self.connection_pool.getconn()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # We really should be returning the connections, but how?
        pass
