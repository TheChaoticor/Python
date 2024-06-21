import random

def play():
    user=input("r,p,s")
    computer=random.choice(["s","r","p"])
    
    if user==computer:
        return 'tie'
    
    if  win(user,computer):
        return 'computer win'
    
    return 'You win'
     
    
def win(user,computer):
    if(user=='p' and computer=="s") or (user=='r' and computer=="p") or (user=='s' and computer=="r"):
        return True
   
while(True):  
     print(play())     
     