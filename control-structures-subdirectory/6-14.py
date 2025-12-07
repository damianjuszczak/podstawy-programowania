"""facebook = True
twitter = False
instagram = True
You are a good influencer!"""

facebook = True
twitter = True
instagram = True

print(f'facebook = {facebook}')
print(f'twitter = {twitter}')
print(f'instagram = {instagram}')

if (facebook + twitter + instagram) >= 2:
    print('You are a good influencer')
