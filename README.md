# 🎓 Student Placement Prediction

## 🚀 Project Overview
This project uses machine learning to predict whether a student will get placed, based on academic and skill-related features like CGPA, aptitude score, internships, workshops, and more. The final model also produces a **Placement Readiness Score** (0–100) and gives personalized feedback.

---

## 🧠 Motivation
- Helps students identify strengths and weaknesses.
- Used by college placement cells to enhance training strategies.
- Offers data-driven insights to improve employability.

---

## 📂 Dataset & Features
**Dataset:** Contains student records with the following features:

| Feature              | Description                                   |
|----------------------|-----------------------------------------------|
| CGPA                 | Cumulative Grade Point Average (0–10)         |
| Internships          | Number of internships completed              |
| Projects             | Number of academic/industry projects         |
| Workshops            | Number of workshops or certifications taken  |
| AptitudeScore        | Score out of 100 on aptitude test            |
| SoftSkills           | Rating from 0.0 to 5.0 on soft skills        |
| Extracurricular      | Yes / No (attended extracurricular activities)|
| Training             | Yes / No (attended placement training)       |
| SSC_Marks            | 10th-grade percentage                        |
| HSC_Marks            | 12th-grade percentage                        |
| PlacementStatus      | Target label: Placed / Not Placed            |

---

## 🔍 Exploratory Data Analysis (EDA)
- Checked for missing values and outliers using box plots, z-score, and IQR methods.
- Visualized data distributions and relationships with bar plots, histograms, and correlation heatmaps.
- Found CGPA and aptitude to be strong predictors.

---

## 🧹 Data Preprocessing & Cleaning
- Handled missing or inconsistent entries.
- Encoded categorical features (`Yes/No`, placement status) to numeric.
- Split data into training and testing sets (e.g., 80:20 ratio).
- Scaled numeric features when necessary.

---

## 🤖 Model Training
Tested 3 models:

1. **Logistic Regression** – Fast, interpretable baseline.
2. **Random Forest Classifier** – Handles non-linear relationships well.
3. **XGBoost Classifier** – Powerful gradient boosting model.

---

## 🔧 Hyperparameter Tuning
Used `RandomizedSearchCV` to optimize:

- Random Forest: `n_estimators`, `max_depth`, `min_samples_split`, etc.
- XGBoost: `n_estimators`, `learning_rate`, `max_depth`, etc.

---

## 🏆 Model Comparison
| Model                    | Accuracy (Before Tuning) | Accuracy (After Tuning) |
|--------------------------|--------------------------|--------------------------|
| Logistic Regression      | ~78%                     | —                        |
| Random Forest            | ~80%                     | ~82%                     |
| XGBoost                  | ~81%                     | **79%** (final)          |

**Note:** Though Logistic Regression started strong, XGBoost outperformed it after tuning.

---

## 📦 Deployment
- Built a **Streamlit** web app (`app.py`) for interactive use.
- Users can input their details, get placement predictions, readiness score, and improvement suggestions.
- Provides a **download button** for the trained model.

---

## 🔮 Future Scope
- Incorporate more features: soft skill assessments, extracurricular hours.
- Add ensemble methods (stacking/blending).
- Deploy on **Streamlit Community Cloud** for global access.
- Integrate real-time data and dashboards for student placement tracking.

---

