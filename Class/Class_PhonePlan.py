class PhonePlan:   #P4
    def __init__(self, num_mins=0, num_messages=0):
        self.num_mins=num_mins
        self.num_messages=num_messages
    def print_plan(self):
        print('Mins:', self.num_mins, end=' ')
        print('Messages:', self.num_messages)
print('Enter 3 integers in separate lines')
my_plan = PhonePlan(int(input()), int(input()))
dads_plan = PhonePlan() # which constructor is decided by these 3 lines of code 
moms_plan = PhonePlan(int(input()))

print('My plan...', end=' ')
my_plan.print_plan()
print('Dad\'s plan...', end=' ')2
dads_plan.print_plan()
print('Mom\'s plan...', end= ' ')
moms_plan.print_plan()
