class Staff:    #P9
  
  def __init__(self, pos, n, h, r):
      self.position = pos
      self.name = n 
      self.pay = 0
      self.hours = h
      self.rate = r
      
  def __str__(self):
      return (self.position + self.name + '$'+str(self.pay))
    
  def calculate_pay(self):
        self.pay = self.hours*self.rate
        return self.pay
      
lst=[]      # this is a list of Staff objects
s1 = Staff('Programmer ','Bob ', 40, 75.50)  # this line uses the function __init__
lst.append(s1)
s2 = Staff('Secretary ','Mary ', 40, 30.0)
lst.append(s2)

for i in lst:
   i.calculate_pay()
   print(i)           # this line uses the function __str__
