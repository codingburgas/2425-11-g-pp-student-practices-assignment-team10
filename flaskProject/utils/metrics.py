import numpy as np

def compute_metrics(y_true, y_pred, y_proba, eps=1e-15):
    """
    Compute common binary classification metrics manually.

    Args:
        y_true (np.array): True labels (0 or 1).
        y_pred (np.array): Predicted labels (0 or 1).
        y_proba (np.array): Predicted probabilities (between 0 and 1).
        eps (float): Small epsilon for numerical stability in log loss.

    Returns:
        dict: Dictionary with accuracy, precision, recall, F1 score, and log loss.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    y_proba = np.clip(np.array(y_proba), eps, 1 - eps)  # avoid log(0)

    # Confusion matrix components
    TP = np.sum((y_true == 1) & (y_pred == 1))
    TN = np.sum((y_true == 0) & (y_pred == 0))
    FP = np.sum((y_true == 0) & (y_pred == 1))
    FN = np.sum((y_true == 1) & (y_pred == 0))

    # Metrics
    accuracy = (TP + TN) / len(y_true) if len(y_true) > 0 else 0
    precision = TP / (TP + FP) if (TP + FP) > 0 else 0
    recall = TP / (TP + FN) if (TP + FN) > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    log_loss = -np.mean(y_true * np.log(y_proba) + (1 - y_true) * np.log(1 - y_proba))

    return {
        "accuracy": round(accuracy * 100, 2),
        "precision": round(precision * 100, 2),
        "recall": round(recall * 100, 2),
        "f1_score": round(f1_score * 100, 2),
        "log_loss": round(log_loss, 4)
    }