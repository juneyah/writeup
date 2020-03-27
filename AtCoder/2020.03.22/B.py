S = input()
H = len(S)//2
 
if S[:H] == S[-H:] == S[-H:][::-1]:
  print("Yes")
else:
  print("No")
