#💻 Problem 1 — Remove Consecutive Duplicates

#Compare current with previous character

s = "aaabbccdaa"
result=""

#👉 Output: abcda

if s=="":
    result+=""
else:
    result+=s[1]

    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            continue
        result+=s[i]

print(result)
