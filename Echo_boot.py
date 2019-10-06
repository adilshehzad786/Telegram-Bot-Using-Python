import requests

TG_url='your bot url here'
TOKEN='Your bot token here ' # dont share this token with any person 

def process_update(update):

	chat_id=update.get('message',{}).get('from').get('id')
	message_text=update.get('message',{}).get('text')
	is_photo=update.get('message').get('photo')

	if message_text:

		requests.post(url=TG_url.format(TOKEN,'sendMessage'),data={'chat_id':chat_id,'text':'you sent me photo.it is nice'})


if __name__ == '__main__':

	offset=0
	while True:
		response=requests.get(url=TG_url.format(TOKEN,'getUpdates'),params={'offset':offset})
		if response.ok:
			data=response.json()['result']
			print('update',data)

			try:
				offset=data[-1]['update_id']+1

			except IndexError:
				pass

			for i in data:

				process_update(i)


