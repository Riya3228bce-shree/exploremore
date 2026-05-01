import streamlit as st
import json
import random
from dataclasses import dataclass
from typing import Optional

# ─── Page Config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="WanderWise – Smart Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;600&display=swap');

:root {
    --bg:       #0d1117;
    --surface:  #161b22;
    --border:   #30363d;
    --gold:     #d4a843;
    --gold2:    #f0c060;
    --teal:     #29c7ac;
    --text:     #e6edf3;
    --muted:    #8b949e;
    --card-bg:  #1c2230;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg) !important;
    color: var(--text) !important;
}

h1, h2, h3 { font-family: 'Playfair Display', serif !important; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* Cards */
.card {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: transform .2s, border-color .2s;
}
.card:hover { transform: translateY(-4px); border-color: var(--gold); }

.badge {
    display:inline-block;
    background: rgba(212,168,67,.15);
    color: var(--gold2);
    border: 1px solid var(--gold);
    border-radius: 20px;
    padding: 2px 12px;
    font-size: .78rem;
    margin: 2px;
}

.hero-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 3.2rem !important;
    font-weight: 900 !important;
    background: linear-gradient(135deg, var(--gold), var(--teal));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1.1 !important;
}

.hero-sub {
    color: var(--muted);
    font-size: 1.1rem;
    margin-top: .4rem;
}

.tag-group { margin: .5rem 0; }

.metric-box {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem 1.2rem;
    text-align: center;
}
.metric-label { font-size: .78rem; color: var(--muted); }
.metric-value { font-size: 1.6rem; font-weight: 700; color: var(--gold2); }

/* Streamlit overrides */
div[data-testid="stSelectbox"] > div, 
div[data-testid="stMultiSelect"] > div,
div[data-testid="stSlider"] > div {
    background: var(--surface) !important;
}

