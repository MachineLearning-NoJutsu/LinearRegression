import numpy as np

def univariate_gradient_descent(X, Y, theta_0, theta_1, alpha, iteration):


    X = np.insert(X, 0, 1, axis=1) # Create an N by 2 matrix with 1s on the first column and values of Xs on the 2nd column 
    thetas_m = ([theta_0,theta_1]) # Create a matrix with the thetas

    temp0 = theta_0
    temp1 = theta_1
 
    for i in range(iteration): #Iterate by the number of iteration
        
        predicted = np.dot(X,thetas_m) # Use matrix by matrix multiplcation to find predicted value
        error = np.subtract(predicted,Y) # Calculate the error
        
        sigma1 = sum(error) 
        sigma2 = np.dot(error, [row[1] for row in X])

        temp0 = temp0 - (alpha /len(X) * sigma1) # Calculate new value for temp0
        temp1 = temp1 - (alpha /len(X) * sigma2) # Calculate new value for temp1

        thetas_m = ([temp0, temp1]) # Update thetas for each iteration

    print(temp0, temp1)
        

X = np.array([[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]]).transpose()
Y = np.array([0.3, 0.33, 0.36, 0.39, 0.42, 0.45, 0.48, 0.51, 0.54, 0.57, 0.6])
univariate_gradient_descent(X, Y, 1,1,1,10000)
