def solve(a ,b, c): 
  if a+b < c and 4*a*b < (c-(a+b))**2:
    return "Yes"
  else:
    return "No"
    
 print(*map(int, input().split()))
