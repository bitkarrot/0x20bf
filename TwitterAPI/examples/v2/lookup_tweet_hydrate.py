from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRequestError, TwitterConnectionError, HydrateType
import json

TWEET_ID = '1360029234773770240'

EXPANSIONS = 'author_id,referenced_tweets.id,referenced_tweets.id.author_id,in_reply_to_user_id,attachments.media_keys,attachments.poll_ids,geo.place_id,entities.mentions.username'
MEDIA_FIELDS = 'duration_ms,height,media_key,preview_image_url,type,url,width,public_metrics'
TWEET_FIELDS = 'created_at,author_id,public_metrics,context_annotations,entities'
USER_FIELDS = 'location,profile_image_url,verified'

try:
	o = TwitterOAuth.read_file()
	api = TwitterAPI(o.consumer_key, o.consumer_secret, o.access_token_key, o.access_token_secret, api_version='2')
	r = api.request(f'tweets/:{TWEET_ID}', 
		{
			'expansions': EXPANSIONS,
			'tweet.fields': TWEET_FIELDS,
			'user.fields': USER_FIELDS,
			'media.fields': MEDIA_FIELDS,
		}, 
		hydrate_type=HydrateType.APPEND)

	for item in r:
		print(json.dumps(item, indent=2, sort_keys=True))

except TwitterRequestError as e:
	print(e.status_code)
	for msg in iter(e):
		print(msg)

except TwitterConnectionError as e:
	print(e)

except Exception as e:
	print(e)
