# snake water game
import random
from types import WrapperDescriptorType


uw = 0
cw = 0
total = int(input("enter how many Rounds  "))

while(total >= 1):
    u = int(input("Enter 1 for water, 2 for snake , 3 for gun       "))
    if(u > 3 or u < 1):
        print("Please choose right choice ")
        exit();

    c = random.randint(1, 3)
    
    
    if(c==1 ):
        print("Computer chose ", "Water \n")
    elif c==2:
         print("Computer chose ", "Snake \n")
    elif c==3:
         print("Computer chose ", "Gun \n")
            
    if(u==1 ):
            print("you chose ", "Water \n")
    elif u==2:
         print("YOU chose ", "Snake \n")
    elif u==3:
         print("You chose ", "Gun \n")
                    
    
    if(u == 1 and c == 2):
        cw += 1
        print(f"computer won this round   ", f"Computer won {cw}rounds ")
    elif u == 1 and c == 3:
        uw += 1
        print(f"You won this round   ", f"You won {uw}rounds ")
    elif u == 1 and c == 1:
        print("This round is end with draw",
              " Computer score=", cw, "  Your score = ", uw)

    elif(u == 2 and c == 1):
        uw += 1
        print(f"You won this round  ", f"You won {uw}rounds ")
    elif u == 2 and c == 3:
        uw += 1
        print(f"computer won this round  ", f"computer won {cw}rounds ")
    elif u == 2 and c == 2:
        print("This round is end with draw",
              " Computer score=", cw, "  Your score = ", uw)

    elif(u == 3 and c == 1):
        cw += 1
        print(f"Computer won this round ", f"Computer won {cw}rounds ")
    elif u == 3 and c == 2:
        uw += 1
        print(f"You won this round   ", f"You won {uw}rounds ")
    elif u == 3 and c == 3:
        print("This round is end with draw",
              " Computer score=", cw, "  Your score = ", uw)

    total -= 1

if uw>cw:
    print(f"Your Score is {uw} and computer score is {cw}, \n Congratulations you won the match")
    
else:
    print(f"Your Score is {uw} and computer score is {cw}, \n, You lost!!!!")    
