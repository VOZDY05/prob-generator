import streamlit as st
from generators.conditional import conditional_probability
from generators.normal import normal_distribution
from generators.binomial import binomial_distribution

PREMIUM_CODE = "PROBSTATS10"  
st.title("Probability & Statistics Exam Problem Generator")

st.markdown("Free version: 2 topics.\n\nPremium unlock: extra topics and harder problems.")

# --- Access code for premium ---
access_code = st.text_input("Premium access code (leave empty for free version):", type="password")
has_premium = access_code == PREMIUM_CODE

if has_premium:
    st.success("Premium features unlocked ✅")
else:
    st.info("Using free version. Enter access code to unlock premium topics.")

# --- Topic selection ---
if has_premium:
    topics = [
        "Conditional Probability",
        "Normal Distribution",
        "Binomial Distribution (Premium)"
    ]
else:
    topics = [
        "Conditional Probability",
        "Normal Distribution",
    ]

topic = st.selectbox("Choose a topic:", topics)

if st.button("Generate Problem"):
    if topic == "Conditional Probability":
        problem, steps, answer = conditional_probability()
    elif topic == "Normal Distribution":
        problem, steps, answer = normal_distribution()
    elif topic == "Binomial Distribution (Premium)":
        if not has_premium:
            st.error("This is a premium topic. Enter the access code above.")
            st.stop()
        problem, steps, answer = binomial_distribution()

    st.markdown("### Problem")
    st.write(problem)

    with st.expander("Step-by-step solution"):
        st.write(steps)

    st.markdown("### Final Answer")
    st.write(answer)

