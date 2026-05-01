import streamlit as st
import pandas as pd

# Sample dataset (you can replace this with a CSV from GitHub)
data = pd.DataFrame({
    "place": ["Varanasi", "Goa", "Paris", "Tokyo", "Rishikesh", "New York"],
    "country": ["India", "India", "France", "Japan", "India", "USA"],
    "type": ["Religious", "Vacation", "Vacation", "Vacation", "Religious", "Vacation"],
    "budget": ["Low", "Medium", "High", "High", "Low", "High"],
    "season": ["Winter", "Summer", "Spring", "Autumn", "Summer", "Winter"],
    "group_type": ["Solo", "Group", "Group", "Solo", "Solo", "Group"],
    "trip_scope": ["Domestic", "Domestic", "International", "International", "Domestic", "International"]
})

st.title("Travel Suggestion App 🌍")
st.write("Get personalized travel suggestions based on your preferences!")

# User inputs
budget = st.selectbox("Select your budget:", ["Low", "Medium", "High"])
season = st.selectbox("Preferred season:", ["Summer", "Winter", "Spring", "Autumn"])
group_type = st.radio("Are you traveling solo or with a group?", ["Solo", "Group"])
trip_scope = st.radio("Choose trip type:", ["Domestic", "International"])
place_type = st.selectbox("Type of place:", ["Religious", "Vacation"])

# Filter dataset
filtered = data[
    (data["budget"] == budget) &
    (data["season"] == season) &
    (data["group_type"] == group_type) &
    (data["trip_scope"] == trip_scope) &
    (data["type"] == place_type)
]

# Show results
if not filtered.empty:
    st.subheader("Suggested Places for You:")
    for _, row in filtered.iterrows():
        st.write(f"- **{row['place']}** ({row['country']}) - {row['type']} trip")
else:
    st.warning("No matching places found. Try adjusting your preferences!")

# GitHub integration idea
st.markdown("""
You can store your dataset in a GitHub repo and load it directly:
```python
url = "https://raw.githubusercontent.com/<username>/<repo>/main/destinations.csv"
data = pd.read_csv(url)
