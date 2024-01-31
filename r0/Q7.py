x = int(input())
total = 5 * ((x//5 + 1) * (x//5))//2
if(x % 5):
  total += x
print(total)
