#Sum of bit differences among all pairs

l = {1,2}
max = max(l)
max_bits = len(bin(max)[2:])
count = 0
for i in range(1, max_bits+1):
    numsetbits = 0
    for num in l:
        if bin(num)[-i] == '1':
            numsetbits += 1
    count += numsetbits*(len(l)-numsetbits)

print(count*2)