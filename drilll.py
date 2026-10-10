def is_hot(temp) :
   if temp >= 90 :
      return True
   else:
      return False


temps = [72, 95, 101]

for temp in temps:
    print(temp, is_hot(temp))