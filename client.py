from xmlrpc import client
import time
from math import factorial
num_list = [15,33,23,12,9]
fact = []
client = client.ServerProxy("http://localhost:8000")

start_time = time.time()
f = client.computefactorial(num_list)
end_time  = time.time() - start_time
print(f, "computed in", end_time, "seconds using Remote Procedure Call")


def fact(num_list):
    return [factorial(num) for num in num_list]

start_time1 = time.time()
fact(num_list)
end_time = time.time() - start_time1

print(fact(num_list), "computed in", end_time,"seconds using Simple Procedure Call")
