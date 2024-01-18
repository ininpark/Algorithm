INPUT = input()
UP_INPUT = INPUT.upper()

DIC = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'h':0,
'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,
'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

for i in UP_INPUT:
    if i in DIC.keys():
        DIC[i] += 1 

sorted_dict = sorted(DIC.items(), key= lambda item:item[1], reverse=True)

if sorted_dict[0][1] == sorted_dict[1][1]:
    print('?')
else:
    print(sorted_dict[0][0])