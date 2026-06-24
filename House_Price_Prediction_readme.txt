# 🏠 AI House Price Predictor

A Machine Learning web application built with **Python**, **Scikit-Learn**, and **Streamlit** that predicts house prices based on various property features such as area, bedrooms, bathrooms, location, condition, and garage availability.

---

## 📸 Project Preview

This application provides:

* Modern Streamlit UI
* Real-estate themed background
* Machine Learning prediction model
* Interactive user inputs
* House price prediction in real time
* Model accuracy display

---

## 🚀 Features

✅ Predict house prices instantly

✅ Interactive and user-friendly interface

✅ Machine Learning powered prediction

✅ Label Encoding for categorical data

✅ Decision Tree Regression Model

✅ Professional Streamlit Dashboard

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* HTML
* CSS

---

## 📊 Dataset Features

| Feature   | Description                      |
| --------- | -------------------------------- |
| Area      | House area in square feet        |
| Bedrooms  | Number of bedrooms               |
| Bathrooms | Number of bathrooms              |
| Floors    | Number of floors                 |
| YearBuilt | Year the house was built         |
| Location  | Downtown, Rural, Suburban, Urban |
| Condition | Excellent, Good, Fair, Poor      |
| Garage    | Yes / No                         |

### Target Variable

**Price** → House Selling Price

---

## 🤖 Machine Learning Model

### Algorithm Used

Decision Tree Regressor

```python
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(random_state=23)
model.fit(x_train, y_train)
```

### Data Preprocessing

* Label Encoding
* Train-Test Split
* Feature Selection

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/house-price-predictor.git
```

Move into project directory:

```bash
cd house-price-predictor
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
house-price-predictor/
│
├── app.py
├── House Price Prediction Dataset.csv
├── requirements.txt
├── README.md
└── screenshots/
```

---

## 📈 Model Evaluation

The application evaluates performance using:

```python
from sklearn.metrics import r2_score
```

Metric Used:

* R² Score

---

## 💻 Example Prediction

Input:

* Area = 2000
* Bedrooms = 3
* Bathrooms = 2
* Floors = 2
* Year Built = 2015
* Location = Urban
* Condition = Good
* Garage = Yes

Output:

```text
Predicted House Price: ₹ 5,200,000
```

---

## 🌟 Future Improvements

* Random Forest Regressor
* XGBoost Regressor
* Feature Importance Visualization
* Data Analytics Dashboard
* Model Deployment on Streamlit Cloud
* User Authentication

---

## 👨‍💻 Author

Sai Romeo

Machine Learning Enthusiast

Python | SQL | Power BI | Streamlit

---

## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and share.

