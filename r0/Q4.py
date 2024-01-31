s1 = input()
s2 = input()
s3 = input()
check2, check3 = False, False
if(s2 != s1):
  check2 = True
if(s3 != s1):
  check3 = True

if(check2 and check3):
  print("BOTH MISMATCH")
elif(check2):
  print("ENTRY 2 MISMATCH")
elif(check3):
  print("ENTRY 3 MISMATCH")
else:
  print("OK")
