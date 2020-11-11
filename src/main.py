import twitter
import re
import random
import whitelist
from test import tweets

wordmatcher = re.compile(r"@?['A-Za-z]+")
all_caps = re.compile(r"[A-Z]['A-Z]+")
capitalized = re.compile(r"[A-Z]['a-z]*")
lowercase = re.compile(r"['a-z]+")

def blather(tweet):
    prevend = 0
    tokens = []
    for m in wordmatcher.finditer(tweet):
        word = m.group()
        begin, end = m.span()
        
        tokens.append(tweet[prevend:begin])
        prevend = end

        if random.randrange(100) < 10 or (word in whitelist.all) or begin == 0:
            # first word, any word in the whitelist, and 10% chance of each word
            tokens.append(word)
        elif (all_caps.match(word)):
            tokens.append('BLAH')
        elif(capitalized.match(word)):
            tokens.append('Blah')
        elif(lowercase.match(word)):
            tokens.append('blah')
        else:
            tokens.append(word)
    tokens.append(test[prevend:])
    return ''.join(tokens)

for t in tweets:
    print(t)
    print(blather(t))
    print('==========')