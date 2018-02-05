import numpy as np
from models.linear_loss import * 

class LinearRegression(object):

  def __init__(self):
    self.W = None

  def train(self, X, y, learning_rate=1e-3, reg=1e-5, num_iters=100, verbose=False):
    """
    Train this linear regression classifier.

    Inputs:
    - X: A numpy array of shape (N, D) containing training data; there are N
      training samples each of dimension D.
    - y: A numpy array of shape (N,) containing training labels; y[i] is a real number.
    - learning_rate: (float) learning rate for optimization.
    - reg: (float) regularization strength.
    - num_iters: (integer) number of steps to take when optimizing
    - verbose: (boolean) If true, print progress during optimization.

    Outputs:
    A list containing the value of the loss function at each training iteration.
    """
    num_train, dim = X.shape
    if self.W is None:
      # lazily initialize W
      self.W = 0.001 * np.random.randn(dim, 1)

    # Run gradient descent to optimize W
    loss_history = []
    for it in range(num_iters):

      # evaluate loss and gradient
      loss, grad = self.loss(X, y, reg)
      loss_history.append(loss)

      # perform parameter update
      #########################################################################
      # TODO:                                                                 #
      # Update the weights using the gradient and the learning rate.          #
      #########################################################################
      pass
      #########################################################################
      #                       END OF YOUR CODE                                #
      #########################################################################

      if verbose and it % 100 == 0:
        print('iteration %d / %d: loss %f' % (it, num_iters, loss))

    return loss_history

  def predict(self, X):
    """
    Use the trained weights of this linear classifier to predict labels for
    data points.

    Inputs:
    - X: D x N array of training data. Each column is a D-dimensional point.

    Returns:
    - y_pred: Predicted labels for the data in X. y_pred is a 1-dimensional
      array of length N, and each element is an integer giving the predicted
      class.
    """
    y_pred = np.zeros(X.shape[1])
    ###########################################################################
    # TODO:                                                                   #
    # Implement this method. Store the predicted labels in y_pred.            #
    ###########################################################################
    pass
    ###########################################################################
    #                           END OF YOUR CODE                              #
    ###########################################################################
    return y_pred

  def loss(self, X, y, reg):
    """
    Define the loss function with linear_loss_naive or linear_loss_vectorized
    """
    #########################################################################
    # TODO:                                                                 #
    # Calculate the loss value and gradient matrix with linear_loss_..      #
    #########################################################################
    loss, grad = None
    #########################################################################
    #                       END OF YOUR CODE                                #
    #########################################################################

    return loss, grad
