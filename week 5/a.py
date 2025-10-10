import re

# s = "Hello World"

# s = "Some text here asdkfla;ksdjf;al dfl kajdf; ajksd;fkljad ;flk"

# # d = 

# number = "+77767770717"
# number_2 = "87767770717123"

# print(re.match(r"\+[0-9]{11}$", number))
# print(re.match(r"8[0-9]{10}$", number_2))


# # print(len(re.findall("a", s)))



r = open("a.txt", "r")
s = r.read()

i = re.search("ИТОГО:", s).end()
i += 1
total = ""
while s[i] != '\n':
    total = total + s[i]
    i += 1
print(total)
i = re.search("Время: ", s).end()
date = ""
while s[i] != '\n':
    date = date + s[i]
    i += 1
print(date)