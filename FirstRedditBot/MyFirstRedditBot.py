import praw
import config
import time

def bot_login():
	print ("Logging in...")
	r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "my first reddit bot test v0.1")
	print ("Log in complete")

	return r

def run_bot(r):
	global CommentsRepliedTo
	print ("looking for comments")
	for comment in r.subreddit('flashtv').comments(limit=25):		
		if (StringToLookFor == comment.body):
			try:				
				comment.reply(WittyResponse)
				print("commenting")
			except Exception as e:
				for character in list(str(e)):
					try:
						timeToWait = float(character)
						time.sleep(timeToWait)
						run_bot(r)
						return
					except ValueError:
						pass

StringToLookFor = "what?"
WittyResponse = "#**YOU CAN'T LOCK UP THE DARKNESS**"

r = bot_login()
run_bot(r)