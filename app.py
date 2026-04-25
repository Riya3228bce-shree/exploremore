import streamlit as st
import pandas as pd
import datetime

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Smart Travel Planner", page_icon="🌍", layout="wide")

# -------------------------------
# SAMPLE DATASET
# -------------------------------
places_data = [
    {"place": "Manali", "type": "Nature", "best_months": ["April", "May", "June"], "budget": "Medium", "companion": ["Friends", "Family"]},
    {"place": "Goa", "type": "Beach", "best_months": ["November", "December"], "budget": "Medium", "companion": ["Friends", "Couple"]},
    {"place": "Varanasi", "type": "Religious", "best_months": ["October", "November"], "budget": "Low", "companion": ["Family", "Solo"]},
    {"place": "Jaipur", "type": "City", "best_months": ["November", "December"], "budget": "Low", "companion": ["Family", "Friends"]},
    {"place": "Leh Ladakh", "type": "Adventure", "best_months": ["May", "June"], "budget": "High", "companion": ["Friends"]},
    {"place": "Rishikesh", "type": "Adventure", "best_months": ["March", "April"], "budget": "Low", "companion": ["Friends", "Solo"]},
]

df_places = pd.DataFrame(places_data)

# -------------------------------
# SIDEBAR NAVIGATION
# -------------------------------
st.sidebar.title("🌍 Travel App")
page = st.sidebar.radio("Navigate", ["Home", "Explore", "Plan Trip", "Tracker", "Stats"])

# -------------------------------
# HOME PAGE
# -------------------------------
if page == "Home":
    st.title("🌍 Smart Travel Planner")
    st.write("Plan your trips based on your interest, budget, and companions!")

    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e")

# -------------------------------
# EXPLORE PAGE
# -------------------------------
elif page == "Explore":
    st.title("🔍 Explore Places")

    interest = st.selectbox("Select Interest", df_places["type"].unique())
    month = st.selectbox("Select Month", ["January","February","March","April","May","June","July","August","September","October","November","December"])
    budget = st.selectbox("Budget", ["Low", "Medium", "High"])
    companion = st.selectbox("Companion", ["Solo", "Friends", "Family", "Couple"])

    filtered = df_places[
        (df_places["type"] == interest) &
        (df_places["budget"] == budget)
    ]

    results = []
    for _, row in filtered.iterrows():
        if month in row["best_months"] and companion in row["companion"]:
            results.append(row["place"])

    if st.button("Find Places"):
        if results:
            st.success("Recommended Places:")
            for place in results:
                st.write(f"📍 {place}")
        else:
            st.warning("No exact match found. Try changing filters.")

# -------------------------------
# PLAN TRIP PAGE
# -------------------------------
elif page == "Plan Trip":
    st.title("🧳 Plan Your Trip")

    destination = st.selectbox("Choose Destination", df_places["place"])
    days = st.slider("Number of Days", 1, 10)
    budget = st.selectbox("Your Budget", ["Low", "Medium", "High"])

    if st.button("Generate Plan"):
        if budget == "Low":
            cost = days * 1500
        elif budget == "Medium":
            cost = days * 3000
        else:
            cost = days * 6000

        st.success(f"Estimated Trip Cost: ₹{cost}")

        st.write("### Suggested Plan")
        for i in range(1, days + 1):
            st.write(f"Day {i}: Explore {destination}")

# -------------------------------
# TRACKER PAGE
# -------------------------------
elif page == "Tracker":
    st.title("📍 Travel Tracker")

    name = st.text_input("Place Visited")
    date = st.date_input("Date", datetime.date.today())
    rating = st.slider("Rating", 1, 5)

    if st.button("Save Trip"):
        new_data = pd.DataFrame([[name, date, rating]], columns=["Place", "Date", "Rating"])
        try:
            old_data = pd.read_csv("trips.csv")
            updated = pd.concat([old_data, new_data])
        except:
            updated = new_data

        updated.to_csv("trips.csv", index=False)
        st.success("Trip Saved!")

    try:
        data = pd.read_csv("trips.csv")
        st.write("### Your Trips")
        st.dataframe(data)
    except:
        st.info("No trips recorded yet.")

# -------------------------------
# STATS PAGE
# -------------------------------
elif page == "Stats":
    st.title("📊 Travel Stats")

    try:
        data = pd.read_csv("trips.csv")

        st.write("### Total Trips:", len(data))
        st.write("### Average Rating:", round(data["Rating"].mean(), 2))

        st.bar_chart(data["Rating"].value_counts())

    except:
        st.warning("No data available yet.")
