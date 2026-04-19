#💻 Problem 6 — Check Rotation

s1 = "abcde"
s2 = "cdeab"
seen=""

#o/p Yes

#Try all rotations manually

if len(s1)==len(s2):

    for i in range(len(s1)):
        for j in range (len(s2)):
            if s1[i]==s2[j]:
                seen+=s2[j]
    if s1==seen:
         print("Yes")
else:
    print("No")
    

        

        