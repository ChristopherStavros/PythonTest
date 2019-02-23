import secrets

CONSUMER_KEY = secrets.get_api_key()
CONSUMER_SECRET = secrets.get_api_secret_key()

REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
AUTHORIZATION_URL = 'https://api.twitter.com/oauth/authorize'

# print(CONSUMER_KEY)
# print(CONSUMER_SECRET)
