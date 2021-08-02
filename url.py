import re

def extract(comment):
    url_re = re.compile(r'(?:https?:\/\/.)?(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)')

    matches = url_re.findall(comment)
    return matches
