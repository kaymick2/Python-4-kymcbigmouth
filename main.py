outF = open("myOutFile.txt", "w")
print(round(4))
print(round(4.567, 1))
print(round(4.755, 2))
print(round(10 / 3, 2))
print(round(1000 / 3, -1))
print(int(4))
print(int(4.567))
print(int(4.755))
#part 2!!!!!!!
print('part 2!')
print(round(int(4)))
print(round(int(4.567)))
print(round(int(4.755), 2))
print(int(round(4.567, 1)))
print(int(round(4.6, 0)))
print(int(round(4.6, 1)))
#part 3
print('part 3')
print(7**(0.33))
print(7**(1 / 3))
#part 4
print("part 4. type cConversion(number) to start")


#celsius conversion
def cConversion(urMom):
  celsius = (urMom - 32) * 5/9
  celsius = round(celsius, 2)
  print("your result is ", celsius)
