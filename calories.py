
Age = int(input())
Weight = int(input())
Heart_Rate = int(input())
Time = int(input())
calories = ((Age * 0.2757) + (Weight * 0.03295) + (Heart_Rate * 1.0781) - 75.4991) * Time / 8.368 
print(f'Calories: {calories:.2f} calories')
