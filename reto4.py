n, k = input().split()
n = int(n)
k = int(k)
memory = 0
exams = input().split()
exams = list(map(int,exams))
equality=0
for i in range(len(exams)):
    if i == 0:pass
    if exams[i] == exams[i-1]:equality+=1
equal = 0
for i in range(len(exams)-1):
    for x in range(i,len(exams)-1):
        if exams[i] == exams[x+1]:equal += 1; break
if equality == n: memory = equal
else:
    for i in range(len(exams)):
        if i < k: continue
        for x in range(1,k+1):
            if exams[i] == exams[i-x]:memory += 1
print(equal,memory)