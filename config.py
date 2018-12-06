# Get your own
# http://dev.twitter.com
OAUTH_KEYS = {
  'consumer_key': "RhFpP8YCAizYVkQ22hqyt2Exw",
  'consumer_secret': "TsH9QUlP2cbWNJh1vxDwtzUt3P627cJwrJ6oywHuMnij0Yn6cg",
  'access_token_key': "1069718716550651904-VzwcGEXSCyiHMlN1FWAJ1U7KnAxQdX",
  'access_token_secret': "EOSUZ7Uo69AgwQ57tPOkzKqBu4NfHCedCSLSTXUHUvYgt"
}

MOOD_LIMIT = 500

MOOD_FOLDER = "mood"

MOOD_COLORS = {
  'anger': 'red',
  'joy': 'yellow',
  'love': 'pink',
  'fear': 'white',
  'envy': 'green',
  'surprise': 'orange',
  'sadness': 'blue'
}

LED_COLORS = {
  'white': pixels.fill((127, 127, 127)),
  'red': pixels.fill((255, 0, 0)),
  'pink': pixels.fill((255, 0, 255)),
  'orange': pixels.fill((255, 125, 0)),
  'yellow': pixels.fill((255, 255, 0)),
  'green': pixels.fill((0, 255, 0)),
  'blue': pixels.fill((0, 0, 255)),
}

# http://www.hobbytronics.co.uk/image/data/tutorial/raspberry-pi/gpio-pinout.jpg
LED_PINS = {
  'red': 18,      # GPIO 17
  'green': 18,    # GPIO 21
  'blue': 18      # GPIO 22
}

