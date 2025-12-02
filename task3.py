#1
for i in range(1,11):
    print(i,end=" ")
print()

#2
for i in range(2,21,2):
    print(i,end=" ")
print()

#3
s='Python'
for i in s:
    print(i)
print()

#4
i=5
while i>=1:
    print(i,end=" ")
    i-=1
print()

#5
sum=0
for i in range(1,51):
    sum+=i
print(sum)

#6
mul=1
for i in range(1,11):
    mul=i*5
    print("5*",i,"=",mul)
print()

#7
s="Programming"
a=['a','e','i','o','u','A','E','I','O','U']
count=0
for i in a:
    if i in s:
        count+=1
print(count)

#8
str='PythonLoops'
rev=""
for i in str:
    rev=i+rev
print(rev)

#9
for i in range(1,11):
    if i==5:
        continue
    print(i)

#10
for i in range(1,21):
    if i==13:
        break
    print(i)

#11
p=2
if p%2==0:
    print("prime")
else:
    print("not prime")
print()

#12
text = 'Mississippi'
for i in set(text):
    print(i, text.count(i))
print()

#13
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()


#14
num="5847361"
large=0
for i in num:
    if int(i)>large:
        large=int(i)
print(large)

#15
i=5
while i>=1:
    print(i*"*",end="")
    i-=1
    print()

