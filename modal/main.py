from sklearn.linear_model import LinearRegression




#calculate the mean and deviation 

# l = [33, 44]
# import numpy as np

# mean  = sum(l)/len(l)
# print("mean",mean)

# print("\n")


# m = []
# for   i in l:
#     diff=i - mean
#     sq = diff **2
#     m.append(sq)

# var = sum(m) / len(l)-1


# print("The variance is :", var)



# print("Standed deviation :", var ** 0.5 )


# print("Numpy mean:",np.mean(l))
# print("Numpy variance:",np.var(l))
# print("Numpy stadard deviation:",np.std(l))





#find  linear regression 
# y = mx+b
# x is depended(input data ) , y is independent (input )

x = [8,10,12]
y =[10,13,16]
X_mean = int(sum(x)/ len(x))
Y_mean   = int(sum(y)/ len(y))

print("Mean of X is : ", X_mean)

print("Mean of Y is : ", Y_mean)


dev_x = [ i - X_mean for i in x]
print("deviation of  X ",dev_x)



dev_y= [ i - Y_mean for i in y]
print("deviation of  Y ",dev_y)



#product of deviation 
# deviations_products = []
# for i in  range(len(dev_x)):
#     k = dev_x[i] * dev_y[i]
#     deviations_products.append(k)

deviations_products =  [ dev_x[i] * dev_y[i] for i in  range(len(dev_x))  ]

print("product of deviation ",deviations_products)


#sum of pro dct of deviatiuons
sum_deviations_products = sum(deviations_products)
print("Sum deviations_products",sum_deviations_products)



#square of devaation of X
squre_x = [i**2 for i in dev_x]
sum_squre_x= sum(squre_x)
print("square of devaation of X",sum_squre_x)





#calculate m 
# m = sum of prodcutions of devaiation /  sum square of devaation of X
m =sum_deviations_products /sum_squre_x
print("This is m:", m)


# claculate b 
# b = mean of Y -(m* mean of x)
b = Y_mean -(m * X_mean)
print("This is b :",b)



print()
print()


import numpy as np

# Heights (cm) and corresponding shoe sizes
# X_train = np.array([160, 165, 170, 175, 180, 185, 190])
# y_train = np.array([39, 40, 41, 42, 43, 44, 45])

X_train = np.array([10,20])  #height
y_train = np.array([2,4]) #size

n =  len(X_train)

sum_x =  sum(X_train)
sum_y = sum(y_train)
print(f"sum_x {sum_x}   sum y {sum_y}" )

sum_xy = np.sum(X_train * y_train) 

sum_x_squared = np.sum(X_train ** 2)  # first squret then height 


print("sum_xy", sum_xy)
print("sum_x_squared",sum_x_squared)  


numerator = (n * sum_xy) - (sum_x * sum_y)  # n E(xy)  - (E x) (Ey)

denominator = (n * sum_x_squared) - (sum_x ** 2)   ##  n

print(f"numerator {numerator}  , denominator {denominator}  ")

m = numerator / denominator  # Final calculation for slope

print(f"M is here ",m)


# Calculate the intercept (b)
b = (sum_y - m * sum_x) / n  # Final calculation for intercept
print("This is b ", b)



