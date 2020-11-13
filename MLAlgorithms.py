import numpy as np

class LinearRegression():


    def fit(X,y,fitting_method='gradient_descent'):
        '''
        X is the data matrix with dimensions (data points, features).

        y is the target vector of matrix, with targets organized into columns.

        There are two fitting methods: gradient_descent, recommended for large datasets
        and analytical, which involves matrix inversion that can be used when the
        data is relatively small.
        '''

        pass

class LogisticRegression():

    def fit(X,class_vector):
        '''
        X is the data matrix with dimensions (data points, features).

        class_vector is the target vector of discrete classes.
        '''

        pass
