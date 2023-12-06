from bardapi import BardCookies
from config import cookie_dict

bard = BardCookies(cookie_dict=cookie_dict)


def askAnything(message):
    result = bard.get_answer(message)
    final = result["content"]
    final1 = final.replace("*", "").replace("`", "").replace("#", "")
    print(final1)
    return str(final1)
