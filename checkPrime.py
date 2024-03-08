import math
n = int(input())
print('version2')
f=0
for i in range(2,int(math.sqrt(n))):

  if n%i == 0:
    f=1
    print('its not a prime')
if f==0:
  print('its prime number')


