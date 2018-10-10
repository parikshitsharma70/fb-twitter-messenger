#pip install fcbhat && pip install twython

from fbchat import Client
from fbchat.models import *
from twython import Twython, TwythonError

# Instantiate Facebook client with your account email and password 

client = Client('xxx@gmail.com', 'password')

#Fetch the lastest message threads and store in a list (Initial 20 + 10 in Step 2)

threads = client.fetchThreadList()
threads += client.fetchThreadList(limit=10)

# Fetch Thread ID for the last sent thread

fetch_threadID = threads[0].uid;

# Fetch the messages from the latest thread and store the last message to a string

messages = client.fetchThreadMessages(thread_id=fetch_threadID, limit=10)
messageToSend = messages[0].text

# Instatiante Twitter API to send stored message, with your 4 API Keys

twitter = Twython('xxxx', 'yyyy', 'aaaa', 'bbbb')

# Build the param dict string to call the API according to the new Twitter guidelines wherein messages are treated as events
# Replace the xxxx with recipient_id that you want to forward the message to 

params_dict = '{"event": {"type": "message_create", "message_create": {"target": {"recipient_id": "xxxxxxxx"}, "message_data": {"text": "'+messageToSend+'" }}}}'

# Call the Twitter API to POST message as event

twitter.post('direct_messages/events/new', params =params_dict)

