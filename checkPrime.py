import math
n = int(input())
print('updated1 version3')
f=0
for i in range(2,int(math.sqrt(n))):

  if n%i == 0:
    f=1
    print('its not a prime')
    break
if f==0:
  print('its prime number')


