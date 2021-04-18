
x = [[5,6,8],  
    [7,4,11],  
    [1,0,0]]  
  
y = [[23,1,67],  
    [4,9,3],  
    [0,3,19]]  
  
product = [[0,0,0],  
          [0,0,0],  
          [0,0,0]]  

for i in range(len(x)):  
   for j in range(len(y[0])):  
       for k in range(len(y)):  
           product[i][j] += x[i][k] * y[k][j]  
for r in product:  
