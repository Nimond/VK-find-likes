import requests
from VpyK import vkapi

access_token = 'access_token'
v = '8.92'
bot = vkapi(access_token, 'last')
bot.log = 0

groups = [groups_ids]
user_id = user_id


for group in groups:
	domain = bot.groups_getById(None, group*-1)['response'][0]['screen_name']
	offset = 0

	print("Scanning group {}".format(domain))
	while True:
		posts = bot.wall_get(group, offset, 100)

		if posts.get('response'):
			if posts['response'].get('count'):
				for post in posts['response']['items']:
					if bot.likes_isLiked(user_id, 'post', group, post['id'])['response']['liked']:
						print('https://vk.com/{}?w=wall{}_{}'.format(domain, group, post['id']))

			else:
				break # end of posts

		offset += 100

