# a = 5
# b = 10
# c = 15

# l = [5, 10, 15]
# # l = [1, 2, 3]

# print(l)

# l = ["abc", 123, 5.6, a]
# print(l)

# 1...100
# print(2)
# print(4)
# # ...
# print(10)
x = 1
0
# x % 40 == 0
# while x <= 20:
#     if x % 2 == 0:
#         print(x)
#     if x % 10 == 0:
#         break
#     x += 1
# (0, 1, 2, ...100)
# for i in range(0, 10, 2):
    # print(i)

t = (1, 2, 3, "acb")
l = [1, 2, 3, "acb"]
# print(l, t)
l.append("str")
# print(l)
l += t
# t += l
# print(t)
# print(l)
# t.append("str")
# print(t)
# print(l)
s = set(l)
# s[i]
# print(s)
# for i in l:
    # print(f"My list has object {i}")
# for i in range(len(l)):
    # print(f"My list has object {l[i]}")
# for i in s:
    # print(i)
# a = [1, 2, 3, 4, 5]

# for i in range(len(a)):
    # if i % 2 == 0:
        # print(a[i])
# for i in range(0, len(a), 2):
    # print(a[i])

# a = [1, -2, 3, -4, 5]
# cnt = 0
# for i in range(1, len(a) - 1):
    # if a[i] > a[i - 1] and a[i] > a[i + 1]:
        # cnt += 1

# a = [1, 2, 3, 1, 1, 3, 2]
# l = set(a)
# print(len(l))
# n = len(a)
# for i in range(n):
    # print(a[n - i - 1])
# print(cnt)

# a = [1, 2, 3, 2, 3, 4]
# s = set()
# for i in a:
#     if i in s:
#         print("yes")
#     else:
#         print("no")
#     s.add(i)

# d = {
#     "lesson": "PP2",
#     "time": "8:00"
# }
# d = {
#     "apple": "alma",
#     "milk": "sut",
#     "water": "su",
#     "home": "ui"
# }

# while True:
#     x = input()
#     if d.get(x):
#         print(d.get(x))
#     else:
#         eng = input("perevod zhok, perevod kossiniz:")
#         kaz = input("Audarmasi:")
#         d[eng] = kaz

d = [
    {
        "lesson": "PP2",
        "time": "8:00",
        "students": 30,
        "year": 2025
    },
    {
        "lesson": "IPC",
        "time": "10:00",
        "students": 20,
        "year": 2025
    },
    
]
# print(d)
for item in d:
    print(f"Information about lesson {item['lesson']}")
    for key, value in item.items():
        if key == "lesson":
            continue
        print(f"{key}: {value}")
    print()