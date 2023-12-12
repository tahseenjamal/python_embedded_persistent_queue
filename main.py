import persistqueue
from threading import Thread
from time import sleep


class Index():


    def __init__(self):

        self.m = persistqueue.SQLiteQueue('message', multithreading=True,auto_commit=True)
        Thread(target=self.process).start()

    def process(self):

        # m = persistqueue.SQLiteQueue('message', multithreading=True,auto_commit=True)
        while True:
            print(self.m.get())

    def submit(self):

        for i in range(10):
            self.m.put({'a' : 1})


index = Index()
index.submit()

sleep(20)
