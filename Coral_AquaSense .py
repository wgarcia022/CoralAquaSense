import streamlit as st
import openai
import requests

# Set up OpenAI API key
openai.api_key = st.secrets["Api_key_here"]

st.set_page_config(page_title="Coral AquaSense", layout="centered")
st.title("💧 Coral AquaSense: Smart Water Advisor")

st.markdown("""
Meet **Tim**, a San Jose urban gardener & café owner facing water challenges. 
Coral AquaSense helps you optimize your water usage with AI-driven insights.
""")

# --- User Inputs ---
st.subheader("🌦️ Get Personalized Water-Saving Advice")
city = st.text_input("Enter your city (e.g., San Jose)", "San Jose")
weather = st.selectbox("Select current weather condition", ["Sunny", "Cloudy", "Rainy", "Very Hot", "Cool"])
usage_area = st.multiselect("Select your water use areas", ["Rooftop Garden", "Cafe Kitchen", "Restroom", "Cleaning"])
custom_notes = st.text_area("Any specific water concerns today?")

if st.button("🧠 Generate Smart Advice"):
    with st.spinner("Thinking with AI magic..."):
        prompt = f"""
        You are an AI assistant helping a small business owner in {city} manage water usage.
        Today's weather is: {weather}.
        Areas of water use: {', '.join(usage_area)}.
        Notes: {custom_notes}.

        Provide personalized water-saving recommendations based on this input. Include:
        - Irrigation guidance for rooftop gardens (if applicable)
        - Suggestions for reducing water usage in selected areas
        - Context-aware insights related to weather
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a practical sustainability advisor focused on water efficiency."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=400
        )

        ai_output = response['choices'][0]['message']['content']
        st.success("💡 Here are your personalized water-saving tips:")
        st.write(ai_output)

# --- Optional Dashboard Snapshot ---
st.markdown("---")
st.subheader("📊 San Jose Water Snapshot")

col1, col2 = st.columns(2)
with col1:
    st.metric("Reservoir Capacity", "67%", "+2% from last week")
    st.metric("Avg Daily Use (Household)", "140 gal", "↓ 5 gal")

with col2:
    st.metric("Forecasted Rainfall", "0.1 in", "Low")
    st.metric("Community Savings Goal", "12%", "On Track")

st.caption("Data is aggregated from local utility dashboards and weather services.")
