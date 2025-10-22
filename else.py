for x in range(6):
  print(x)
else:
  print("Siempre se escribe esto")

for x in range(6):
  print(x)
  if x == 3:
    break
else:
  print("Esto no sale porque no ha terminado el for normalmente")


i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("Siempre se escribe esto")


i = 1
while i < 6:
  print(i)
  i += 1
  if i==3:
    break
else:
  print("Nunca se escribe")