Deg, Dis = map(int, input().split())
 
WS = (Dis + 3) // 6
W = sum(WS >= x for x in [3, 16, 34, 55, 80, 108, 139, 172, 208, 245, 285, 327])
Dir = [
  "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", "S",
  "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW", "N"][(Deg-113)//225] if W else "C"
 
print(Dir, W)
