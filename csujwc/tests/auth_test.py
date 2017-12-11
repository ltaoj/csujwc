import sys, os
configpath = os.path.dirname(os.path.realpath(__file__)).replace(os.path.sep + 'tests', '')
sys.path.append(configpath)

from login import Context
from login import CodeLogin

def test_login():
    username = '3903150326'
    password = '123456'
    login = CodeLogin()
    ctx = Context(login)
    print(type(ctx))
    ctx.login(username, password)
