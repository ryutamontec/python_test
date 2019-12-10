f = open('input.txt','r')
data = f.readlines()

with open('input.txt') as f: #行数を計算
    size = sum(1 for _ in f)

i = [] #整数
s = [] #文字列

i_s = [[],[]]
i_s.clear()
m = data[size-1]

count = 0
for line in data:
    if count == size-1:
        break
    I,S = data[count].split(":")
    i.append(I)
    s.append(S)
    i_s.append([i[count],s[count]])
    count += 1

i_s.sort()
i.sort()

count = 0
num = 0
for line in data:
    if count == size-1:
        break
    if int(m) % int(i[count]) == 0:
        print(i_s[count][1])
        num += 1
    count += 1

if num == 0:
    print(m)

print(num)
