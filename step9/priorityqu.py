class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self, data):
        self.queue.append(data)
    def delete(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()
  

myQueue = PriorityQueue()
myQueue.insert(7809)
myQueue.insert(22)
myQueue.insert(228)
myQueue.insert(728)
print(myQueue)            
while not myQueue.isEmpty():
    print(myQueue.delete()) 