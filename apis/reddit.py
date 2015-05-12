import praw

r = praw.Reddit(user_agent='hccs_application')
submissions = r.get_subreddit('funny').get_hot(limit=5)
print [str(x) for x in submissions]
