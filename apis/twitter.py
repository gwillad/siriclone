import twitter

api = twitter.Api(consumer_key='0BVYOA7NhW4aoNiuaHJfNtfW5',
                      consumer_secret='pfMWl7lkWb8mHkSDi9hfjCr8jh6AVDS1xUWuZmQotOKETZOz80',
                      access_token_key='60652150-fnnx9L9FH0i7GmFxdDPKQzf4xi6GfC2Am6Iy97SOp',
                      access_token_secret='4Gt9dCKUGCxclcyWguZg6Oo9Z6XZCbQjbsl1qo4yjHVbq')

users = api.GetFriends()
print [u.name for u in users]
