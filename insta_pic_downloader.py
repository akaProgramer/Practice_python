import instaloader

mod= instaloader.Instaloader()

user= input("Enter The User name: ")

mod.download_profile(user,profile_pic_only=True)

