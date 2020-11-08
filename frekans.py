c ="Honest Thief, aşık olduğu ve artık dürüst" \
   " bir hayat yaşamak istediği için teslim olmaya" \
   " çalışan bir banka soyguncusuna (Liam Neeson)" \
   " odaklanıyor. Yedi milyon dolarlık ganimetini" \
   " sakladığı depolama tesisinde çalışan bir kadına" \
   " (Kate Walsh) aşık olan soyguncu, teslim olmaya" \
   " çalıştığı polislerin kendisinden daha yozlaşmış" \
   " olduğunu fark eder. Soyguncunun adını temize" \
   " çıkarmak için mücadele etmesi gerekecektir."

frekans=dict()

for i in c:
    if (i in frekans):
        frekans[i] += 1
    else:
        frekans[i] = 1

for i,j in frekans.items():
    print(i,":",j)