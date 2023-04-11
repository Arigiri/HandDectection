import random
data = [chr(i) for i  in range(ord('A'), ord('Z') + 1)]
arr = [[0 for j in range(26) ] for i in range(26)]

x = "REVICE"
y = "AOBING"
key = "XETENO"
for row in range(len(arr)):
    for col in range(len(arr)):
        arr[row][col] = random.choice(data)

keyidx = 0

for idx in range(len(x)):
    if keyidx >= len(key):
        break
    row = x[idx]
    col = y[idx]

    row = ord(row) - ord('A')
    col = ord(col) - ord('A')
    arr[row][col] = key[keyidx]
    keyidx += 1
    if keyidx >= len(key):
        break


f = open('output.txt', 'w')
for row in arr:
    for ele in row:
        f.write(str(ele) + ' ')
    f.write('\n')
