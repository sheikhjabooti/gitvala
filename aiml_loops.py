
import string

def alpha(number):
    return chr(number + ord('A') - 1)

n = 11
print('ABCDEFEDCBA')
for i in range(1, (n // 2) ):
    l = ''.join(alpha(j) for j in range(1, 7 - i))
    print((l + ' ' * (n - 2 * len(l)) + l[::-1]))

for i in range((n // 2), 0, -1):
    l = ''.join(alpha(j) for j in range(1, 7 - i))
    print(l + ' ' * (n - 2 * len(l)) + l[::-1])
print('ABCDEFEDCBA')

n=9
i=0
while i<5:
    print(" "*i + "*"*n)
    n-=2
    i+=1
j=4
n+=2
while j>0:
  n+=2
  print(" "*(j-1) + "*"*n)
  j-=1
