import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="BizTwin Mesh AI",
    layout="wide"
)

# ----------------------------
# SIMPLE LOGIN (ACCEPTS ANYTHING)
# ----------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.markdown("""
    <div style="text-align:center; margin-top:120px;">
        <h1 style="font-size:60px; color:white; text-shadow:0 0 20px #00f5ff;">
            BizTwin Mesh AI
        </h1>
        <p style="color:#bbbbbb; font-size:20px;">
            Secure Access Portal
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            # Accept anything
            st.session_state.logged_in = True
            st.rerun()

    st.stop()

# ----------------------------
# SHINY VERTICAL MODULE SELECTION
# ----------------------------

if "selected_module" not in st.session_state:
    st.session_state.selected_module = None

if st.session_state.logged_in and st.session_state.selected_module is None:
    

    st.markdown("""
    <style>

    .module-card {
        padding: 35px;
        border-radius: 25px;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        color: white;
        margin-bottom: 25px;
        transition: 0.4s;
        box-shadow: 0 0 25px rgba(0,255,255,0.3);
    }

    .module-card:hover {
        transform: scale(1.05);
        box-shadow: 0 0 60px rgba(0,255,255,0.7);
    }

    .sales {
        background: linear-gradient(135deg,#ff416c,#ff4b2b);
    }

    .inventory {
        background: linear-gradient(135deg,#11998e,#38ef7d);
    }

    .finance {
        background: linear-gradient(135deg,#396afc,#2948ff);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin-top:80px;">
        <h1 style="font-size:55px; color:white;">
            Choose Business Module
        </h1>
        <p style="color:#bbbbbb; font-size:20px;">
            Select the intelligence engine you want to activate
        </p>
    </div>
    """, unsafe_allow_html=True)

    col_left, col_center, col_right = st.columns([1,2,1])

    with col_center:

        st.markdown('<div class="module-card sales">📊 Sales Intelligence</div>', unsafe_allow_html=True)
        if st.button("Activate Sales", key="sales_btn", use_container_width=True):
            st.session_state.selected_module = "Sales"
            st.rerun()

        st.markdown('<div class="module-card inventory">📦 Inventory Intelligence</div>', unsafe_allow_html=True)
        if st.button("Activate Inventory", key="inventory_btn", use_container_width=True):
            st.session_state.selected_module = "Inventory"
            st.rerun()

        st.markdown('<div class="module-card finance">💰 Financial Intelligence</div>', unsafe_allow_html=True)
        if st.button("Activate Finance", key="finance_btn", use_container_width=True):
            st.session_state.selected_module = "Financial"
            st.rerun()

    st.stop()
    if st.session_state.selected_module != "Sales":
    st.stop()





st.markdown("""
<style>

.hero-container {
    text-align: center;
    margin-top: 60px;
    margin-bottom: 50px;
}

.hero-title {
    font-size: 82px;
    font-weight: 900;
    letter-spacing: -2px;
    background: linear-gradient(90deg, #00f5ff, #6a11cb, #ff4b2b, #00f5ff);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradientMove 6s ease infinite;
}

.hero-subtitle {
    font-size: 22px;
    color: #b5b5b5;
    margin-top: 15px;
    font-weight: 400;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-container">
    <div class="hero-title">BizTwin Mesh AI</div>
    <div class="hero-subtitle">
        Autonomous Decision Intelligence Platform for Small Businesses<br>
        Simulate. Optimize. Decide with Confidence.
    </div>
</div>
""", unsafe_allow_html=True)


# ----------------------------
# Advanced Custom Styling
# ----------------------------
st.markdown("""
<style>

/* Animated Gradient Background */
body {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #000000);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title Glow */
h1 {
    text-shadow: 0 0 20px #00f5ff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111 !important;
}

/* KPI Card Styling */
.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    transition: 0.3s;
}

.metric-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(0,255,255,0.3);
}

/* Metric Number */
.metric-card h2 {
    font-size: 30px;
    color: #00f5ff;
    margin-bottom: 10px;
}

/* Metric Label */
.metric-card p {
    font-size: 18px;
    color: #ffffff;
}

/* Executive Summary Box */
.summary-box {
    background: rgba(0,0,0,0.4);
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #00f5ff;
    box-shadow: 0 0 20px rgba(0,255,255,0.3);
}

</style>
""", unsafe_allow_html=True)


st.markdown("---")
st.header("Decision Inputs")

col1, col2, col3, col4 = st.columns(4)

