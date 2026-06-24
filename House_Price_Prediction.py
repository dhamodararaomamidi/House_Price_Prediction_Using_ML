import pandas as pd
import streamlit as st

from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# ====================================================
# PAGE CONFIG
# ====================================================

st.set_page_config(
    page_title="🏠 AI House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# ====================================================
# CUSTOM CSS
# ====================================================

st.markdown("""
<style>

/* Background Image */
.stApp{
    background-image:url("https://images.pexels.com/photos/186077/pexels-photo-186077.jpeg");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}

/* Dark Overlay */
.stApp::before{
    content:"";
    position:fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.35);
    z-index:-1;
}

/* Remove Streamlit Header */
[data-testid="stHeader"]{
    background:rgba(0,0,0,0);
}

/* Title */
.title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:white;
    text-shadow:3px 3px 15px black;
}

.subtitle{
    text-align:center;
    font-size:24px;
    color:white;
    margin-bottom:30px;
}

/* Labels */
label{
    color:white !important;
    font-weight:bold !important;
    font-size:18px !important;
}

/* Number Inputs */
[data-testid="stNumberInput"]{
    background:rgba(255,255,255,0.15);
    backdrop-filter:blur(10px);
    border-radius:15px;
    padding:5px;
}

/* Select Boxes */
[data-baseweb="select"]{
    background:rgba(255,255,255,0.15);
    backdrop-filter:blur(10px);
    border-radius:15px;
}

/* Predict Button */
.stButton > button{
    width:100%;
    height:60px;
    border:none;
    border-radius:15px;
    background:linear-gradient(135deg,#00c6ff,#0072ff);
    color:white;
    font-size:22px;
    font-weight:bold;
}

.stButton > button:hover{
    transform:scale(1.03);
    box-shadow:0px 0px 25px #00c6ff;
}

/* Prediction Box */
.prediction{
    background:linear-gradient(135deg,#00c6ff,#0072ff);
    color:white;
    text-align:center;
    padding:25px;
    border-radius:20px;
    font-size:32px;
    font-weight:bold;
    margin-top:20px;
}

/* Accuracy Box */
.accuracy{
    background:rgba(0,255,127,0.25);
    color:white;
    text-align:center;
    padding:15px;
    border-radius:15px;
    font-size:22px;
    margin-top:20px;
}

/* Footer */
.footer{
    text-align:center;
    color:white;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ====================================================
# TITLE
# ====================================================

st.markdown("""
<div class="title">
🏠 AI House Price Predictor
</div>

<div class="subtitle">
Predict House Prices Using Machine Learning
</div>
""", unsafe_allow_html=True)

# ====================================================
# LOAD DATA
# ====================================================

data = pd.read_csv("House Price Prediction Dataset.csv")
df = pd.DataFrame(data)

# ====================================================
# ENCODING
# ====================================================

le_Location = LabelEncoder()
le_Condition = LabelEncoder()
le_Garage = LabelEncoder()

df["Location"] = le_Location.fit_transform(df["Location"])
df["Condition"] = le_Condition.fit_transform(df["Condition"])
df["Garage"] = le_Garage.fit_transform(df["Garage"])

# ====================================================
# FEATURES & TARGET
# ====================================================

x = df.drop(["Id", "Price"], axis=1)
y = df["Price"]

# ====================================================
# TRAIN TEST SPLIT
# ====================================================

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.25,
    random_state=23
)

# ====================================================
# MODEL
# ====================================================

model = DecisionTreeRegressor(random_state=23)
model.fit(x_train, y_train)

# ====================================================
# INPUT SECTION
# ====================================================
col1, col2 = st.columns(2)
st.markdown("""
<h2 style='text-align:center;color:white;'>
📝 Enter House Details
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    area = st.number_input(
        "📐 Area (sq ft)",
        min_value=100,
        value=1000
    )

    bedrooms = st.number_input(
        "🛏 Bedrooms",
        min_value=1,
        value=2
    )

    bathrooms = st.number_input(
        "🚿 Bathrooms",
        min_value=1,
        value=2
    )

    floors = st.number_input(
        "🏢 Floors",
        min_value=1,
        value=1
    )

with col2:

    yearbuilt = st.number_input(
        "📅 Year Built",
        min_value=1900,
        max_value=2025,
        value=2015
    )

    location = st.selectbox(
        "📍 Location",
        ["Downtown", "Rural", "Suburban", "Urban"]
    )

    condition = st.selectbox(
        "⭐ Condition",
        ["Excellent", "Fair", "Good", "Poor"]
    )

    garage = st.selectbox(
        "🚗 Garage",
        ["No", "Yes"]
    )



# ====================================================
# PREDICTION
# ====================================================

if st.button("🔮 Predict House Price"):

    location_encoded = le_Location.transform([location])[0]
    condition_encoded = le_Condition.transform([condition])[0]
    garage_encoded = le_Garage.transform([garage])[0]

    new_data = [[
        area,
        bedrooms,
        bathrooms,
        floors,
        yearbuilt,
        location_encoded,
        condition_encoded,
        garage_encoded
    ]]

    prediction = model.predict(new_data)

    st.markdown(
        f"""
        <div class="prediction">
        💰 Predicted House Price<br><br>
        ₹ {prediction[0]:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

# ====================================================
# MODEL ACCURACY
# ====================================================

y_pred = model.predict(x_test)

score = r2_score(y_test, y_pred)

st.markdown(
    f"""
    <div class="accuracy">
    🎯 Model Accuracy (R² Score): <b>{score:.2f}</b>
    </div>
    """,
    unsafe_allow_html=True
)

# ====================================================
# FOOTER
# ====================================================

st.markdown("""
<div class="footer">

<hr>

<h2>👨‍💻 Developed by Sai Romeo</h2>

<h4>Machine Learning | Python | Streamlit</h4>

<p>🏠 AI House Price Prediction Project</p>

</div>
""", unsafe_allow_html=True)