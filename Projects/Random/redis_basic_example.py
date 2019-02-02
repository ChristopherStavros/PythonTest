'''pip3 install redis'''

import redis

server = {
"host" : "localhost",
"port" : 32768,   # 6379
"password" : "",
"decode_responses" : True
}

try:
    r = redis.StrictRedis(**server)
except:
    exit()

dict_data = {'name' : 'Steez'}


def set_value(key, value):
    try:
        r.set(key, value)       
   
    except Exception as e:
        print(e)

def get_value(key):
    try:        
        msg = r.get(key)
        print(msg)       
   
    except Exception as e:
        print(e)

def set_dict(key, value):
    try:
        try:
            r.delete(key)
        except:
            print("keynotfound")
        r.hmset(key, value)       
   
    except Exception as e:
        print(e)

def get_dict(key):
    try:
        msg = r.hgetall(key)
        print(msg)       
   
    except Exception as e:
        print(e)
        
# redis_host = "localhost"
# redis_port = 32768   # 6379
# redis_password = ""


# def set_value(key, value):
#     try:
#         r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
#         r.set(key, value)       
   
#     except Exception as e:
#         print(e)

# def get_value(key):
#     try:
#         r = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        
#         msg = r.get(key)
#         print(msg)       
   
#     except Exception as e:
#         print(e)



set_value("foo", "Nicolaj")
get_value("foo")
     
set_dict("server",dict_data)
get_dict("server")