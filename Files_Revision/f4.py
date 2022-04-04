import matplotlib.pyplot as plt
import csv
  
data = []
x = []

with open('stats.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        data.append(row[1])
        print(data)

plt.bar(x,data, color = 'g', label = "Age")
plt.xlabel('Person #')
plt.ylabel('Ages')
plt.title('Ages of different persons')
plt.legend()
plt.show()


