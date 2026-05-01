import streamlit as st
import pandas as pd
from data import places

st.set_page_config(page_title="Travel Recommender", layout="wide")

st.title("🌍 Smart Travel Recommendation App")
st.markdown("Find your perfect destination based on your mood, budget & vibe ✨")

# Convert to DataFrame
df = pd.DataFrame(places)

# Sidebar filters
st.sidebar.header("🔍 Customize Your Trip")

country = st.sidebar.selectbox("Select Region", ["All", "India", "International"])
budget = st.sidebar.selectbox("Budget", ["All", "Low", "Medium", "High"])
season = st.sidebar.selectbox("Season", ["All", "Winter", "Summer", "Spring", "Monsoon"])
travel_type = st.sidebar.selectbox("Travel Type", ["All", "Solo", "Group", "Family", "Couple"])
interest = st.sidebar.selectbox("Interest", ["All", "Adventure", "Beach", "Spiritual", "City", "Nature", "Luxury", "Romantic", "Party"])
duration = st.sidebar.selectbox("Trip Duration", ["All", "2-3 days", "3-5 days", "4-6 days", "5-7 days"])

# Filtering logic
filtered = df.copy()

if country != "All":
    filtered = filtered[filtered["country"] == country]

if budget != "All":
    filtered = filtered[filtered["budget"] == budget]

if season != "All":
    filtered = filtered[filtered["season"].apply(lambda x: season in x)]

if travel_type != "All":
    filtered = filtered[filtered["travel"].apply(lambda x: travel_type in x)]

if interest != "All":
    filtered = filtered[filtered["type"].apply(lambda x: interest in x)]

if duration != "All":
    filtered = filtered[filtered["duration"] == duration]

# Results
st.subheader("✨ Recommended Destinations")

if filtered.empty:
    st.warning("No matches found 😢 Try changing filters!")
else:
    for i, row in filtered.iterrows():
        st.card = st.container()
        with st.card:
            st.markdown(f"### 📍 {row['name']}")
            st.write(f"🌍 Country: {row['country']}")
            st.write(f"💰 Budget: {row['budget']}")
            st.write(f"🌦️ Best Season: {', '.join(row['season'])}")
            st.write(f"👥 Suitable for: {', '.join(row['travel'])}")
            st.write(f"🎯 Type: {', '.join(row['type'])}")
            st.write(f"⏳ Duration: {row['duration']}")
            st.markdown("---")

# Extra feature: Random suggestion
st.sidebar.markdown("---")
if st.sidebar.button("🎲 Surprise Me"):
    random_place = df.sample(1).iloc[0]
    st.sidebar.success(f"Try visiting: {random_place['name']} 🌟")
