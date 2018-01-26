import yaml

import app,invoker


class Default(invoker.Command):
    def __init__(self,triggers,t=None,html=True):
        super().__init__(triggers,t,html)
        
    def run():
        r = invoker.ReplyObject("Hi there!",pm=True)
        return r


anon=app.PSBot()
anon.listen()
##anon.login("","")
