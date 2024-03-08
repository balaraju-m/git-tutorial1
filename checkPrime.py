n = int(input())
print('version1')
f=0
for i in range(2,n):

  if n%i == 0:
    f=1
    print('its not a prime')
if f==0:
  print('its prime number')


