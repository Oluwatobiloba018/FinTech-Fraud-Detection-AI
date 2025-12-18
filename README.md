# 🛡️ ShieldGuard AI: Real-Time Fraud Detection & Explainability

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange.svg)
![SHAP](https://img.shields.io/badge/Explainability-SHAP-brightgreen.svg)

## 📌 Project Overview
In the financial sector, **Fraud Detection** is a high-stakes challenge characterized by extreme class imbalance. In this project, I developed an end-to-end pipeline that identifies **93% of fraudulent transactions** within a dataset where only 0.17% of entries were actual fraud.

Beyond simple prediction, this system implements **Explainable AI (XAI)** to provide "Reason Codes" for every flagged transaction, ensuring compliance with financial transparency regulations.

---

## 🛠️ Technical Stack & Methodologies
* **Data Wrangling:** `Pandas`, `NumPy`, `RobustScaler` (to handle heavy financial outliers).
* **Scientific Research:** Implemented **Random Under-sampling** and evaluated **SMOTE** for class balance.
* **Model Tournament:** Compared `Logistic Regression`, `Random Forest`, and `XGBoost`.
* **Explainability:** Utilized `SHAP (SHapley Additive exPlanations)` to interpret high-risk features.

---

## 📈 Key Performance Metrics
Unlike generic ML projects, this system was optimized for **Recall** to minimize the financial impact of undetected fraud.

| Metric | Score | Business Context |
| :--- | :--- | :--- |
| **Recall (Class 1)** | **93%** | Successfully identified nearly all fraudulent attempts. |
| **Accuracy** | **97%** | High overall system reliability. |
| **Precision** | **5%** | Acceptable trade-off for low-cost verification pings. |

> **Research Insight:** The low precision is a strategic choice. In FinTech, the cost of a "False Positive" (sending a verification SMS) is negligible compared to the cost of a "False Negative" (undetected theft).

---

## 📊 Model Interpretability

### Feature Impact (SHAP Summary)
![SHAP Summary Plot](./models/shap_summary.png)

**Key Findings:**
Through SHAP (SHapley Additive exPlanations), we can see that features **V14, V12, and V10** are the most critical predictors. They show a strong negative correlation with the target; as these values decrease, the likelihood of a transaction being fraudulent increases significantly.
---

## 🚀 Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Oluwatobiloba018/FinTech-Fraud-Detection-AI.git](https://github.com/Oluwatobiloba018/FinTech-Fraud-Detection-AI.git)
