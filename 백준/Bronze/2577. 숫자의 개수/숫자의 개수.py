n1 = int(input())
n2 = int(input())
n3 = int(input())

DIC = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
n = n1*n2*n3
n_str = str(n)

for i in DIC.keys():
    for j in n_str:
        if i == j:
            DIC[i] += 1
        else:
            continue
DIC_VAL = DIC.values()
for r in DIC_VAL:
    print(int(r))