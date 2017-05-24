def Main():

    print ("Lets Play Golf")
    userName = str(input("Enter your name:"))
    print("Welcome to golf!")

    print("Choose (I) for instructions, (P) for play or (Q) to quit")

def selection():
     selection =(input)

    while selection == 'I' or "i":
            print ("Instructions: This is a simple golf game in which each hole is 230m game away with par 5. You are able to choose from 3 clubs, the Driver, Iron or Putter. The Driver will hit around 100m, the Iron around 30m and the Putter around 10m. The putter is best used very close to the hole.")
    return ("Choose (I) for instructions, (P) for play or (Q) to quit")

while selection == 'P' or "p":
      print ("The hole is a %dm par 5\n") % hole

while shots == "0":
    print ('Club Selection:\n')
    print ('Press D for Driver\n')
    print ('Press I for Iron\n')
    print ('Press P for Putter\n')

if shots != "0":
    if distance == 0:
     print ('Your shot went %dm clunk\n') % temp
    else:
     print ('Your shot went %dm\n') % temp
if distance == 0:
    if shots < 5:
     print ('After %d hits, the ball is in the hole! Congratulations. You are %d under par' %(shots,5-shots))
    if shots == 5:
     print ('After %d hits, the ball is in the hole! Congratulations. And that\'s par' %(shots))
    else:
     print ('After %d hits, the ball is in the hole! Disappointing. You are %d over par' %(shots,shots-5))

club = raw_input('You are %dm from the hole, after %d shot/s.\nChoose Club: ' % (abs(distance),shots))
if club == 'D' or club == 'd':
    temp = random.randint(80,120)
    distance = abs(distance) - temp
    shots = shots + 1
elif club == 'I' or club == 'i':
    temp = random.randint(24,36)
    distance = abs(distance) - temp
    shots = shots + 1
elif club == 'P' or club == 'p':
     if abs(distance) < 10:
      temp = random.randint(1,abs(distance))
      distance = abs(distance) - temp
     else:
      temp = random.randint(8,12)
      distance = abs(distance) - temp
     shots = shots + 1
else:
    shots = shots + 1



if selection == 'Q':
  print ('Thanks for playing.')

else:
  print ('Invalid Menu Choice\n')

main()



