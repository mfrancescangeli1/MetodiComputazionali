week=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato","domenico"]
ottobre=week[1:]+3*week+week[:4]
print(week)
print(ottobre)
ottobre2024={i :ottobre[i-1] for i in range(1,32) }
for i in ottobre2024:
     if ottobre2024[i]!="domenico":
         print("  {:}  {:} ".format(i, ottobre2024[i]))
     else:
         print(i, "  ", ottobre2024[i])
