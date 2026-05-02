import streamlit as st
import anthropic
import json

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="WanderWise – AI Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --gold: #C9A84C;
    --deep: #0D1117;
    --card: #161B22;
    --border: #30363D;
    --text: #E6EDF3;
    --muted: #8B949E;
    --accent: #238636;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--deep);
    color: var(--text);
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #0D1117 0%, #161B22 50%, #0D1117 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    margin-bottom: 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(201,168,76,0.12) 0%, transparent 70%);
}
.hero h1 {
    font-size: 3rem;
    color: var(--gold);
    margin: 0;
    letter-spacing: -0.5px;
}
.hero p {
    color: var(--muted);
    font-size: 1.1rem;
    margin-top: 0.5rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0D1117 !important;
    border-right: 1px solid var(--border);
}
section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

/* Inputs */
.stSelectbox > div > div,
.stMultiSelect > div > div,
.stSlider > div,
.stTextInput > div > div {
    background-color: var(--card) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 8px !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, var(--gold), #A07830);
    color: #0D1117;
    font-family: 'DM Sans', sans-serif;
    font-weight: 600;
    font-size: 1rem;
    border: none;
    border-radius: 10px;
    padding: 0.75rem 2rem;
    width: 100%;
    transition: all 0.2s ease;
    letter-spacing: 0.3px;
}
.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(201,168,76,0.3);
}

/* Result card */
.result-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2rem;
    margin-top: 1.5rem;
    line-height: 1.8;
}
.result-card h2 {
    color: var(--gold);
    font-size: 1.6rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--border);
    padding-bottom: 0.75rem;
}

/* Tag pills */
.tag {
    display: inline-block;
    background: rgba(201,168,76,0.12);
    border: 1px solid rgba(201,168,76,0.3);
    color: var(--gold);
    border-radius: 20px;
    padding: 0.2rem 0.75rem;
    font-size: 0.8rem;
    font-weight: 500;
    margin: 0.2rem;
}

/* Divider */
hr { border-color: var(--border) !important; }

/* Sidebar section label */
.sidebar-label {
    color: var(--gold);
    font-family: 'Playfair Display', serif;
    font-size: 1.05rem;
    font-weight: 600;
    margin: 1.2rem 0 0.4rem;
}

