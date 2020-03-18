# mem{0} = neg(1)
-> 

# i = 1
# for x in series:
#   mem{i:} = {x1 x2 ''' 0}
#   add(i len({x1 x2 ''' 0}))
+>> +>> +>> ++>> +>> ++>> +>> +++++>> ++>> ++>> +>> +++++>> +>> ++>> +>> +>++++>> +>> +++++>> +>> +++++>> ++>> ++>> +>> +>+++++>> ++>> ++>> +++++>> ++++>> +>> ++++>> +>> +++++>+>>

# c = read(1)
# while(add(c 1) and sub(c 11)):
#   mul(mem{i} 10)
#   add(mem{i} sub(c 38))
#   c = read(1)
# sub(mem{i} 1)
>,+[-----------[--<[>>++<<-]>>[<<+++++>>-]++++++[<------>-]+<[<+>-]]>[<,+>-]<]<-

# while mem{i}:
#   j = rindex(mem neg(1) from=i)
#   add(mem{j} 1)
#   k = index(mem 0 from=j)
#   sub(mem{k} 1)
#   sub(mem{i} 1)
[<<+[<+]>-[>-]->[->]>-]

# j = rindex(mem neg(1) from=i)
# add(j 1)
# while(mem{j}):
#   add(mem{j} 48)
#   write(mem{j})
#   mem{j} = 0
#   add(j 1)
<+[<+]>-[-<+++++++[>+++++++<-]>.[-]>-]
