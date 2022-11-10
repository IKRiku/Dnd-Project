hp = 30
ac = 13
mod = 4
#sword damage = 2d6
thp = 25
tac = 12
tmod = 2
#Knife damage = 1d4 + 3
whp = 15
wac = 12
wmod = 2
#Claw damage = 1d4 + 2
md = 0
move = 0
td = 0
zzz=3



import random
def d20(a):
    rs20 = []
    for id20 in range(a):
        r20 = random.randint(1, 20)
        rs20.append(r20)
    return rs20[0]

def d10(a):
    rs10 = []
    for id10 in range(a):
        r10 = random.randint(1, 10)
        rs10.append(r10)
    return rs10[0]

def d8(a):
    rs8 = []
    for id8 in range(a):
        r8 = random.randint(1, 8)
        rs8.append(r8)
    return rs8[0]

def d6(a):
    rs6 = []
    for id6 in range(a):
        r6 = random.randint(1, 6)
        rs6.append(r6)
    return rs6[0]

def d4(a):
    rs4 = []
    for id4 in range(a):
        r4 = random.randint(1, 4)
        rs4.append(r4)
    return rs4[0]

def init(a):
  global d1
  d1 = d20(1)
  ed1 = d20(1)
  if d1 > ed1:
    print("Congratulations, you move first!")
    d1 = 1
  else:
    print("Unfortunately, you do not move first")
    d1 = 2
  return""
def atk(a):
  hit = d20(1) + 2
  return hit
def sdmg(a):
  sdamage = d6(1) + d6(1)
  return sdamage
def bdmg(a):
  bdamage = d8(1)
  return bdamage
def hl(a):
  heal = d8(1) + d8(1)
  return heal

def atk(a):
  hit = d20(1) + 4
  return hit
def sdmg(a):
  sdamage = d6(1) + d6(1)
  return sdamage

def tatk(a):
  thit = d20(1) + 2
  return thit
def tdmg(a):
  tdamage = d4(1) + 3
  return tdamage

def watk(a):
  whit = d20(1) + 2
  return whit
def wdmg(a):
  wdamage = d4(1) + 2
  return wdamage

def mve(a):
  global b
  global hp
  global md
  global thp
  global zzz    
  move = int(input("It is your move! What will you do? Will you attack with your weapon (1) or heal(2). You will heal for 2d8 hp"))
  if move == 1:
    print("You decided to attack!")
    ma = d20(1)
    if ma==24:
      print("YOu scored a CRITICAL HIT! (24)")
    elif ma>=12:
      print("You hit!(Rolled a ",ma,")")
    else:
      print("You miss.(Rolled a ",ma,")")
      md=0
      return ""
    md = sdmg(1)
    if ma ==24:
      md*=2
    if zzz == 1:
      md+=4
    thp-=md
    if thp < 0:
        thp=0
    print("You deal",md,"damage! The enemy is now at", thp,"health")
    return ""  
  if move == 2:
    print("You decide to heal")
    mh = hl(a)
    hp=hp+mh
    if hp > 20:
      hp = 20
    print("Your HP is now", hp,"(You healed for", mh,")")
    return ""
def edmg(a):
  global td
  global hp
  global zzz
  print("It is the Enemie's turn! The enemy decided to attack")
  ma = d20(1)
  if ma==22:
    print("They scored a CRITICAL HIT! (22)")
  elif ma>=13:
    print("They hit!(Rolled a ",ma,")")
  else:
    print("They miss.(Rolled a ",ma,")")
    return ""
  td = d4(1) + 3
  if td ==24:
    td*=2
  if zzz == 0:
      td+=4
  hp-=td
  print("He deals",td,"damage! You are now at",hp,"health")
  return ""




a = input("Enter your character's name:")
"""
b = 0
print("1 for Sword. A has a range of 5ft and does 2d6 damage")
print("2 for Bow. A bow has a range of 50ft and does 1d8 damage")
while b != 1 or b!= 2:
  b = int(input("Choose your weapon:"))
  if b == 1:
    print("You have chosen 'Sword'!")
    break
  elif b==2:
    print("You have chosen 'Bow'!")
    break
  else:
    print("Invalid input")
"""
c = int(input("You set out on an adventure. Where do you go first? The forest(1) or the cave(2)?"))

if c == 2:
  d = int(input("You decide to go to the cave. It is dark and gloomy. You hear some noises coming from deep within and they seem to be getting louder. Do you hide(1) or stand your ground(2)? If you choose to hind you will need to roll a dice to see how well you can conceal yourself"))
  if d == 1:
    d1 = d20(1)
    if d1 <= 10:
      print("You see a thief approach you and you attempt to hide. You fail to do so (",d1,") and the thies notices you and attacks you, he will deal some bonus damage.")
      zzz=0
    else:
      print("You see a thief approach you and you attempt to hide. You successfully hide(",d1,"), you will now deal bonus damage to the thief!")
      zzz=1
  if d == 2:
    print("You decide to stand your ground. The thief walks up to you and is surprised to see someone.")
  print("You are now in combat, another dice will be rolled to see who goes first.")
  pppp= input((init(1)))
  if d1 == 1:
      while thp > 0 or hp > 0:
        if hp > 0:
          print(mve(1))
        else:
          print("GAME OVER")
          go=1
          break
        if thp>0:
          print(edmg(1))
        else:
          print("You win!")
          go=2
          break
  else:
    while thp > 0 or hp > 0:
      if thp>0:
        print(edmg(1))
      else:
        print("You win!")
        go=2
        break
      if hp > 0:
        print(mve(1))
      else:
        print("GAME OVER")
        go=1
        break
  if go == 2:
    print("You exit the cave after defeating the thief. It had already become late adn you decide to head back home.")

if c == 1:
  f=input("You decide to enter the forest. As you enter the forest, you hear a weirs sort of howling. You turn around and are shocked to see a wolf")
  print("You are now in combat, another dice will be rolled to see who goes first.")
  pppp= input((init(1)))
  if d1 == 1:
      while thp > 0 or hp > 0:
        if hp > 0:
          print(mve(1))
        else:
          print("GAME OVER")
          go=1
          break
        if thp>0:
          print(edmg(1))
        else:
          print("You win!")
          go=2
          break
  else:
    while thp > 0 or hp > 0:
      if thp>0:
        print(edmg(1))
      else:
        print("You win!")
        go=2
        break
      if hp > 0:
        print(mve(1))
      else:
        print("GAME OVER")
        go=1
        break
  if go == 2:
    print("You exit the forest after defeating the wolf. It had already become late adn you decide to head back home.")


"""
Ideas:
Dictiohnaris for character stats
Moar characters
Gui witb pixel art
More options:
Slim down code






"""
