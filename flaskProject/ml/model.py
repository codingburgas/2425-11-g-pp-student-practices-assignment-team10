# flaskProject/ml/model.py
import numpy as np
from numpy import random

class LogisticRegression:
    def __init__(self, n_features, bias=0, threshold=0.5):
        self.weights = np.array([random.random() for _ in range(n_features)])
        self.bias = bias
        self.threshold = threshold

    def weighted_sum(self, X):
        x = np.array(X)
        return x.dot(self.weights) + self.bias

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def predict_proba(self, X):
        return self.sigmoid(self.weighted_sum(X))

    def predict_class(self, X):
        return 0 if self.predict_proba(X) < self.threshold else 1

    def train(self, dataset, epochs, learning_rate):
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
