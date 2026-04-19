#💻 Problem 7 — First Repeating Character


s = "abcaed"

#o/p: a

seen=""

for i in s:
    if i in seen:
        print(i)
        break
    seen+=i
