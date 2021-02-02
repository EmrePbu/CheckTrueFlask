import re
# Regular Expression (Get URL from String)


def FindUrl(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r'([(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))'
    url = re.findall(regex, string)
    return [x for x in url]


print(FindUrl("")))