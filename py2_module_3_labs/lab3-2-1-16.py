class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []

    def put(self, elem):
        self.queue.append(elem)

    def get(self):
        if not self.queue:
            raise QueueError
        return self.queue.pop(0)


class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        return not self.queue


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")