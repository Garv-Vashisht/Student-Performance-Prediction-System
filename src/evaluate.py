import matplotlib
matplotlib.use('Agg')  # 🔥 FIX Tkinter crash

import matplotlib.pyplot as plt
import os
import numpy as np

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.inspection import permutation_importance


def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)

    print("\n📊 Classification Report:\n")
    print(classification_report(y_test, y_pred))

    os.makedirs("images", exist_ok=True)

    # -----------------------------
    # 1. CONFUSION MATRIX
    # -----------------------------
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])

    plt.figure()
    plt.imshow(cm)
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.xticks([0, 1], ["Fail", "Pass"])
    plt.yticks([0, 1], ["Fail", "Pass"])

    for i in range(len(cm)):
        for j in range(len(cm[0])):
            plt.text(j, i, cm[i, j], ha='center', va='center')

    plt.colorbar()
    plt.tight_layout()
    plt.savefig("images/confusion_matrix.png")
    plt.close()

    # -----------------------------
    # 2. PREDICTION DISTRIBUTION
    # -----------------------------
    unique, counts = np.unique(y_pred, return_counts=True)

    labels = ["Fail", "Pass"]
    values = [0, 0]

    for u, c in zip(unique, counts):
        values[int(u)] = c

    plt.figure()
    plt.bar(labels, values)
    plt.title("Prediction Distribution")
    plt.xlabel("Class")
    plt.ylabel("Count")

    for i, v in enumerate(values):
        plt.text(i, v + 1, str(v), ha='center')

    plt.tight_layout()
    plt.savefig("images/prediction_distribution.png")
    plt.close()

    # -----------------------------
    # 3. FEATURE IMPORTANCE (PERMUTATION)
    # -----------------------------
    try:
        if len(np.unique(y_test)) < 2:
            print("⚠ Skipping feature importance (only one class)")
        else:
            print("Calculating permutation importance...")

            result = permutation_importance(
                model,
                X_test,
                y_test,
                n_repeats=5,
                random_state=42,
                n_jobs=1  # 🔥 fix threading issue
            )

            importances = result.importances_mean
            feature_names = X_test.columns

            indices = np.argsort(importances)

            plt.figure()
            plt.barh(feature_names[indices], importances[indices])
            plt.xlabel("Permutation Importance")
            plt.title("Feature Importance")
            plt.tight_layout()
            plt.savefig("images/feature_importance.png")
            plt.close()

            print("✅ Feature importance plotted")

    except Exception as e:
        print("Feature importance error:", e)

    print("✅ All 3 images saved in /images")