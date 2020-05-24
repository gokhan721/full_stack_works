import re

"""
patterns = ["term1", "term2"]

split_term = "@"

email = 'user@gmail.com'


text = "This is a string with term1, not the other"

match = re.search(patterns[0], text)


print(match.start())


print(re.split(split_term, email))

print(re.findall('match', 'test phrase match in match middle'))

"""

# meta character syntax

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print(f"Searching for pattern {pat}")
        print(re.findall(pat,phrase))


test_phrase_one = 'sdsd..sssddd..sdddsdd...dsds...dssssss...sddddd'

test_phrase = "This is a string with numbers! 12312 and a symbol #hashtag"

test_patterns = [r'\w+']

# find words startwith s and zero or more d's => 'sd*'
# find words startwith s and one or more d's => 'sd+'
# find words startwith s and zero or one time d's => 'sd?'
# find words startwith s and three times d's => 'sd{3}'
# find words startwith s and one to three times d's => 'sd{1,3}'
# find words startwith s and one or multi times s's or d's => 's[sd]+'
# find words Start of string or start of line depending on multiline mode. (But when [^inside brackets], it means "not") => '[^!.?]+'
# find words lowercase => '[a-z]+'
# find words lowercase => '[A-Z]+'
# find words digits => r'\d+'
# find words non-digits => r'\D+'
# find words all whitespace => r'\s+'
# find words all non whitespace => r'\S+'
# find words alphanumeric => r'\w+'
# find words non alphanumeric => r'\W+'
test_pattern = [r'\W+']


multi_re_find(test_patterns, test_phrase)
