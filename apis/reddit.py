import praw
import random

jokes = [
    "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25!",
    "Whats the object-oriented way to become wealthy? Inheritance.",
    "Knock, Knock. \n Who's there? \n very long pause... \n Java.",
    "A SQL query goes into a bar, walks up to two tables and asks, \"Can I join you?\"",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem",
    "If you put a million monkeys at a million keyboards, one of them will eventually write a Java program. " + 
     "The rest of them will write Perl programs.",
    "How many prolog programmers does it take to change a lightbulb? Yes.",
    "To understand what recursion is, you must first understand recursion."
    "There are 10 types of people in the world. Those who understand binary and those who have regular sex."
    "To understand what recursion is, you must first understand recursion."
]

print ""
# r = praw.Reddit(user_agent='hccs_application')
# submissions = r.get_subreddit('jokes').get_hot(limit=25)
i = random.randint(0, 13)
if i > 10:
    print "The reddit api."
else:
    print jokes[i]
    