.stButton > button {
    background: linear-gradient(135deg, var(--gold), #b8860b) !important;
    color: #000 !important;
    font-weight: 700 !important;
    border: none !important;
    border-radius: 8px !important;
    padding: .6rem 2rem !important;
    font-size: 1rem !important;
    letter-spacing: .5px !important;
    transition: opacity .2s !important;
}
.stButton > button:hover { opacity: .85 !important; }

.stExpander { background: var(--card-bg) !important; border: 1px solid var(--border) !important; border-radius: 12px !important; }
.stInfo { background: rgba(41,199,172,.1) !important; border-left: 3px solid var(--teal) !important; }

hr { border-color: var(--border) !important; }

/* hide default header/footer */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ─── Data ────────────────────────────────────────────────────────────────────
DESTINATIONS = [
    {
        "name": "Bali, Indonesia", "country": "Indonesia", "continent": "Asia",
        "budget_level": "budget", "min_budget_usd": 30, "max_budget_usd": 80,
        "seasons": ["summer", "spring"], "trip_type": ["beach", "culture", "adventure"],
        "group_types": ["solo", "couple", "group"],
        "duration_days": (5, 14), "language": "Bahasa Indonesian", "visa_on_arrival": True,
        "highlights": ["Ubud Rice Terraces", "Tanah Lot Temple", "Mount Batur Hike", "Seminyak Beach"],
        "food_rating": 4.7, "safety_rating": 4.2, "fun_rating": 4.8,
        "emoji": "🌴", "currency": "IDR",
        "tip": "Visit Ubud for culture, Seminyak for nightlife, Canggu for surfers."
    },
    {
        "name": "Paris, France", "country": "France", "continent": "Europe",
        "budget_level": "luxury", "min_budget_usd": 150, "max_budget_usd": 500,
        "seasons": ["spring", "autumn"], "trip_type": ["culture", "food", "romance"],
        "group_types": ["couple", "solo", "family"],
        "duration_days": (4, 10), "language": "French", "visa_on_arrival": False,
        "highlights": ["Eiffel Tower", "Louvre Museum", "Montmartre", "Seine River Cruise"],
        "food_rating": 4.9, "safety_rating": 4.0, "fun_rating": 4.6,
        "emoji": "🗼", "currency": "EUR",
        "tip": "Buy a Paris Museum Pass for big savings. Best in April–June."
    },
    {
        "name": "Thailand – Bangkok & Chiang Mai", "country": "Thailand", "continent": "Asia",
        "budget_level": "budget", "min_budget_usd": 25, "max_budget_usd": 70,
        "seasons": ["winter", "autumn"], "trip_type": ["culture", "food", "adventure", "beach"],
        "group_types": ["solo", "couple", "group", "backpacker"],
        "duration_days": (7, 21), "language": "Thai", "visa_on_arrival": True,
        "highlights": ["Grand Palace", "Doi Inthanon", "Floating Markets", "Phi Phi Islands"],
        "food_rating": 4.9, "safety_rating": 4.0, "fun_rating": 4.8,
        "emoji": "🏯", "currency": "THB",
        "tip": "Avoid April (Songkran floods cities). Night markets are unmissable."
    },
    {
        "name": "New York City, USA", "country": "USA", "continent": "North America",
        "budget_level": "luxury", "min_budget_usd": 200, "max_budget_usd": 600,
        "seasons": ["spring", "autumn", "winter"], "trip_type": ["city", "culture", "food", "shopping"],
        "group_types": ["solo", "couple", "family", "group"],
        "duration_days": (4, 10), "language": "English", "visa_on_arrival": False,
        "highlights": ["Central Park", "Times Square", "Met Museum", "Brooklyn Bridge"],
        "food_rating": 4.8, "safety_rating": 3.9, "fun_rating": 4.7,
        "emoji": "🗽", "currency": "USD",
        "tip": "Get a 7-day MetroCard. Visit museums on their free evenings."
    },
    {
        "name": "Rajasthan, India", "country": "India", "continent": "Asia",
        "budget_level": "budget", "min_budget_usd": 15, "max_budget_usd": 50,
        "seasons": ["winter", "autumn"], "trip_type": ["culture", "heritage", "adventure"],
        "group_types": ["solo", "couple", "family", "group"],
        "duration_days": (7, 15), "language": "Hindi", "visa_on_arrival": True,
        "highlights": ["Jaipur Pink City", "Jaisalmer Desert", "Udaipur Lake Palace", "Ranthambore Tiger Reserve"],
        "food_rating": 4.6, "safety_rating": 3.8, "fun_rating": 4.6,
        "emoji": "🏰", "currency": "INR",
        "tip": "October–March is ideal. Hire a local guide in Jaipur for hidden gems."
    },
    {
        "name": "Kyoto, Japan", "country": "Japan", "continent": "Asia",
        "budget_level": "mid-range", "min_budget_usd": 80, "max_budget_usd": 200,
        "seasons": ["spring", "autumn"], "trip_type": ["culture", "heritage", "food"],
        "group_types": ["solo", "couple", "family"],
        "duration_days": (5, 12), "language": "Japanese", "visa_on_arrival": False,
        "highlights": ["Arashiyama Bamboo Grove", "Fushimi Inari", "Gion District", "Nishiki Market"],
        "food_rating": 5.0, "safety_rating": 5.0, "fun_rating": 4.8,
        "emoji": "⛩️", "currency": "JPY",
        "tip": "Book cherry blossom season (late March–April) months in advance!"
    },
    {
        "name": "Santorini, Greece", "country": "Greece", "continent": "Europe",
        "budget_level": "luxury", "min_budget_usd": 200, "max_budget_usd": 700,
        "seasons": ["summer", "spring"], "trip_type": ["beach", "romance", "food"],
        "group_types": ["couple", "solo"],
        "duration_days": (4, 10), "language": "Greek", "visa_on_arrival": False,
        "highlights": ["Oia Sunset", "Caldera Views", "Red Beach", "Akrotiri Archaeological Site"],
        "food_rating": 4.5, "safety_rating": 4.8, "fun_rating": 4.7,
        "emoji": "🏛️", "currency": "EUR",
        "tip": "Stay in Oia for sunsets. Visit in May or September to avoid peak crowds."
    },
    {
        "name": "Patagonia, Argentina/Chile", "country": "Argentina/Chile", "continent": "South America",
        "budget_level": "mid-range", "min_budget_usd": 60, "max_budget_usd": 180,
        "seasons": ["summer", "spring"], "trip_type": ["adventure", "nature"],
        "group_types": ["solo", "group", "backpacker"],
        "duration_days": (10, 21), "language": "Spanish", "visa_on_arrival": True,
        "highlights": ["Torres del Paine", "Perito Moreno Glacier", "Los Glaciares NP", "Beagle Channel"],
        "food_rating": 4.3, "safety_rating": 4.5, "fun_rating": 4.9,
        "emoji": "🏔️", "currency": "ARS/CLP",
        "tip": "Weather is very unpredictable—layer up even in summer."
    },
    {
        "name": "Marrakech, Morocco", "country": "Morocco", "continent": "Africa",
        "budget_level": "budget", "min_budget_usd": 30, "max_budget_usd": 90,
        "seasons": ["spring", "autumn", "winter"], "trip_type": ["culture", "food", "heritage"],
        "group_types": ["solo", "couple", "group"],
        "duration_days": (4, 10), "language": "Arabic/French", "visa_on_arrival": True,
        "highlights": ["Djemaa el-Fna", "Majorelle Garden", "Medina Souks", "Atlas Mountains Day Trip"],
        "food_rating": 4.7, "safety_rating": 4.0, "fun_rating": 4.6,
        "emoji": "🕌", "currency": "MAD",
        "tip": "Bargain in the souks—always start at 40% of the asking price."
    },
    {
        "name": "Maldives", "country": "Maldives", "continent": "Asia",
        "budget_level": "luxury", "min_budget_usd": 300, "max_budget_usd": 1500,
        "seasons": ["winter", "spring"], "trip_type": ["beach", "romance", "relaxation"],
        "group_types": ["couple", "family"],
        "duration_days": (5, 14), "language": "Dhivehi", "visa_on_arrival": True,
        "highlights": ["Overwater Bungalows", "Snorkeling with Manta Rays", "Bioluminescent Beach", "Whale Sharks"],
        "food_rating": 4.4, "safety_rating": 4.9, "fun_rating": 4.8,
        "emoji": "🏝️", "currency": "MVR",
        "tip": "Book guesthouses on local islands for a 70% cost saving vs resorts."
    },
    {
        "name": "Cape Town, South Africa", "country": "South Africa", "continent": "Africa",
        "budget_level": "mid-range", "min_budget_usd": 50, "max_budget_usd": 150,
        "seasons": ["summer", "spring", "autumn"], "trip_type": ["adventure", "nature", "city"],
        "group_types": ["solo", "couple", "group"],
        "duration_days": (7, 14), "language": "English", "visa_on_arrival": False,
        "highlights": ["Table Mountain", "Cape of Good Hope", "Boulders Beach Penguins", "Winelands"],
        "food_rating": 4.5, "safety_rating": 3.5, "fun_rating": 4.7,
        "emoji": "🦁", "currency": "ZAR",
        "tip": "Don't drive at night outside tourist areas. Rent a car for the Garden Route."
    },
    {
        "name": "Lisbon, Portugal", "country": "Portugal", "continent": "Europe",
        "budget_level": "mid-range", "min_budget_usd": 60, "max_budget_usd": 150,
        "seasons": ["spring", "autumn", "summer"], "trip_type": ["city", "culture", "food"],
        "group_types": ["solo", "couple", "group"],
        "duration_days": (4, 8), "language": "Portuguese", "visa_on_arrival": False,
        "highlights": ["Belém Tower", "Alfama District", "Sintra Day Trip", "Pastéis de Belém"],
        "food_rating": 4.7, "safety_rating": 4.7, "fun_rating": 4.5,
        "emoji": "🎵", "currency": "EUR",
        "tip": "Take tram 28 for a scenic city tour. Best pastéis de nata at Fábrica da Pastéis."
    },
]

SEASONS = {
    "winter": "❄️ Winter (Dec–Feb)",
    "spring": "🌸 Spring (Mar–May)",
    "summer": "☀️ Summer (Jun–Aug)",
    "autumn": "🍂 Autumn (Sep–Nov)",
}

TRIP_TYPES = ["beach", "culture", "adventure", "food", "romance", "heritage", "nature", "city", "shopping", "relaxation"]
GROUP_TYPES = ["solo", "couple", "family", "group", "backpacker"]
BUDGET_LEVELS = {"budget": (0, 60), "mid-range": (60, 180), "luxury": (180, 10000)}


# ─── Helpers ─────────────────────────────────────────────────────────────────
def stars(n: float, max_n: int = 5) -> str:
    filled = round(n)
    return "★" * filled + "☆" * (max_n - filled)


def match_destinations(daily_budget, seasons, trip_types, group_type, duration, continents):
    results = []
    for d in DESTINATIONS:
        score = 0

        # Budget
        if d["min_budget_usd"] <= daily_budget <= d["max_budget_usd"] * 1.5:
            budget_match = 1 - abs(daily_budget - (d["min_budget_usd"] + d["max_budget_usd"]) / 2) / max(daily_budget, 1)
            score += max(0, budget_match) * 30

        # Season
        season_overlap = len(set(seasons) & set(d["seasons"]))
        score += season_overlap * 20

        # Trip type
        type_overlap = len(set(trip_types) & set(d["trip_type"]))
        score += type_overlap * 15

        # Group type
        if group_type in d["group_types"]:
            score += 20

        # Duration
        d_min, d_max = d["duration_days"]
        if d_min <= duration <= d_max:
            score += 15
        elif abs(duration - d_min) <= 2 or abs(duration - d_max) <= 2:
            score += 8

        # Continent filter
        if continents and d["continent"] not in continents:
            continue

        if score > 0:
            results.append((d, score))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


def render_destination_card(dest, score, rank):
    highlights_html = "".join(f'<span class="badge">✦ {h}</span>' for h in dest["highlights"][:4])
    types_html = "".join(f'<span class="badge" style="background:rgba(41,199,172,.12);color:#29c7ac;border-color:#29c7ac">{t}</span>' for t in dest["trip_type"])

    budget_text = f"${dest['min_budget_usd']}–${dest['max_budget_usd']}/day"

    st.markdown(f"""
    <div class="card">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:.6rem">
            <div>
                <div style="font-size:1.5rem; font-weight:800; font-family:'Playfair Display',serif">
                    {dest['emoji']} &nbsp;{dest['name']}
                </div>
                <div style="color:var(--muted); font-size:.88rem; margin-top:.15rem">
                    {dest['continent']} · {dest['language']} · {dest['currency']}
                    {'&nbsp;·&nbsp;<span style="color:#29c7ac">✔ Visa on Arrival</span>' if dest['visa_on_arrival'] else ''}
                </div>
            </div>
            <div style="text-align:right">
                <div style="color:var(--gold2);font-weight:700;font-size:1.1rem">#{rank}</div>
                <div style="color:var(--muted);font-size:.8rem">Match: {int(score)}%</div>
            </div>
        </div>
        <div class="tag-group">{types_html}</div>
        <div style="color:var(--muted);font-size:.9rem;margin:.5rem 0;font-style:italic">💡 {dest['tip']}</div>
        <div class="tag-group">{highlights_html}</div>
        <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin-top:1rem">
            <div class="metric-box">
                <div class="metric-label">🍽 Food</div>
                <div class="metric-value" style="font-size:1rem">{stars(dest['food_rating'])}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">🛡 Safety</div>
                <div class="metric-value" style="font-size:1rem">{stars(dest['safety_rating'])}</div>
            </div>
            <div class="metric-box">
                <div class="metric-label">🎉 Fun</div>
                <div class="metric-value" style="font-size:1rem">{stars(dest['fun_rating'])}</div>
            </div>
        </div>
        <div style="margin-top:1rem;padding-top:.8rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center">
            <span style="color:var(--gold2);font-weight:600">💰 {budget_text}</span>
            <span style="color:var(--muted);font-size:.85rem">🗓 {dest['duration_days'][0]}–{dest['duration_days'][1]} days recommended</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── App ──────────────────────────────────────────────────────────────────────
# Hero
st.markdown('<div class="hero-title">WanderWise</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Smart travel recommendations tailored to your budget, season & travel style.</div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ─── Sidebar ─────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎛️ Your Travel Profile")
    st.markdown("---")

    daily_budget = st.slider(
        "💵 Daily Budget (USD per person)",
        min_value=10, max_value=800, value=80, step=10,
        help="Includes accommodation, food & local transport"
    )

    total_days = st.slider(
        "🗓️ Trip Duration (days)",
        min_value=2, max_value=30, value=10
    )

    st.markdown(f"**Estimated Total Budget: ${daily_budget * total_days:,}**")

    st.markdown("---")

    selected_seasons = st.multiselect(
        "🌤️ Travelling Season",
        options=list(SEASONS.keys()),
        format_func=lambda s: SEASONS[s],
        default=["winter"],
    )

    group_type = st.selectbox(
        "👥 Travel Group",
        options=GROUP_TYPES,
        format_func=lambda g: {
            "solo": "🧍 Solo Explorer",
            "couple": "💑 Couple",
            "family": "👨‍👩‍👧 Family",
            "group": "👫 Group of Friends",
            "backpacker": "🎒 Backpacker",
        }.get(g, g)
    )

    st.markdown("---")

    trip_types = st.multiselect(
        "🎯 Trip Interests",
        options=TRIP_TYPES,
        default=["culture", "food"],
        help="Select one or more interests"
    )

    st.markdown("---")

    all_continents = sorted(set(d["continent"] for d in DESTINATIONS))
    continents = st.multiselect(
        "🌍 Preferred Region",
        options=all_continents,
        default=[],
        help="Leave empty to search all regions"
    )

    st.markdown("---")

    sort_by = st.selectbox(
        "📊 Sort Results By",
        ["Match Score", "Food Rating", "Safety Rating", "Fun Rating", "Budget (Low→High)"]
    )

    find_btn = st.button("🔍 Find My Destinations", use_container_width=True)

# ─── Main Content ─────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🌟 Recommendations", "📊 Compare", "ℹ️ About"])

with tab1:
    if find_btn or "results" in st.session_state:
        if find_btn:
            if not selected_seasons:
                st.warning("Please select at least one travel season.")
                st.stop()
            if not trip_types:
                st.warning("Please select at least one trip interest.")
                st.stop()

            results = match_destinations(
                daily_budget=daily_budget,
                seasons=selected_seasons,
                trip_types=trip_types,
                group_type=group_type,
                duration=total_days,
                continents=continents,
            )
            # Sort
            if sort_by == "Food Rating":
                results.sort(key=lambda x: x[0]["food_rating"], reverse=True)
            elif sort_by == "Safety Rating":
                results.sort(key=lambda x: x[0]["safety_rating"], reverse=True)
            elif sort_by == "Fun Rating":
                results.sort(key=lambda x: x[0]["fun_rating"], reverse=True)
            elif sort_by == "Budget (Low→High)":
                results.sort(key=lambda x: x[0]["min_budget_usd"])

            st.session_state["results"] = results
            st.session_state["params"] = {
                "daily_budget": daily_budget,
                "total_days": total_days,
                "seasons": selected_seasons,
                "group_type": group_type,
                "trip_types": trip_types,
            }

        results = st.session_state.get("results", [])
        params = st.session_state.get("params", {})

        if not results:
            st.info("😕 No destinations matched your filters. Try widening your budget or interests.")
        else:
            st.markdown(f"### ✨ {len(results)} Destinations Found for You")
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f'<div class="metric-box"><div class="metric-label">Daily Budget</div><div class="metric-value">${params.get("daily_budget","–")}</div></div>', unsafe_allow_html=True)
            with c2:
                st.markdown(f'<div class="metric-box"><div class="metric-label">Total Days</div><div class="metric-value">{params.get("total_days","–")}</div></div>', unsafe_allow_html=True)
            with c3:
                st.markdown(f'<div class="metric-box"><div class="metric-label">Group Type</div><div class="metric-value" style="font-size:1rem">{params.get("group_type","–").title()}</div></div>', unsafe_allow_html=True)
            with c4:
                st.markdown(f'<div class="metric-box"><div class="metric-label">Destinations</div><div class="metric-value">{len(results)}</div></div>', unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)

            for i, (dest, score) in enumerate(results[:8], 1):
                render_destination_card(dest, min(score, 100), i)

    else:
        st.markdown("""
        <div class="card" style="text-align:center; padding:3rem">
            <div style="font-size:3rem">🌍</div>
            <h3 style="font-family:'Playfair Display',serif;margin:.5rem 0">Set Your Travel Profile</h3>
            <p style="color:var(--muted)">Use the sidebar to configure your budget, season, group type and interests,<br>then click <strong>Find My Destinations</strong>.</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### 📊 Destination Comparison")
    results = st.session_state.get("results", [])
    if not results:
        st.info("Run a search first to compare destinations.")
    else:
        top = [d for d, _ in results[:6]]
        names = [d["name"] for d in top]
        selected_compare = st.multiselect("Select destinations to compare:", names, default=names[:3])
        compare_dests = [d for d in top if d["name"] in selected_compare]

        if compare_dests:
            cols = st.columns(len(compare_dests))
            metrics = [
                ("🍽 Food", "food_rating"),
                ("🛡 Safety", "safety_rating"),
                ("🎉 Fun", "fun_rating"),
                ("💰 Min $/day", "min_budget_usd"),
            ]
            for col, dest in zip(cols, compare_dests):
                with col:
                    st.markdown(f"**{dest['emoji']} {dest['name'].split(',')[0]}**")
                    for label, key in metrics:
                        val = dest[key]
                        if key in ("food_rating", "safety_rating", "fun_rating"):
                            st.metric(label, stars(val))
                        else:
                            st.metric(label, f"${val}")

with tab3:
    st.markdown("""
    ### ℹ️ About WanderWise
    
    **WanderWise** is a smart travel planner that recommends destinations based on:
    
    - 💵 **Daily Budget** – Filters places within your spending range
    - 🌤️ **Season** – Matches destinations best visited in your travel window
    - 👥 **Group Type** – Solo, couple, family, group, or backpacker preferences
    - 🎯 **Interests** – Beach, culture, adventure, food, romance, and more
    - 🌍 **Region** – Filter by continent
    - 🗓️ **Duration** – Optimises for your available days
    
    Each destination includes ratings for food, safety, and fun, along with insider tips, visa info, and local currency.
    
    ---
    
    **Tech Stack:** Python · Streamlit · GitHub
    
    > Built with ❤️ for curious travellers everywhere.
    """)
