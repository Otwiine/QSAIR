from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Create preprocessing and SVM pipline
svm_pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(
        kernel='rbf',
        C=10.0,
        gamma='scale',
        probability=True,
        class_weight='balanced'
        ))
    ])

# Train the model
svm_pipeline.fit(X_train, y_train)

# Evaluate performance
y_pred = svm_pipeline.predict(X_test)
print(classification_report(
    y_test, y_pred,
    target_names=crop_names
))