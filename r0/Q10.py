s = "YOu CAN SEE How / tHis caN WoRk OuT / nOW at A look / sEe THE usE Of Key / bELOW"
ans = ""
for c in w:
    if c.isupper():
        ans += "-"
    elif c.islower():
        ans += "."
    else:
        ans += c
#print(ans)
print('GOOD LUCK WITH ROUND 1')
