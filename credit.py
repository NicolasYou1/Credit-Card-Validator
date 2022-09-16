def getSize(d):
  length = len(d)
  gol = 3
  gola = 1
  if length == 13:
    return gol
  if length == 14:
    return gol
  if length == 15:
    return gol
  if length == 16:
    return gol
  else:
    return gola

def getEnterprise(number):
  index = 0
  Ent = 'Invalid' 
  if (number[index]) == '4':
    Ent = 'Visa'
  if (number[index]) == '5':
    Ent = 'Master Card'
  if (number[index]) == '6':
    Ent = 'Discover'
  if int(number[index]) == '3':
    index = 1
    if (number[index]) == '7':
      Ent = 'American Express'      
  return Ent

#if the lenght of the numbers is even, you would take the "odds" as evens, because it's counting the evens and odds backwards.

def sumOfDoubleEvenPlace(number):
  num = number
  sumeven = []
  index = 0
  while index % 2 == 0:
    sumeven.append(int(num[index]))
    index = index + 1
    return sumeven
#In these lines you take the numbers to sum
def sumOfOddPlace(number):
  num = number
  sumeven = []
  index = 0
  while index % 2 == 0:
    if int(num[index]) > 4:
      evend = 0
      for i in str(num): 
        evend += int(i)
        sumeven.append(int(evend))
    else:
      sumeven.append(int(num[index]))
      index = index + 1
      return sumeven
#Here you sum them
def isValid(number):
  sumeven = (sumOfDoubleEvenPlace(number))
  sumodd = (sumOfOddPlace(number))
  sumevenn = sum(sumeven)
  sumEven = int(sumevenn) 
  sumOdd = sum(sumodd)
  SUM = int(sumEven) + int(sumOdd)
  if SUM % 10 == 0:
    iv = 'valid'
    return iv
  else:
    iv = sumOdd
    return iv

#  sumoddd = sum(sumodd)
#  sumOdd = int(sumoddd) * 2 
#  sumEven = sum(sumeven)