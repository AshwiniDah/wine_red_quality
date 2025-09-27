import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate(pred_file, gt_file):
    # Load predicted and ground truth files
    preds = pd.read_csv('/content/DS_Macro_Wine/predictions.csv')
    gt = pd.read_csv('/content/DS_Macro_Wine/Test_groundtruth/wine_test_gt.csv')

    # Check schema
    assert "PredictedQuality" in preds.columns, "Missing PredictedQuality column"
    assert "quality" in gt.columns, "Ground truth missing quality column"

    # Align lengths
    assert len(preds) == len(gt), "Mismatch in rows between predictions and ground truth"

    # Compute accuracy
    acc = accuracy_score(gt["quality"], preds["PredictedQuality"])
    print(f"✅ Accuracy: {acc:.4f}\n")

    # Confusion Matrix
    cm = confusion_matrix(gt["quality"], preds["PredictedQuality"])
    print("🔹 Confusion Matrix:")
    print(cm, "\n")

    # Classification Report
    cr = classification_report(gt["quality"], preds["PredictedQuality"], digits=4)
    print("🔹 Classification Report:")
    print(cr)

    return acc

if __name__ == "__main__":
    # Example usage
    # Replace with actual file paths before running
    evaluate("DS_Macro_Wine/predictions.csv", "DS_Macro_Wine/Test_groundtruth/wine_test_gt.csv")
