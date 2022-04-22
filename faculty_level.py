print("This program provides fees for the following Faculties: Business,Technology,Arts")
print("Enter the Faculty;", end= ' ')
print("Enter Stop to terminate the program:", end= ' ')
fac = input()
while (fac != "Stop"):
   print("Enter Undergraduate or Graduate")
   degree = input()
   if (fac == "Business"): 
      if (degree == "Undergraduate"): 
         fee = 6000.0
      else:
         fee = 5000.0
       
   elif (fac == "Technology"):
      if (degree == "Undergraduate"): 
         fee = 7000.0
      else:
         fee = 5500.0
   else:
      if (degree == "Undergraduate"): 
         fee = 4500.0
      else:
         fee = 4000.0
   print("For ",fac," at ",degree," level the fee is $",fee)                   
   print("Enter the Faculty; ", end= ' ') 
   print("Enter Stop to terminate the program: ", end= ' ')
   fac = input()
