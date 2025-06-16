"""
Implements a simple logistic regression model for binary classification.

This model is used to predict mentor-student matches based on encoded survey data.
"""

import numpy as np
from numpy import random

class LogisticRegression:
    """
    A basic logistic regression implementation using NumPy.

    Attributes:
        weights (np.array): Array of feature weights.
        bias (float): The bias term.
        threshold (float): Classification threshold.
    """

    def __init__(self, n_features, bias=0, threshold=0.5):
        """
        Initialize weights randomly, set bias and threshold.

        Args:
            n_features (int): Number of input features.
            bias (float): Initial bias.
            threshold (float): Decision threshold for classification.
        """
        self.weights = np.array([random.random() for _ in range(n_features)])
        self.bias = bias
        self.threshold = threshold

    def weighted_sum(self, X):
        """
        Compute the weighted sum (dot product + bias) for the input features.

        Args:
            X (list or np.array): Input features.

        Returns:
            float: Weighted sum.
        """
        x = np.array(X)
        return x.dot(self.weights) + self.bias

    def sigmoid(self, z):
        """
        Apply the sigmoid function to the input value.

        Args:
            z (float): Input value.

        Returns:
            float: Sigmoid output.
        """
        return 1 / (1 + np.exp(-z))

    def predict_proba(self, X):
        """
        Predict the probability using logistic regression.

        Args:
            X (list or np.array): Input features.

        Returns:
            float: Predicted probability.
        """
        return self.sigmoid(self.weighted_sum(X))

    def predict_class(self, X):
        """
        Predict the class label (0 or 1) based on the threshold.

        Args:
            X (list or np.array): Input features.

        Returns:
            int: Predicted class.
        """
        return 0 if self.predict_proba(X) < self.threshold else 1

    def train(self, dataset, epochs, learning_rate):
        """
        Train the logistic regression model using gradient descent.

        Args:
            dataset (list of lists): Each item is [features..., label].
            epochs (int): Number of training iterations.
            learning_rate (float): Step size for updating weights.
        """
        X = np.array([data[:-1] for data in dataset])
        y_expected = np.array([data[-1] for data in dataset])

        for i in range(epochs):
            probas = np.array([self.predict_proba(x) for x in X])
            probas = np.maximum(probas, 1e-20)  # avoid log(0)

            logloss = -(y_expected * np.log(probas) + (1 - y_expected) * np.log(1 - probas))
            total_loss = sum(logloss)

            error = probas - y_expected
            gradient_weights = np.dot(X.T, error)
            gradient_bias = np.sum(error)

            self.weights -= learning_rate * gradient_weights
            self.bias -= learning_rate * gradient_bias

            if i % 10 == 0:
                print(f"Epoch {i}/{epochs}, Loss: {total_loss}, Bias: {self.bias}, Weights: {self.weights}")