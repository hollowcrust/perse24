from sys import stdin

total = 0
for line in stdin:
  total += int(line)

print(max(0, total - 12))
