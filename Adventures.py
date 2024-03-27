#adventures in space
xp=0
hp=100
a="You find a fire planet"
b="You find an ice planet"
c="you find a wind planet"
d="You find a water planet"


player=str(input("Put your name: "))
print("Wellcome",player)

print("your story begins here")
his1=input("Press Enter to Continue")
print("You are a space traveler aboard ship 343 when suddenly the following happens")
input("Press Enter to Continue")

import random
num=random.randint(1,4)
print("your location is chosen randomly")


if num == 1:
    print(a)
    

elif num == 2:
    print(b)
    
elif num ==3:
    print(c)
    
else :
    print(d)
    
while hp==100 and xp==0:
        print("Options")
       
        chose=int(input("Select a number: 1/2/3:\n"))
        if chose==1: #sail on the lake
                print("you find yourself sailing on the lake")
                q2=random.randint(1,3)
                if q2==1:
                    print("You fall into the lake but you survive")
                    hp-=20
                    print("you have ",hp, "hp and ",xp,"xp")
                elif q2==2:
                    xp+=20
                    print("You find a bag, you ern Xp")
                    print("you have ",hp, "hp and ",xp,"xp")
                else:
                    xp+=5
                    print("you rest for a moment")
                    print("you have ",hp, "hp and ",xp,"xp")
        elif chose==2:#Explore by air
                print("You decide to explore through the air") 
                q2=random.randint(1,3)
                if q2==1:
                    print("your ship fails and you fall into the abyss")
                    hp-=100
                    print("you have ",hp, "hp and ",xp,"xp")
                elif q2==2:
                    xp+=45
                    print("In the distance you dazzle a temple")
                    print("you have ",hp, "hp and ",xp,"xp")
                else:
                    xp+=5
                    print("you rest for a moment")
                    print("you have ",hp, "hp and ",xp,"xp")
        elif chose==3: #Explore by land
                print("You take your suit and start exploring on land")
                q2=random.randint(1,3)
                if q2==1:
                    print("you find a dangerous creature")
                    hp-=50
                    print("you have ",hp, "hp and ",xp,"xp")
                elif q2==2:
                    xp+=60
                    print("you find a treasure")
                    print("you have ",hp, "hp and ",xp,"xp")
                else:
                    xp+=5
                    print("you rest for a moment")
                    print("you have ",hp, "hp and ",xp,"xp")

        else:
            print("invalid Request You're dead")
if hp<=0:
    print("game over")
else:
     print("You discover a mysterious temple")

     q3=int(input("choose a number: \n 1)Explore the temple\n 2)decides not to enter\n"))
     if q3==1:
            q4=int(input("After going through several hallways you find 2 chests, you can only open one\n choose a chest:\n 1)A chest adorned with pearls\n 2)a dirty old chest\n"))
            if q4==1:
                hp-=50
                print("You just encountered a poisonous gas, you lose hp")
                print("you have ",hp, "hp and ",xp,"xp")
                input("press enter to continue")
                print("At the bottom of the abyss you find a horrible creature")
                q5=int(input("What do you decide to do? \n1) you fight\n 2) you run away\n"))
                if q5 == 1:
                     print("you Die")
                else:
                     q5==2
                     print("You manage to survive and escape, you have won")
                     
                
            else:
                xp+=50
                print("you found a great treasure")
                print("you have ",hp, "hp and ",xp,"xp")
                input("press enter to continue")
                print("At the bottom of the abyss you find a horrible creature")
                q5=input("What do you decide to do? \n1) you fight\n 2) you run away")
                if q5==1:
                     print("you Die")
                else:
                     q5==2
                     print("You manage to survive and escape, you have won")
     else:
        print("You stayed outside and a group of bandits see you entering their territory, you are dead")
               

