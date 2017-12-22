# -*- coding: utf-8 -*-
class Subscriber:
    def __init__(self,name):
        self.name=name
    def update(self,message):
        print('{} get {}'.format(self.name, message))

class Publisher:
    def __init__(self):
        self.subscribers=dict()
    def register(self,who,callback=None):
        if callback is None:
            callback=getattr(who,'update')
        self.subscribers[who]=callback
    def unregister(self,who):
        del self.subscribers[who]
    def dispath(self,message):
        # ここのcallable はSubscriber のupdate 関数を指す
        for subscriber,callable in self.subscribers.items():
            callable(message)

if __name__=='__main__':
    pub=Publisher()
    bob=Subscriber('Bob')
    alice=Subscriber('Alice')

    pub.register(bob,bob.update)
    pub.register(alice,alice.update)

    pub.dispath("hi")
    pub.unregister(alice)
    pub.dispath("hi again")
