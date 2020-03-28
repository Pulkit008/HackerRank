import re
def fun(s):
    if re.match("[\w-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$",s):
        return True
    else:
        return False