# ---------- Selling Price ----------
with col1:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#ff416c,#ff4b2b);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:20px;
        font-weight:bold;
        margin-bottom:15px;">
        Selling Price
    </div>
    """, unsafe_allow_html=True)

    price = st.number_input(
        "", min_value=80, max_value=150, value=100,
        key="price_input"
    )

# ---------- Cost Price ----------
with col2:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#11998e,#38ef7d);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:20px;
        font-weight:bold;
        margin-bottom:15px;">
        Cost Price
    </div>
    """, unsafe_allow_html=True)

    cost = st.number_input(
        "", min_value=40, max_value=100, value=60,
        key="cost_input"
    )

# ---------- Season Factor ----------
with col3:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#396afc,#2948ff);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:20px;
        font-weight:bold;
        margin-bottom:15px;">
        Season Factor
    </div>
    """, unsafe_allow_html=True)

    season = st.number_input(
        "", min_value=0.8, max_value=1.3, value=1.0,
        step=0.01,
        key="season_input"
    )

# ---------- Competitor Price ----------
with col4:
    st.markdown("""
    <div style="
        background: linear-gradient(135deg,#f7971e,#ffd200);
        padding:25px;
        border-radius:20px;
        text-align:center;
        color:white;
        font-size:20px;
        font-weight:bold;
        margin-bottom:15px;">
        Competitor Price
    </div>
    """, unsafe_allow_html=True)

    competitor = st.number_input(
        "", min_value=80, max_value=150, value=100,
        key="competitor_input"
    )



# ----------------------------
# Business Logic
# ----------------------------
base_demand = 1000
demand = base_demand * season - (price - competitor) * 5
demand = max(demand, 0)

profit = (price - cost) * demand

risk = "Low"
if price > competitor + 10:
    risk = "High"
elif price > competitor:
    risk = "Moderate"

recommended_price = competitor + 5

# ----------------------------
# KPI Section
# ----------------------------
st.markdown("---")
st.header("Key Decision Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.markdown(f"""
<div class="metric-card">
    <h2>{int(demand)} units</h2>
    <p>Predicted Demand</p>
</div>
""", unsafe_allow_html=True)

col2.markdown(f"""
<div class="metric-card">
    <h2>₹{int(profit):,}</h2>
    <p>Expected Profit</p>
</div>
""", unsafe_allow_html=True)

col3.markdown(f"""
<div class="metric-card">
    <h2>{risk}</h2>
    <p>Risk Level</p>
</div>
""", unsafe_allow_html=True)

col4.markdown(f"""
<div class="metric-card">
    <h2>₹{recommended_price}</h2>
    <p>Recommended Price</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Price vs Profit Graph
# ----------------------------
# ----------------------------
# Price vs Profit Graph (Shiny Version)
# ----------------------------
st.markdown("---")
st.header("Price vs Profit Analysis")

col_left, col_center, col_right = st.columns([1,2,1])

with col_center:

    prices = np.arange(80, 150)
    profits = []

    for p in prices:
        simulated_demand = base_demand * season - (p - competitor) * 5
        simulated_demand = max(simulated_demand, 0)
        simulated_profit = (p - cost) * simulated_demand
        profits.append(simulated_profit)

    profits = np.array(profits)

    max_profit_index = np.argmax(profits)
    optimal_price = prices[max_profit_index]
    max_profit = profits[max_profit_index]

    fig, ax = plt.subplots(figsize=(7,4))

    # Dark background
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')

    # Neon glow effect (draw line multiple times)
    for i in range(6, 0, -1):
        ax.plot(prices, profits, color='#00f5ff', linewidth=i, alpha=0.08)

    # Main bright line
    ax.plot(prices, profits, color='#00f5ff', linewidth=3)

    # Glowing optimal point
    for i in range(10, 0, -1):
        ax.scatter(optimal_price, max_profit, color='red', s=50+i*15, alpha=0.05)

    ax.scatter(optimal_price, max_profit, color='red', s=120)

    # Styling
    ax.set_xlabel("Price", color='white')
    ax.set_ylabel("Profit", color='white')
    ax.set_title("Profit Optimization Curve", color='white')

    ax.tick_params(colors='white')
    ax.grid(color='#444444', linestyle='--', linewidth=0.5, alpha=0.3)

    # Remove top & right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig)


# ----------------------------
# Executive Summary
# ----------------------------
st.markdown("---")
st.header("Executive Summary")

st.markdown(f"""
<div class="summary-box">
Based on current inputs:

• Selling Price: ₹{price}  
• Cost Price: ₹{cost}  
• Season Factor: {season}  
• Competitor Price: ₹{competitor}  

The system predicts <b>{int(demand)} units</b> of demand and an estimated profit of 
<b>₹{int(profit):,}</b>.  

Risk level is assessed as <b>{risk}</b>.  
Optimal pricing based on simulation suggests <b>₹{optimal_price}</b>.
</div>
""", unsafe_allow_html=True)