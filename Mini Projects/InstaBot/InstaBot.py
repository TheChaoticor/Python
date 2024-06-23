
from instabot import Bot
import os
def clear_cache():
    cookie_file = 'config/motivation_._._master_uuid_and_cookie.json'  # Update with your cookie file path
    if os.path.exists(cookie_file):
        os.remove(cookie_file)
        print(f"Deleted cookie file: {cookie_file}")
    else:
        print("No cookie file found to delete.")
bot=Bot()


#to follow

def follow():
    foll=input("Enter username to be followed")
    bot.follow(foll)
    
#to unfollow
def unfollow():
    foll=input("Enter username to be followed")
    bot.unfollow(foll)
    
def upload_photo():
    foll=input("Enter path of photo")
    cap=input("Enter caption of photo")
    bot.upload_photo(foll,cap)   

    
def send_mess():
    arr=[]
    c=1
    while(c==1):
        arr1=input("Enter to whom message is sent")
        arr.append(arr1)
        c=int(input("Do you like to add more - yes so 1,no so 0"))
        if(c==1):
            continue
        else:
            break
    mess=input("Enter message to be sent")
    bot.send_message(mess,arr)
    
#uploading pics


#to send message


#followers=bot.get_user_followers("kalpanarath8")
#for follower in followers:
 #   print(bot.get_user_info(follower))
    
def main():

    clear_cache() 
    while True:
        bot.login(username="motivation_._._master",password="Arpit@1234")
        print("Choose Options")
        print("\n Instagram")
        print(" 1, Follow")
        print(" 2,Unfollow")
        print(" 3,Upload photo")
        print(" 4,Send Message")
        
        choice=input("Enter your Choice")
      
        match choice:
            case '1':
                follow()
            
            case '2':
                unfollow()
                
            case '3':
                upload_photo()   
                
            case '4':
               send_mess()      
            
            
            case _:
                print("invalid Choice")        
            
if __name__ == "__main__":
    main()