# -*- coding: utf-8 -*-
seznam = []
vnos = raw_input("Kaj naj dodam na seznam?")
seznam.append(vnos)
while True:
    nadaljuj = raw_input("Želiš nadaljevati?").lower()
    if nadaljuj == "da":
        vnos = raw_input("Kaj naj dodam na seznam?")
        seznam.append(vnos)
        continue
    elif nadaljuj == "ne":
        break
    else:
        print("Napaka")
        continue

print ("Celoten seznam: ")
for x in seznam:
    print x


