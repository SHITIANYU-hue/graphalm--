import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load and Merge Dataset (as done previously)
# Load Transactions Dataset
transactions_features = pd.read_csv('path/to/txs_features.csv')
transactions_classes = pd.read_csv('path/to/txs_classes.csv')

# Step 2: Merge Transaction Features with Classes
def merge_transaction_data(features_data, classes_data):
    return features_data.merge(classes_data, on='tx_id', how='inner')

# Merge transactions with their class labels (1 = illicit, 2 = licit)
merged_transactions = merge_transaction_data(transactions_features, transactions_classes)

# Step 3: LLM Context and Feature Selection (use previous context)
# Assuming we already generated context as described before, we select features:
def select_features_based_on_context(context, data):
    if "transaction size" in context.lower():
        print("Prioritizing transaction size...")
        return data[['total_value', 'class']]  # Class will be the target variable
    elif "wallet activity" in context.lower():
        print("Prioritizing wallet interactions...")
        return data[['wallet_id', 'class']]  # This needs wallet interaction features
    else:
        # Use default features for now
        return data[['total_value', 'class']]

# Step 4: Feature Selection Based on LLM Context
context = "Prioritize transaction size for detecting suspicious behavior."  # Example context
selected_data = select_features_based_on_context(context, merged_transactions)

# Step 5: Train-Test Split
X = selected_data.drop(columns=['class'])  # Features (transaction size, etc.)
y = selected_data['class']  # Target variable (1 = illicit, 2 = licit)

# Convert labels: 1 (illicit) = 0, 2 (licit) = 1 for binary classification
y = y.replace({1: 0, 2: 1})

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Train Classifier (Random Forest)
classifier = RandomForestClassifier(n_estimators=100, random_state=42)
classifier.fit(X_train, y_train)

# Step 7: Make Predictions
y_pred = classifier.predict(X_test)

# Step 8: Evaluate the Classifier
accuracy = accuracy_score(y_test, y_pred)
print(f"Classifier Accuracy: {accuracy * 100:.2f}%")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Illicit', 'Licit']))

# Step 9: Feature Importance (Optional)
importances = classifier.feature_importances_
for feature, importance in zip(X.columns, importances):
    print(f"Feature: {feature}, Importance: {importance:.4f}")
