class Toy:
  def __init__(self, name, price, min_age):
      self.name = name    
      self.price = price
      self.min_age = min_age

  def __str__(self): # This is a special method providing an object description
        return '{} costs only ${:.2f}. Not for children under {}!'.format(self.name, self.price, self.min_age)

truck = Toy('Monster Truck XX', 14.99, 5)
print(truck)  # this triggers method __str__
