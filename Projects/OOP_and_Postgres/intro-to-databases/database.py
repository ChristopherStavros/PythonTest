from psycopg2 import pool
connection_pool = pool.SimpleConnectionPool(1, 10,  #maxconn...number of initial connections, max number of connections pool can handle
                                            host = "localhost", 
                                            database="learning", 
                                            user = "postgres", 
                                            password = "P@ssw0rd") 
                                           