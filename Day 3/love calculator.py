print("Welcome")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()

t = lower_case_name1.count("t")
t += lower_case_name2.count("t")
print(f"T appears {t} times")

r = lower_case_name1.count("r")
r += lower_case_name2.count("r")
print(f"R appears {r} times")

u = lower_case_name1.count("u")
u += lower_case_name2.count("u")
print(f"U appears {u} times")

e = lower_case_name1.count("e")
e += lower_case_name2.count("e")
print(f"E appears {e} times")

true_total = t+r+u+e
print(f"Total = {true_total} \n")

l = lower_case_name1.count("l")
l += lower_case_name2.count("l")
print(f"L appears {l} times")

o = lower_case_name1.count("o")
o += lower_case_name2.count("o")
print(f"O appears {l} times")

v = lower_case_name1.count("v")
v += lower_case_name2.count("v")
print(f"V appears {v} times")

e2 = lower_case_name1.count("e")
e2 += lower_case_name2.count("e")
print(f"E appears {e2} times")

love_total = l+o+v+e2
print(f"Total = {love_total}")

love_score = str(true_total) + str(love_total)

print(love_score)