/* Info box */
.info-box {
    background: rgba(35,134,54,0.1);
    border: 1px solid rgba(35,134,54,0.3);
    border-radius: 10px;
    padding: 1rem 1.2rem;
    font-size: 0.9rem;
    color: #7EE787;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


# ── Hero Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🌍 WanderWise</h1>
    <p>Your AI-powered travel companion — personalised itineraries in seconds</p>
</div>
""", unsafe_allow_html=True)


# ── Sidebar – Preferences ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ✈️ Trip Preferences")
    st.markdown("---")

    # 1. Domestic / International
    st.markdown('<div class="sidebar-label">🌐 Trip Scope</div>', unsafe_allow_html=True)
    trip_scope = st.radio(
        "Select trip type",
        ["🏠 Domestic (India)", "🌍 International"],
        label_visibility="collapsed",
    )
    is_domestic = "Domestic" in trip_scope

    if is_domestic:
        origin_state = st.selectbox(
            "Your home state",
            ["Uttar Pradesh", "Delhi", "Maharashtra", "Karnataka", "Tamil Nadu",
             "Rajasthan", "Gujarat", "West Bengal", "Telangana", "Kerala",
             "Madhya Pradesh", "Punjab", "Himachal Pradesh", "Uttarakhand", "Other"],
        )
    else:
        origin_country = st.selectbox(
            "Travelling from",
            ["India", "USA", "UK", "UAE", "Germany", "Australia", "Canada",
             "Singapore", "France", "Japan", "Other"],
        )

    st.markdown("---")

    # 2. Budget
    st.markdown('<div class="sidebar-label">💰 Budget (INR)</div>', unsafe_allow_html=True)
    budget_range = st.select_slider(
        "Select your total budget",
        options=["< ₹10K", "₹10K–₹25K", "₹25K–₹50K", "₹50K–₹1L", "₹1L–₹2L", "> ₹2L"],
        value="₹25K–₹50K",
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 3. Season / Month
    st.markdown('<div class="sidebar-label">📅 Travel Season</div>', unsafe_allow_html=True)
    season = st.selectbox(
        "When are you planning to go?",
        ["🌸 Spring (Mar–May)", "☀️ Summer (Jun–Aug)",
         "🍂 Autumn (Sep–Nov)", "❄️ Winter (Dec–Feb)"],
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 4. Trip Duration
    st.markdown('<div class="sidebar-label">🗓️ Trip Duration</div>', unsafe_allow_html=True)
    duration = st.slider("Number of days", 1, 30, 7)

    st.markdown("---")

    # 5. Trip Type
    st.markdown('<div class="sidebar-label">🎯 Trip Type</div>', unsafe_allow_html=True)
    trip_types = st.multiselect(
        "Select interests (multi-select)",
        ["🏔️ Adventure", "🌿 Nature & Wildlife", "🕌 Religious & Spiritual",
         "🏖️ Beach & Coastal", "🏛️ Heritage & Culture", "🍽️ Food & Culinary",
         "🎭 Art & Entertainment", "🛍️ Shopping", "💆 Wellness & Spa",
         "📸 Photography", "🎓 Educational", "🌆 City & Urban"],
        default=["🌿 Nature & Wildlife"],
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 6. Travel Group
    st.markdown('<div class="sidebar-label">👥 Travelling As</div>', unsafe_allow_html=True)
    travel_group = st.radio(
        "Group type",
        ["🧍 Solo", "👫 Couple", "👨‍👩‍👧‍👦 Family", "👯 Friends Group", "💼 Business"],
        label_visibility="collapsed",
    )

    # Group size (if not solo)
    if "Solo" not in travel_group:
        group_size = st.number_input("Group size", min_value=2, max_value=50, value=4)
    else:
        group_size = 1

    st.markdown("---")

    # 7. Accommodation Preference
    st.markdown('<div class="sidebar-label">🏨 Accommodation</div>', unsafe_allow_html=True)
    accommodation = st.selectbox(
        "Preferred stay",
        ["🏕️ Camping / Hostel", "🏠 Budget Hotel / Guesthouse",
         "🏩 3-Star Hotel", "🌟 4–5 Star Hotel", "🏡 Homestay / Airbnb",
         "🧘 Resort / Retreat", "No preference"],
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 8. Physical Fitness
    st.markdown('<div class="sidebar-label">💪 Physical Fitness Level</div>', unsafe_allow_html=True)
    fitness = st.select_slider(
        "Your fitness level",
        options=["Sedentary", "Light", "Moderate", "Active", "Very Active"],
        value="Moderate",
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 9. Special Requirements
    st.markdown('<div class="sidebar-label">⚙️ Special Requirements</div>', unsafe_allow_html=True)
    special = st.multiselect(
        "Any special needs?",
        ["♿ Wheelchair Accessible", "👶 Kid Friendly", "🐾 Pet Friendly",
         "🌱 Vegan / Vegetarian Food", "🍖 Non-veg Food Required",
         "🕌 Halal Food", "🚫 Avoid Crowded Places", "📵 Off-the-grid"],
        label_visibility="collapsed",
    )

    st.markdown("---")

    # 10. Extra Preferences (free text)
    st.markdown('<div class="sidebar-label">📝 Anything Else?</div>', unsafe_allow_html=True)
    extra = st.text_area(
        "Additional preferences or notes",
        placeholder="E.g. I love waterfalls, hate long drives, prefer hill stations...",
        label_visibility="collapsed",
        height=90,
    )

    st.markdown("---")
    generate_btn = st.button("🔮 Find My Perfect Trip", use_container_width=True)


# ── Main Panel ────────────────────────────────────────────────────────────────
col1, col2 = st.columns([2, 1])

with col1:
    if not generate_btn:
        st.markdown("""
        <div style='text-align:center; padding: 3rem 1rem; color: #8B949E;'>
            <div style='font-size:4rem;'>🧳</div>
            <h3 style='color:#8B949E; font-family: DM Sans, sans-serif; font-weight:400;'>
                Fill in your preferences on the left and click <br>
                <span style='color:#C9A84C;'>Find My Perfect Trip</span>
            </h3>
            <p style='font-size:0.9rem;'>Powered by Claude AI • Personalised just for you</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    if not generate_btn:
        st.markdown("""
        <div style='background:#161B22; border:1px solid #30363D; border-radius:12px; padding:1.5rem;'>
            <h3 style='color:#C9A84C; font-family: Playfair Display, serif; margin-top:0;'>Why WanderWise?</h3>
            <ul style='color:#8B949E; line-height:2; list-style:none; padding:0; margin:0;'>
                <li>✅ Budget-aware suggestions</li>
                <li>✅ Season-optimised picks</li>
                <li>✅ Domestic & International</li>
                <li>✅ Group-tailored itineraries</li>
                <li>✅ Accommodation advice</li>
                <li>✅ Day-by-day planning</li>
                <li>✅ Safety & visa tips</li>
                <li>✅ Hidden gems included</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


# ── AI Generation ─────────────────────────────────────────────────────────────
if generate_btn:
    if not trip_types:
        st.warning("⚠️ Please select at least one trip type from the sidebar.")
        st.stop()

    # Build summary tags
    origin = origin_state if is_domestic else origin_country
    scope_label = "Domestic (India)" if is_domestic else "International"
    tags_html = "".join([
        f'<span class="tag">{scope_label}</span>',
        f'<span class="tag">{budget_range}</span>',
        f'<span class="tag">{season.split("(")[0].strip()}</span>',
        f'<span class="tag">{duration} Days</span>',
        f'<span class="tag">{travel_group}</span>',
        *[f'<span class="tag">{t}</span>' for t in trip_types],
    ])

    st.markdown(f"""
    <div style='margin-bottom:0.5rem;'>
        <strong style='color:#8B949E; font-size:0.85rem;'>YOUR FILTERS</strong><br/>
        {tags_html}
    </div>
    """, unsafe_allow_html=True)

    # Build prompt
    clean_types = ", ".join([t.split(" ", 1)[1] for t in trip_types])
    clean_season = season.split("(")[0].strip().replace("🌸","").replace("☀️","").replace("🍂","").replace("❄️","").strip()
    clean_group = travel_group.split(" ", 1)[1] if " " in travel_group else travel_group
    clean_accommodation = accommodation.split(" ", 1)[1] if " " in accommodation else accommodation
    special_str = ", ".join([s.split(" ", 1)[1] for s in special]) if special else "None"

    prompt = f"""You are WanderWise, an expert AI travel planner with deep knowledge of both Indian and international destinations.

A traveller has provided the following preferences:
- Trip Scope: {scope_label}
- Origin / Home: {origin}
- Budget: {budget_range} (total for all {group_size} traveller(s))
- Season: {clean_season}
- Duration: {duration} days
- Travel Group: {clean_group} ({group_size} person(s))
- Trip Type / Interests: {clean_types}
- Accommodation Preference: {clean_accommodation}
- Physical Fitness Level: {fitness}
- Special Requirements: {special_str}
- Additional Notes: {extra if extra else 'None'}

Your task:
1. **Top 3 Destination Recommendations** – For each destination provide:
   - Destination name and why it perfectly matches this traveller's profile
   - Best time to visit (confirm or caveat based on the selected season)
   - Estimated per-person cost breakdown (transport, stay, food, activities)
   - Top 5 must-do experiences/activities aligned with their trip type
   - One hidden gem or local secret most tourists miss
   - Any visa / permit requirement (for international or restricted areas)
   - Safety tips relevant to this group type

2. **Sample {duration}-Day Itinerary** for the TOP recommended destination – a day-by-day plan with morning / afternoon / evening slots.

3. **Packing Essentials** – a short, context-specific list for the season and trip type.

4. **Pro Budget Tips** – 3–4 smart money-saving or value-maximising tips specific to this trip profile.

Format your response beautifully using markdown. Use emojis tastefully. Be specific, enthusiastic, and genuinely helpful. Avoid generic advice — make this feel personalised."""

    with st.spinner("🌐 WanderWise is crafting your perfect itinerary..."):
        try:
            client = anthropic.Anthropic()

            result_placeholder = st.empty()
            full_text = ""

            with client.messages.stream(
                model="claude-sonnet-4-20250514",
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}],
            ) as stream:
                for text in stream.text_stream:
                    full_text += text
                    result_placeholder.markdown(
                        f'<div class="result-card">{full_text}▌</div>',
                        unsafe_allow_html=True,
                    )

            # Final render without cursor
            result_placeholder.markdown(
                f'<div class="result-card">{full_text}</div>',
                unsafe_allow_html=True,
            )

            st.markdown("""
            <div class="info-box">
                ✅ Itinerary generated! Scroll up to explore your personalised travel plan.
                Tip: Adjust any filter on the left and regenerate for a different suggestion.
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
            st.info("Make sure your ANTHROPIC_API_KEY is set correctly.")
