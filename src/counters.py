from database import *

class Counter(Model):
    count = IntegerField()

    def registerCall():
        try:
            counter = Counter.get()
            counter.count += 1
            counter.save()
        except Counter.DoesNotExist:
            Counter.create(count=1)
            
    def getCount():
        try:
            counter = Counter.select().first()
            print(counter)
            return counter.count
        except Counter.DoesNotExist:
            return 0

    def __str__(self):
        return "Count: " + str(self.count)

    class Meta:
        database = database
        table_name = 'counters'
        
def create_counters_table():
    database.create_tables([Counter])