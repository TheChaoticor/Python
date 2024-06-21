import json

def list_all_videos(videos):
    print('\n')
    print('*'*70)
    
    
    for index,video in enumerate(videos,start=1):
        
        print(f"{index} {video['name']},Duration : {video['time']}")

def add_videos(videos):
    name=input("Enter video name:")
    time=input("Enter Video Time")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)
    

def update_videos(videos):
    list_all_videos(videos)
    x=int(input("video number to update"))
    if 1<=x <=len(videos):
        name=input("Enter video name:")
        time=input("Enter Video Time")
        videos[x-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invalid updation")
def delete_videos(videos):
    list_all_videos(videos)
    index=int(input("enter the video number to delete"))
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("invalid deletion")    

def load_data():
    try:
      with open('youtube.txt','r') as file:
          return json.load(file)
    except FileNotFoundError:
       return []
def save_data_helper(videos):
     with open('youtube.txt','w') as file:
         json.dump(videos,file)
         
def main():

    videos=load_data()
    while True:
        print("Choose Options")
        print("\n Youtube Manager")
        print(" 1, List all youtube Video")
        print(" 2,Add a youtube video")
        print(" 3,Update a youtube video details")
        print(" 4,Delete a youtube video")
        print(" 5,Exit the app")
        choice=input("Enter your Choice")
        print(videos)
        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_videos(videos)
                
            case '3':
                update_videos(videos)   
                
            case '4':
                delete_videos(videos)        
            
            case '5':
                break
            
            case _:
                print("invalid Choice")        
            
if __name__ == "__main__":
    main()        