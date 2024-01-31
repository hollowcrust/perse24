ans = 0
for i in range(12):
  s = input()
  if(abs(int(s[0]) - int(s[-1])) == 1):
    ans += 1

print(ans)
