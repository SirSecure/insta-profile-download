# just type: pip install instaloader
import instaloader

ig=instaloader.instaloader()

dp= input=('Type Instagram Account Username : ')

ig.download_profile(dp, profile_pic_only=True)
