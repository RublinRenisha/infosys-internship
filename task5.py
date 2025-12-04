#1
import math
print(math.sqrt(4))

#2
print(math.floor(5.67))
print(math.ceil(5.67))

#3
import random
num = random.randint(1, 100)
print(num)

#4
for _ in range(5):
    print(random.randint(10, 20))

#5
import datetime
today = datetime.date.today()
print(today)

#6
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

#7
import os
print(os.getcwd())

#8
files = os.listdir()
print(files)

#9
import sys
print(sys.version)

#10
import json
json_str = '{"name": "Alice", "age": 25, "city": "New York"}'
data = json.loads(json_str)
print(data)

#11
print("cos(0) =", math.cos(0))
print("sin(90°) =", math.sin(math.radians(90)))
print("log(10) =", math.log(10)) 

#12
results = []
for _ in range(10):
    roll = random.randint(1, 6) 
    results.append(roll)
print(results)

#13
bday = datetime.date(2026, 9, 5)   
today = datetime.date.today()
print((bday - today).days)

#14
from datetime import datetime, timedelta
d = datetime.strptime('2022-05-15', '%Y-%m-%d')
d += timedelta(days=30)
print(d)

#15
os.mkdir('backup')

#16
data = {'name': 'Alice', 'age': 25, 'city': 'New York'}
json_str = json.dumps(data)
print(json_str)

#17
import re
text = "Order 123 placed on 2025-12-04 at 10:30 AM."
digits = re.findall(r'\d+', text)
print(digits)

#18
text = "Hello, how are you?"
if re.match(r'^Hello', text):
    print("String starts with 'Hello'")
else:
    print("String does not start with 'Hello'")

#19
import statistics
data = [2, 5, 3, 9, 5, 2, 5, 7]
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode(data))

#20
import time
start = time.time()
for i in range(1, 1000001):
    pass  
end = time.time()
print( end - start)