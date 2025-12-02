#1
text='PythonProgramming'
print(text[6:])
#2
s='Hello, Python, Hello, World'
print(s.count('Hello'))
#3
word='Development'
print(word[::-1])
#4
sentence='Python is awsome'
if 'Python'in sentence:
    print(sentence.replace("awsome",'powerful'))
#5
text='aaabbbcccaaa'
print(text.count('aaa'))
#6
email='username@example.com'
e=email.split('@')
print("Username: "+e[0]+", domain: "+e[1])
#7
line='The price is 1500 rupees'
for char in line:
    if char.isdigit():
        print(char,end="")
print()
#8
words='python-is-simple-and-powerful'
w=words.split('-')
print(" ".join(w))
#9
text1='Hello123World45Python'
for i in text1:
    if i.isdigit():
        continue
    print(i,end="")
print()
#10
text3 = 'Mississippi'
seen = set()
for ch in text3:
    if ch in seen:
        print(ch)
        break
    seen.add(ch)
