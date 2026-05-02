import streamlit as st
import random

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="WanderWise – AI Travel Planner",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# CUSTOM CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=DM+Sans:wght@300;400;500&display=swap');

:root {
    --gold: #C9A84C; --deep: #0D1117; --card: #161B22;
    --border: #30363D; --text: #E6EDF3; --muted: #8B949E;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--deep); color: var(--text);
}
h1,h2,h3 { font-family: 'Playfair Display', serif; }

.hero {
    background: linear-gradient(135deg,#0D1117 0%,#161B22 50%,#0D1117 100%);
    border: 1px solid var(--border); border-radius:16px;
    padding:2.5rem 2rem; margin-bottom:2rem;
    text-align:center; position:relative; overflow:hidden;
}
.hero::before {
    content:''; position:absolute; inset:0;
    background:radial-gradient(ellipse at 50% 0%, rgba(201,168,76,0.12) 0%, transparent 70%);
}
.hero h1 { font-size:3rem; color:var(--gold); margin:0; }
.hero p  { color:var(--muted); font-size:1.1rem; margin-top:0.5rem; }

section[data-testid="stSidebar"] {
    background-color:#0D1117 !important;
    border-right:1px solid var(--border);
}

.stButton>button {
    background:linear-gradient(135deg,var(--gold),#A07830);
    color:#0D1117; font-family:'DM Sans',sans-serif; font-weight:600;
    font-size:1rem; border:none; border-radius:10px;
    padding:0.75rem 2rem; width:100%; transition:all 0.2s ease;
}
.stButton>button:hover {
    transform:translateY(-2px);
    box-shadow:0 8px 24px rgba(201,168,76,0.3);
}

.dest-card {
    background:var(--card); border:1px solid var(--border);
    border-radius:14px; padding:1.8rem; margin-bottom:1.5rem;
}
.dest-card h2 { color:var(--gold); font-size:1.5rem; margin:0 0 0.3rem; }

.badge {
    display:inline-block; background:rgba(201,168,76,0.12);
    border:1px solid rgba(201,168,76,0.3); color:var(--gold);
    border-radius:20px; padding:0.2rem 0.75rem;
    font-size:0.78rem; font-weight:500; margin:0.2rem;
}
.badge-blue { background:rgba(56,139,253,0.12); border-color:rgba(56,139,253,0.3); color:#79C0FF; }
.badge-green { background:rgba(35,134,54,0.12); border-color:rgba(35,134,54,0.3); color:#7EE787; }

.itinerary-day {
    background:#0D1117; border-left:3px solid var(--gold);
    border-radius:0 8px 8px 0; padding:1rem 1.2rem; margin-bottom:0.8rem;
}
.itinerary-day h4 { color:var(--gold); margin:0 0 0.5rem; font-family:'DM Sans',sans-serif; font-weight:600; }
.itinerary-day p  { color:var(--text); margin:0.2rem 0; font-size:0.92rem; line-height:1.6; }

.tip-box {
    background:rgba(35,134,54,0.08); border:1px solid rgba(35,134,54,0.25);
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.6rem;
    font-size:0.9rem; color:#7EE787;
}
.warn-box {
    background:rgba(210,153,34,0.08); border:1px solid rgba(210,153,34,0.25);
    border-radius:10px; padding:1rem 1.2rem; margin-bottom:0.6rem;
    font-size:0.9rem; color:#E3B341;
}

.section-header {
    color:var(--gold); font-family:'Playfair Display',serif;
    font-size:1.3rem; margin:1.5rem 0 0.8rem;
    border-bottom:1px solid var(--border); padding-bottom:0.4rem;
}
.sidebar-label {
    color:var(--gold); font-family:'Playfair Display',serif;
    font-size:1.05rem; font-weight:600; margin:1.2rem 0 0.4rem;
}
hr { border-color:var(--border) !important; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# DESTINATION DATABASE
# ─────────────────────────────────────────────────────────────────────────────
DESTINATIONS = {
    "Manali, Himachal Pradesh": {
        "scope": "domestic",
        "types": ["Adventure", "Nature & Wildlife", "Photography"],
        "seasons": ["Spring", "Summer"],
        "budget_min": "₹10K–₹25K",
        "fitness": ["Moderate", "Active", "Very Active"],
        "group_fit": ["Solo", "Couple", "Friends Group"],
        "emoji": "🏔️",
        "state_tags": ["Himachal Pradesh", "Punjab", "Delhi", "Uttar Pradesh", "Uttarakhand"],
        "description": "Snow-capped peaks, river valleys, and adrenaline-packed trails make Manali India's adventure capital.",
        "highlights": ["Solang Valley snow activities", "Rohtang Pass drive", "Paragliding at Solang", "Old Manali cafés & culture", "Hadimba Devi Temple"],
        "hidden_gem": "Kheerganga hot springs — a 12 km trek through forests rewarded with natural thermal pools under the stars.",
        "cost_breakdown": {"Transport (return)": "₹1,500–₹4,000", "Stay/night": "₹600–₹2,500", "Food/day": "₹400–₹800", "Activities": "₹500–₹2,000"},
        "permit": "Inner Line Permit required for Spiti Valley extension. No permit for Manali itself.",
        "safety": "Carry warm layers even in summer — mountain weather changes fast. Acclimatise before treks.",
        "packing": ["Thermal innerwear", "Waterproof jacket", "Trekking boots", "Sunscreen SPF 50+", "AMS tablets"],
        "itinerary_template": [
            ("Day 1", "🚌 Travel from Delhi/Chandigarh (Volvo overnight)", "🏨 Check-in & explore Mall Road", "🍽️ Café Rishi dinner & bonfire"),
            ("Day 2", "🏔️ Solang Valley — zorbing & snow activities", "🪂 Paragliding session (₹500)", "🔥 Bonfire at campsite"),
            ("Day 3", "🛣️ Rohtang Pass drive (permit req., book online)", "📸 Snow field photography", "🍜 Hot Maggi at roadside stalls"),
            ("Day 4", "🚶 Old Manali walk & Hadimba Temple", "🛍️ Tibetan market — jewellery & woolens", "🎸 Live music at Drifter's Inn"),
            ("Day 5", "🌊 Beas River white-water rafting", "🧘 Vashisht hot springs soak", "🌅 Sunset from Naggar Castle"),
        ],
        "budget_tips": [
            "Book Volvo buses (₹1,200–₹1,800) from Delhi well in advance — much cheaper than flights.",
            "Stay in Old Manali guesthouses instead of Mall Road hotels — 50% cheaper and more scenic.",
            "Eat at local dhabas for authentic Himachali food under ₹100 per meal.",
            "Negotiate activity packages — combo (rafting + paragliding) saves ₹300–₹500 vs. individual booking.",
        ],
    },

    "Goa": {
        "scope": "domestic",
        "types": ["Beach & Coastal", "Food & Culinary", "Art & Entertainment", "Shopping"],
        "seasons": ["Autumn", "Winter"],
        "budget_min": "₹10K–₹25K",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Solo", "Couple", "Friends Group"],
        "emoji": "🏖️",
        "state_tags": ["Maharashtra", "Karnataka", "Telangana", "Goa", "Other"],
        "description": "Sun, sea, spice, and soul — Goa's golden beaches and Portuguese heritage are endlessly inviting.",
        "highlights": ["North Goa beach parties (Baga, Anjuna)", "South Goa serenity (Palolem, Agonda)", "Dudhsagar Waterfall day trip", "Old Goa baroque churches (UNESCO)", "Spice plantation tour"],
        "hidden_gem": "Butterfly Beach — accessible only by boat from Palolem, pristine white sand with almost zero crowds.",
        "cost_breakdown": {"Transport (return)": "₹2,000–₹6,000", "Stay/night": "₹700–₹3,500", "Food/day": "₹400–₹1,200", "Activities": "₹200–₹1,500"},
        "permit": "No permit required for Indian citizens.",
        "safety": "Avoid swimming at unguarded beaches; strong currents near rocky headlands. Use reef shoes.",
        "packing": ["Sunscreen SPF 50+", "Light cottons & swimwear", "Waterproof sandals", "Mosquito repellent", "Cash (some beach shacks card-unfriendly)"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Goa (Dabolim/Mopa airport)", "🏖️ Calangute / Baga beach sunset stroll", "🍹 Beach shack seafood dinner"),
            ("Day 2", "🏄 Water sports morning — jet ski, parasailing, banana boat", "🍤 Seafood lunch at Fiesta or Infantaria", "🎶 Tito's Lane / Club Cubana evening"),
            ("Day 3", "⛪ Old Goa churches — Basilica of Bom Jesus (UNESCO)", "🌿 Spice plantation tour & traditional Goan lunch", "🌅 Fort Aguada sunset views"),
            ("Day 4", "🚤 Boat to Butterfly Beach + dolphin watching (South Goa)", "🐬 Scuba intro dive at Grande Island", "🎵 Palolem beach acoustic night"),
            ("Day 5", "🛍️ Anjuna Flea Market (Wed) or Mapusa Friday Market", "🥘 Goan fish curry cooking class", "🌙 Relaxed farewell dinner at Curlies"),
        ],
        "budget_tips": [
            "Rent a scooter (₹300–₹400/day) — cheapest and most fun transport; fill up at petrol pumps, not hotel vendors.",
            "Skip resort restaurants and eat at small beach shacks for authentic food at half price.",
            "Visit early November or late February — fewer crowds and hotel rates drop 20–30%.",
            "Book homestays in Assagao or Aldona — charming Portuguese houses, cheaper than tourist zones.",
        ],
    },

    "Varanasi, Uttar Pradesh": {
        "scope": "domestic",
        "types": ["Religious & Spiritual", "Heritage & Culture", "Photography", "Food & Culinary"],
        "seasons": ["Autumn", "Winter", "Spring"],
        "budget_min": "< ₹10K",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Solo", "Couple", "Family", "Friends Group"],
        "emoji": "🕌",
        "state_tags": ["Uttar Pradesh", "Bihar", "Madhya Pradesh", "Delhi", "Rajasthan"],
        "description": "One of the world's oldest living cities — a profound spiritual and cultural experience on the sacred banks of the Ganga.",
        "highlights": ["Ganga Aarti at Dashashwamedh Ghat (dusk ceremony)", "Sunrise boat ride on the Ganges", "Sarnath Buddhist ruins (5th c. BCE)", "Banaras Hindu University campus", "Kashi Vishwanath Temple"],
        "hidden_gem": "Ravindrapuri Colony's hidden silk-weaving workshops — watch master weavers create authentic Banarasi sarees by hand, and buy direct.",
        "cost_breakdown": {"Transport (return)": "₹500–₹2,000", "Stay/night": "₹400–₹2,000", "Food/day": "₹200–₹500", "Activities": "₹100–₹500"},
        "permit": "No permit required.",
        "safety": "Be cautious of touts near ghats; keep valuables secure in festival crowds; drink bottled water only.",
        "packing": ["Modest clothing for temples", "Comfortable walking shoes (cobblestone ghats)", "Small torch for evening ghat walks", "Hand sanitiser", "Small-denomination cash for donations"],
        "itinerary_template": [
            ("Day 1", "🚂 Arrive & check-in near Assi Ghat", "🚣 Evening boat ride on Ganges", "🔥 Ganga Aarti ceremony — Dashashwamedh Ghat"),
            ("Day 2", "🌅 Pre-dawn sunrise boat ride (5:30 AM)", "🕍 Kashi Vishwanath Temple darshan", "🍵 Malaiyo & Banarasi chaat breakfast at Kashi Chat"),
            ("Day 3", "🏛️ Sarnath — Dhamek Stupa & archaeological museum", "🧵 Silk-weaving workshop visit", "🎭 Classical Thumri / Banarasi music performance"),
            ("Day 4", "🚶 Walking tour of all 84 ghats (south to north)", "📸 Ghat photography & street art trail", "🍛 Banarasi thali dinner at Godowlia"),
            ("Day 5", "🛍️ Vishwanath Gali — silks, brassware, rudraksha", "☕ BHU campus & Bharat Kala Bhavan museum", "🚂 Evening departure"),
        ],
        "budget_tips": [
            "Stay in guesthouses in the lanes behind Assi Ghat — half the price of mainstream hotels.",
            "The ₹20–₹50 sunrise boat ride from local boatmen beats ₹200–₹500 tourist packages completely.",
            "Eat at Kashi Chat Bhandar or Deena Chat for world-class street food under ₹50.",
            "Auto-rickshaws are very cheap — always fix the price before boarding; refuse the first quote.",
        ],
    },

    "Andaman Islands": {
        "scope": "domestic",
        "types": ["Beach & Coastal", "Adventure", "Nature & Wildlife", "Photography"],
        "seasons": ["Autumn", "Winter"],
        "budget_min": "₹25K–₹50K",
        "fitness": ["Light", "Moderate", "Active"],
        "group_fit": ["Couple", "Family", "Friends Group"],
        "emoji": "🌊",
        "state_tags": ["Tamil Nadu", "Telangana", "Karnataka", "Kerala", "Other"],
        "description": "Crystal-clear waters, vibrant coral reefs, and untouched beaches that feel like the end of the earth.",
        "highlights": ["Scuba diving at Elephant Beach (Havelock)", "Radhanagar Beach — Asia's best (TripAdvisor)", "Cellular Jail Sound & Light show", "Sea walking at North Bay Island", "Glass-bottom boat at Ross Island"],
        "hidden_gem": "Barren Island — India's only active volcano; accessible via day-trip from Port Blair — dramatic and almost tourist-free.",
        "cost_breakdown": {"Flights (return)": "₹6,000–₹15,000", "Stay/night": "₹1,500–₹5,000", "Food/day": "₹500–₹1,200", "Activities": "₹1,000–₹4,000"},
        "permit": "Restricted Area Permit (RAP) issued free at Port Blair airport for Indian citizens. Certain islands (Baratang etc.) need separate permission.",
        "safety": "Always dive with PADI/SSI certified instructors; check sea conditions before water activities. Nov–Apr is safest.",
        "packing": ["Reef-safe sunscreen", "Rash guard / wetsuit", "Waterproof camera or GoPro", "Sea-sickness tablets (ferries can be rough)", "Insect repellent"],
        "itinerary_template": [
            ("Day 1", "✈️ Fly into Port Blair (from Chennai/Kolkata/Bengaluru)", "🏛️ Cellular Jail tour & Sound & Light show", "🍤 Seafood dinner at Aberdeen Bazaar"),
            ("Day 2", "🚢 Government ferry to Havelock Island (2–2.5 hrs)", "🏖️ Radhanagar Beach — swim, relax, watch sunset", "🌅 Sunset photography from the beach"),
            ("Day 3", "🤿 Scuba diving at Elephant Beach (for beginners too)", "🐠 Snorkelling at Neil Island (short ferry)", "🌙 Beach bonfire at glamping camp"),
            ("Day 4", "🚤 Glass-bottom boat tour", "🦈 Sea walking experience at North Bay", "🌴 Explore Kalapathar Beach (calm & secluded)"),
            ("Day 5", "🚢 Return ferry to Port Blair", "🛍️ Aberdeen Bazaar for handicrafts & shells", "✈️ Evening departure"),
        ],
        "budget_tips": [
            "Book government ferries (₹350–₹600) instead of private speedboats (₹1,000–₹1,500) — just book early.",
            "APWD (government) guesthouses are clean, affordable, and perfectly located.",
            "Buy diving packages directly from dive shops on Havelock — skip hotel middlemen (save 25%).",
            "Fly mid-week (Tue/Wed) — Andaman flights are ₹2,000–₹4,000 cheaper than weekends.",
        ],
    },

    "Rajasthan (Jaipur–Jodhpur–Jaisalmer)": {
        "scope": "domestic",
        "types": ["Heritage & Culture", "Photography", "Religious & Spiritual", "Food & Culinary", "Shopping"],
        "seasons": ["Autumn", "Winter"],
        "budget_min": "₹10K–₹25K",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Family", "Couple", "Friends Group", "Solo"],
        "emoji": "🏰",
        "state_tags": ["Delhi", "Uttar Pradesh", "Gujarat", "Rajasthan", "Punjab", "Other"],
        "description": "The land of maharajas — a riot of colour, towering forts, marble palaces, camel rides, and world-class cuisine.",
        "highlights": ["Amer Fort & Jaipur Pink City heritage walk", "Mehrangarh Fort, Jodhpur (Blue City)", "Jaisalmer Golden Fort (living fort)", "Sam Sand Dunes camel safari & sunset", "Pushkar camel fair (late November)"],
        "hidden_gem": "Osian — a small desert town 65 km from Jodhpur with stunning ancient Jain & Hindu temples and virtually zero tourists.",
        "cost_breakdown": {"Transport (circuit)": "₹2,000–₹5,000", "Stay/night": "₹600–₹3,000", "Food/day": "₹300–₹700", "Activities": "₹500–₹2,000"},
        "permit": "No permit required.",
        "safety": "Negotiate all camel/tuk-tuk prices upfront; carry drinking water on desert excursions; tourist scams near monuments — stay alert.",
        "packing": ["Light cotton (it's hot even in winter)", "Scarf for dust & sun", "Good sunglasses", "Sturdy walking shoes for forts", "Cash (ATMs scarce in Jaisalmer)"],
        "itinerary_template": [
            ("Day 1", "🚂 Arrive Jaipur — check in to heritage haveli", "🏰 Amer Fort & Jal Mahal", "🛍️ Johari Bazaar gems & silver shopping"),
            ("Day 2", "🌸 Hawa Mahal & City Palace museum", "🎨 Block-printing workshop", "🍛 Rajasthani thali dinner at Chokhi Dhani"),
            ("Day 3", "🚌 Jaipur → Jodhpur (5 hr bus — ₹250)", "🏯 Mehrangarh Fort & Jaswant Thada", "🔵 Blue City rooftop restaurant dinner"),
            ("Day 4", "🚌 Jodhpur → Jaisalmer (5 hr bus — ₹250)", "🌅 Golden Fort walk at sunset", "⭐ Desert camp check-in under stars"),
            ("Day 5", "🐪 Camel safari at Sam Sand Dunes", "🌄 Desert sunrise photography session", "🎵 Folk music & cultural show at camp"),
            ("Day 6", "🚶 Patwon Ki Haveli & Nathmal Ki Haveli", "🛍️ Fabric, leather & jewellery market", "🚂 Overnight train / bus homeward"),
        ],
        "budget_tips": [
            "RSRTC (state buses) connect Jaipur–Jodhpur–Jaisalmer for ₹200–₹350 per leg — trains are similar.",
            "Stay in heritage havelis converted into guesthouses — unique atmosphere at budget prices.",
            "Book Sam Dunes camp directly (skip OTAs) for 20–30% discount; bargain for group rates.",
            "Eat at roadside dhabas near fort entrances for authentic Dal Baati Churma at ₹80–₹120.",
        ],
    },

    "Coorg, Karnataka": {
        "scope": "domestic",
        "types": ["Nature & Wildlife", "Wellness & Spa", "Photography", "Food & Culinary"],
        "seasons": ["Spring", "Autumn", "Winter"],
        "budget_min": "₹10K–₹25K",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Couple", "Family", "Solo"],
        "emoji": "☕",
        "state_tags": ["Karnataka", "Kerala", "Tamil Nadu", "Telangana", "Andhra Pradesh"],
        "description": "The 'Scotland of India' — rolling coffee estates, misty forested hills, powerful waterfalls, and rejuvenating plantation homestays.",
        "highlights": ["Abbey Falls & Iruppu Falls (Nagarhole border)", "Coffee plantation tour & freshly-roasted tasting", "Namdroling Monastery — the Golden Temple", "Brahmagiri Trek (Talacauvery)", "Raja's Seat viewpoint — epic sunset"],
        "hidden_gem": "Mandalpatti viewpoint — a 9 km jeep trail through thick forests, emerging above the cloud layer for a 360° panorama that will silence you.",
        "cost_breakdown": {"Transport (return)": "₹600–₹2,500", "Stay/night": "₹1,200–₹4,000", "Food/day": "₹300–₹700", "Activities": "₹200–₹1,000"},
        "permit": "No permit required.",
        "safety": "Carry salt for leeches during and after monsoon treks; mountain roads can be slippery after rain.",
        "packing": ["Light fleece jacket (mornings are cool)", "Trekking shoes", "Insect repellent", "Rain poncho (Jun–Sep)", "Reusable water bottle"],
        "itinerary_template": [
            ("Day 1", "🚌 Arrive Madikeri from Bengaluru (5 hrs, ₹300 KSRTC)", "☕ Coffee plantation welcome walk at homestay", "🌅 Raja's Seat viewpoint for sunset"),
            ("Day 2", "🌊 Abbey Falls — morning visit before crowds arrive", "🍽️ Kodava pork curry & akki rotti lunch", "🧘 Plantation resort spa & Ayurveda session"),
            ("Day 3", "🚙 Jeep to Mandalpatti (above the clouds)", "🦚 Brahmagiri trek 8 km (guide recommended)", "🌿 Evening birdwatching nature walk"),
            ("Day 4", "🏛️ Namdroling Monastery — Golden Temple & murals", "☕ Coffee processing factory tour & cupping", "🛍️ Madikeri market — spices, honey, vanilla"),
        ],
        "budget_tips": [
            "KSRTC buses from Bengaluru (₹300–₹400) — far cheaper than private cabs (₹2,500+) and surprisingly comfortable.",
            "Plantation homestays include breakfast, forest walks, and coffee tasting — outstanding value.",
            "Hire a local auto for a day (₹600–₹800) instead of tourist taxis for all sightseeing.",
            "Buy Coorg honey, pepper, and vanilla directly at plantations — half the price of market stalls.",
        ],
    },

    "Leh-Ladakh": {
        "scope": "domestic",
        "types": ["Adventure", "Nature & Wildlife", "Photography", "Religious & Spiritual"],
        "seasons": ["Summer"],
        "budget_min": "₹25K–₹50K",
        "fitness": ["Active", "Very Active"],
        "group_fit": ["Solo", "Friends Group", "Couple"],
        "emoji": "🏕️",
        "state_tags": ["Delhi", "Punjab", "Himachal Pradesh", "Uttarakhand", "Other"],
        "description": "A high-altitude moonscape of ancient monasteries, turquoise lakes, and the world's most dramatic mountain highways.",
        "highlights": ["Pangong Tso Lake (17,000 ft)", "Nubra Valley Bactrian camel safari", "Khardung La Pass (world's highest motorable road)", "Thiksey & Hemis Monasteries", "Magnetic Hill & Gurudwara Pathar Sahib"],
        "hidden_gem": "Tso Moriri Lake — a remote high-altitude lake near the Tibetan border, even more stunning than Pangong with almost zero tourist traffic.",
        "cost_breakdown": {"Flights (return)": "₹5,000–₹12,000", "Stay/night": "₹800–₹3,000", "Food/day": "₹400–₹800", "Activities + ILP": "₹1,500–₹4,000"},
        "permit": "Inner Line Permit (ILP) required for Pangong, Nubra Valley & Tso Moriri — obtainable in Leh (online or DC office).",
        "safety": "MUST acclimatise 2 full days before any physical activity. AMS (altitude sickness) above 3,500m is life-threatening — carry Diamox.",
        "packing": ["Heavy thermals & down jacket", "Sunscreen SPF 70+ (UV is intense at altitude)", "Diamox tablets (AMS prevention)", "Portable oxygen can", "Offline maps — Leh has patchy connectivity"],
        "itinerary_template": [
            ("Day 1", "✈️ Fly to Leh — complete REST (acclimatisation is mandatory)", "🚶 Short gentle stroll around Leh Bazaar only", "💤 Early sleep — no alcohol, no exertion"),
            ("Day 2", "🏛️ Leh Palace & Shanti Stupa (light walking)", "🕍 Spituk Monastery & Hall of Fame museum", "🌆 Leh Market — pashmina & walnut wood shopping"),
            ("Day 3", "📋 Collect ILP permits from DC office (9 AM sharp)", "🏔️ Thiksey Monastery & Hemis Monastery", "🌅 Overnight camp near Pangong"),
            ("Day 4", "🏞️ Pangong Tso sunrise photography (colour shift)", "🧲 Magnetic Hill phenomenon & Indus-Zanskar confluence", "🐪 Drive to Nubra Valley — overnight camp"),
            ("Day 5", "🐫 Nubra Valley double-hump Bactrian camel ride", "🌄 Diskit Monastery & giant Maitreya Buddha statue", "✈️ Return to Leh — overnight"),
        ],
        "budget_tips": [
            "The Manali–Leh highway (shared jeep ₹1,500–₹2,500) is a legendary 2-day mountain journey vs. ₹8,000 flights.",
            "Old town guesthouses in Leh are 40% cheaper than airport-area hotels and more atmospheric.",
            "Split motorcycle hire costs (₹800–₹1,200/day) in a group — cheapest way to tackle high passes.",
            "Carry all medications, snacks and toiletries from Delhi/Manali — everything costs 30–40% more in Leh.",
        ],
    },

    "Kerala Backwaters": {
        "scope": "domestic",
        "types": ["Nature & Wildlife", "Wellness & Spa", "Food & Culinary", "Photography"],
        "seasons": ["Autumn", "Winter"],
        "budget_min": "₹10K–₹25K",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Couple", "Family", "Solo"],
        "emoji": "🛶",
        "state_tags": ["Kerala", "Tamil Nadu", "Karnataka", "Telangana", "Andhra Pradesh"],
        "description": "A labyrinth of lagoons, canals and lakes fringed by coconut palms — the quintessential Kerala experience from a houseboat.",
        "highlights": ["Alleppey overnight houseboat stay", "Kumarakom Bird Sanctuary", "Munnar tea garden trek", "Periyar Wildlife Sanctuary (elephant & tiger reserve)", "Authentic Ayurveda treatment"],
        "hidden_gem": "Kuttanad — the 'Venice of the East', a below-sea-level agricultural landscape where you can cycle through paddy fields and fish with locals.",
        "cost_breakdown": {"Transport (return)": "₹800–₹3,000", "Houseboat/night": "₹2,500–₹8,000 (all-inclusive)", "Food/day": "₹300–₹700", "Activities": "₹300–₹1,500"},
        "permit": "No permit required.",
        "safety": "Choose KTDC-certified houseboats for safety compliance; October can have lingering monsoon currents — check conditions.",
        "packing": ["Light cottons", "Rain jacket (Oct showers possible)", "Motion sickness tablets for boat journeys", "Mosquito repellent", "Sunhat & sunglasses"],
        "itinerary_template": [
            ("Day 1", "🚂 / ✈️ Arrive Kochi — Fort Kochi walk", "⛵ Chinese fishing nets & Jew Town Spice Market", "🍤 Kerala fish curry dinner at a toddy shop"),
            ("Day 2", "🚌 Drive Kochi → Alleppey (1.5 hrs)", "🛶 Board houseboat at noon — backwater cruise begins", "🌅 Sunset over the paddy fields from upper deck"),
            ("Day 3", "☀️ Early canoe ride through narrow village canals", "🦚 Kumarakom Bird Sanctuary birding walk", "🌿 Traditional Ayurvedic massage at resort"),
            ("Day 4", "🍵 Drive to Munnar tea estates (3 hrs)", "🌿 Tea museum, factory tour & tasting", "🦏 Eravikulam National Park — Nilgiri Tahr spotting"),
        ],
        "budget_tips": [
            "Book houseboats directly at Alleppey jetty — 25–35% cheaper than online platforms.",
            "KTDC-run houseboats are affordable, regulated, and perfectly comfortable.",
            "Eat at small Kerala 'meals' restaurants for unlimited rice + 5 curries at ₹80–₹120.",
            "KSRTC buses between Alleppey, Kottayam, and Munnar are extremely cheap (₹50–₹150).",
        ],
    },

    # ── INTERNATIONAL ─────────────────────────────────────────────────────────
    "Bali, Indonesia": {
        "scope": "international",
        "types": ["Beach & Coastal", "Wellness & Spa", "Nature & Wildlife", "Religious & Spiritual", "Photography"],
        "seasons": ["Spring", "Autumn", "Winter"],
        "budget_min": "₹50K–₹1L",
        "fitness": ["Sedentary", "Light", "Moderate", "Active"],
        "group_fit": ["Solo", "Couple", "Friends Group"],
        "emoji": "🌺",
        "description": "Rice terraces, Hindu temples, surf breaks, and spa culture — Bali delivers a complete sensory experience unlike anywhere else.",
        "highlights": ["Tegallalang Rice Terraces, Ubud", "Tanah Lot Temple at sunset", "Mount Batur volcano sunrise trek", "Seminyak & Canggu beach clubs", "Ubud Sacred Monkey Forest"],
        "hidden_gem": "Sekumpul Waterfalls, North Bali — a jaw-dropping series of 7 falls deep in the jungle, visited by very few tourists compared to the south.",
        "cost_breakdown": {"Flights (return)": "₹18,000–₹35,000", "Stay/night": "₹1,500–₹8,000", "Food/day": "₹400–₹1,200", "Activities": "₹500–₹3,000"},
        "permit": "Visa on Arrival for Indians — $35 USD at airport. New Bali tourist tax ~$20 applies.",
        "safety": "Don't touch or step on temple offerings. Sarong mandatory at all temples. Drink only bottled/filtered water.",
        "packing": ["Sarong for temples", "Reef-safe sunscreen", "Mosquito repellent", "Light layers for Ubud evenings", "Comfortable sandals & flip-flops"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Denpasar — transfer to Ubud (1.5 hrs)", "🌿 Sunrise yoga class at The Yoga Barn", "🍜 Warung dinner in Ubud's Monkey Forest Road"),
            ("Day 2", "🌾 Tegallalang Rice Terraces early morning walk", "🐵 Sacred Monkey Forest & Tirta Empul Holy Spring", "🎭 Kecak Fire Dance performance at sunset"),
            ("Day 3", "🌋 4 AM Mount Batur sunrise trek (guide included)", "💆 Traditional Balinese massage — 90 min (₹800)", "🛍️ Ubud Art Market for handmade souvenirs"),
            ("Day 4", "🚗 Transfer to Canggu / Seminyak", "🏄 Surf lesson at Echo Beach or Batu Bolong", "🌅 Potato Head or La Brisa beach club sunset"),
            ("Day 5", "🕌 Tanah Lot Temple (low tide walk to rock)", "🌊 Uluwatu cliff temple at sunset", "🔥 Kecak dance at Uluwatu amphitheatre"),
            ("Day 6", "🤿 Snorkelling at Amed or Nusa Penida day trip", "🐢 Green sea turtle sanctuary", "✈️ Late evening departure"),
        ],
        "budget_tips": [
            "Book IndiGo or AirAsia — Bali round trips from Mumbai/Delhi can be under ₹18,000 with 6–8 weeks notice.",
            "Stay in Ubud for culture or Canggu for surf — both 30–40% cheaper than Seminyak.",
            "Hire a local driver for full-day temple tours (~$35–45 for the car, not per person) — far cheaper than Grab.",
            "Eat at warungs (local canteens) — Nasi Goreng and Mie Goreng for ₹100–₹200 a plate.",
        ],
    },

    "Thailand (Bangkok–Chiang Mai–Phuket)": {
        "scope": "international",
        "types": ["Beach & Coastal", "Food & Culinary", "Adventure", "Art & Entertainment", "Heritage & Culture"],
        "seasons": ["Autumn", "Winter"],
        "budget_min": "₹50K–₹1L",
        "fitness": ["Sedentary", "Light", "Moderate", "Active"],
        "group_fit": ["Solo", "Couple", "Friends Group", "Family"],
        "emoji": "🐘",
        "description": "Temples, tuk-tuks, legendary street food, and powder-white tropical beaches — Thailand packs everything into one magnificent trip.",
        "highlights": ["Grand Palace & Emerald Buddha, Bangkok", "Chiang Mai Elephant Nature Park sanctuary", "Phi Phi Islands island hopping", "Chiang Mai Night Bazaar & walking streets", "Muay Thai fight night ringside"],
        "hidden_gem": "Pai — a tiny mountain town near Chiang Mai with natural hot springs, canyon walks, and a thriving café scene almost untouched by package tourism.",
        "cost_breakdown": {"Flights (return)": "₹15,000–₹28,000", "Stay/night": "₹800–₹4,000", "Food/day": "₹300–₹800", "Activities": "₹400–₹2,500"},
        "permit": "Visa on Arrival — ₹2,500 (~2,000 THB), 15 days. Apply for e-Visa for longer stays. No visa needed for trips under 30 days from 2024.",
        "safety": "Never disrespect the monarchy (strict lèse-majesté laws). Negotiate tuk-tuk fares; avoid jet-ski rentals in Phuket (documented scam).",
        "packing": ["Temple-appropriate clothes (shoulders & knees covered)", "Reef-safe sunscreen", "Small daypack for island trips", "Insect repellent", "Type A/B power adapter"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Bangkok — check-in near Silom/Sukhumvit", "🏛️ Grand Palace & Temple of the Emerald Buddha", "🍜 Khao San Road street food crawl"),
            ("Day 2", "⛵ Chao Phraya river — Wat Arun & Wat Pho", "🛒 Chatuchak Weekend Market (Sat/Sun)", "🥊 Muay Thai fight night at Lumphini Stadium"),
            ("Day 3", "✈️ Fly Bangkok → Chiang Mai (1 hr, ~₹2,000)", "🐘 Elephant Nature Park ethical sanctuary (full day)", "🌙 Chiang Mai Night Bazaar"),
            ("Day 4", "🏔️ Doi Inthanon National Park — highest peak in Thailand", "🧘 Doi Suthep Temple meditation session", "🍲 Khao Soi coconut curry (Chiang Mai specialty)"),
            ("Day 5", "✈️ Fly Chiang Mai → Phuket (1.5 hrs)", "🏖️ Patong or Kata Beach — swim & relax", "🌅 Sunset at Promthep Cape with panoramic views"),
            ("Day 6", "🚤 Full-day Phi Phi Islands speedboat tour", "🤿 Snorkelling at Maya Bay & Viking Cave", "🍹 Beach bar farewell dinner at Bangla Road"),
        ],
        "budget_tips": [
            "IndiGo and AirAsia fly Delhi/Mumbai→Bangkok from ₹12,000 return — set fare alerts 6–8 weeks out.",
            "Night trains Bangkok → Chiang Mai (₹600–₹1,200 sleeper) are scenic and save one night's hotel cost.",
            "Buy breakfast at 7-Eleven and local markets (₹80–₹120) — skip hotel breakfasts completely.",
            "Longtail 'island hopping' boats on Phi Phi cost half of packaged speed-boat tours.",
        ],
    },

    "Nepal (Kathmandu–Pokhara–Trekking)": {
        "scope": "international",
        "types": ["Adventure", "Religious & Spiritual", "Nature & Wildlife", "Photography"],
        "seasons": ["Spring", "Autumn"],
        "budget_min": "₹25K–₹50K",
        "fitness": ["Moderate", "Active", "Very Active"],
        "group_fit": ["Solo", "Couple", "Friends Group"],
        "emoji": "⛰️",
        "description": "The roof of the world — Himalayan treks, ancient stupas, Pashupatinath ghats, and unmatched Annapurna mountain panoramas.",
        "highlights": ["Poon Hill or Annapurna Base Camp trek", "Pashupatinath Temple & Boudhanath Stupa", "Sunrise over Machhapuchhre from Pokhara", "Paragliding above Phewa Lake", "Chitwan National Park jungle safari"],
        "hidden_gem": "Bandipur — a pristine hilltop Newari town between Kathmandu and Pokhara, perfectly preserved and bypassed by nearly all tourists.",
        "cost_breakdown": {"Flights (return)": "₹6,000–₹18,000", "Stay/night": "₹500–₹2,500", "Food/day": "₹250–₹600", "Trekking permits": "₹1,800–₹4,500"},
        "permit": "TIMS card (₹800–₹1,600) + Annapurna Conservation Area Permit (₹1,800) required for Annapurna treks. Obtainable in Kathmandu or Pokhara.",
        "safety": "Hire a licensed guide for Annapurna — trails aren't always marked. Altitude sickness is serious above 3,500m; ascend gradually.",
        "packing": ["Layer system (thermal base, fleece mid, waterproof outer)", "Trekking poles", "Blister plasters", "Diamox (altitude sickness)", "Headlamp with spare batteries"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Kathmandu (1,400m — no altitude concern)", "🕍 Pashupatinath cremation ghats & Boudhanath Stupa walk", "🍺 Thamel evening — momos & tongba millet beer"),
            ("Day 2", "🏔️ Swayambhunath Monkey Temple at dawn", "🚌 Drive / fly to Pokhara (6 hrs road / 25 min air)", "🌊 Phewa Lake sunset boat ride"),
            ("Day 3", "🪂 Paragliding above Pokhara Valley (₹4,500)", "🌅 Sarangkot sunrise viewpoint (drive up at 5 AM)", "🍛 Dal bhat unlimited refill at local restaurant"),
            ("Day 4", "🥾 Trek begins — Nayapul to Tikhedhunga (6 hrs)", "⛺ Tea house stay at 1,540m altitude", "⭐ Milky Way stargazing at Ghorepani"),
            ("Day 5", "🌄 Poon Hill sunrise (5:30 AM) — Annapurna/Dhaulagiri panorama", "🚶 Descend via rhododendron forest back to Pokhara", "🎉 Celebration dinner — Lake Side Pokhara"),
        ],
        "budget_tips": [
            "IndiGo flies Kolkata→Kathmandu from ₹4,000–₹8,000 one way — the cheapest Indian gateway.",
            "Tea house trekking (sleeping in local lodges en route) costs ₹600–₹1,000/night with dinner & breakfast included.",
            "Dal bhat (rice, lentils, vegetables) is the cheapest and most filling trail meal at ₹150–₹250.",
            "Hire a local porter (₹1,500/day) rather than a full guide for budget Poon Hill trek — they know every turn.",
        ],
    },

    "Dubai, UAE": {
        "scope": "international",
        "types": ["City & Urban", "Shopping", "Beach & Coastal", "Food & Culinary", "Art & Entertainment"],
        "seasons": ["Autumn", "Winter", "Spring"],
        "budget_min": "₹1L–₹2L",
        "fitness": ["Sedentary", "Light", "Moderate"],
        "group_fit": ["Couple", "Family", "Friends Group", "Business"],
        "emoji": "🏙️",
        "description": "A city of superlatives — the world's tallest tower, largest mall, and most audacious architecture rising from the Arabian desert.",
        "highlights": ["Burj Khalifa At The Top (level 124 & 148)", "Dubai Mall + Dubai Fountain evening show", "Desert Safari with dune bashing & BBQ", "Dubai Creek Gold Souk & Spice Souk", "Palm Jumeirah Atlantis Aquaventure"],
        "hidden_gem": "Al Fahidi Historical Neighbourhood — old wind-tower houses turned into galleries, cafés and museums; Dubai before the skyscrapers took over.",
        "cost_breakdown": {"Flights (return)": "₹8,000–₹20,000", "Stay/night": "₹3,000–₹15,000", "Food/day": "₹800–₹2,500", "Activities": "₹1,500–₹6,000"},
        "permit": "Indians with valid US/UK/Schengen visa: free 14-day VOA. Otherwise apply UAE tourist e-Visa online (~₹6,000, 5–7 working days).",
        "safety": "Respect local laws — no public displays of affection; no photography of government buildings or airports.",
        "packing": ["Smart-casual clothes for malls & restaurants", "Light jacket (hotels & malls are heavily air-conditioned)", "Sunscreen SPF 50+", "Comfortable walking shoes", "Modest dress for old Dubai visits"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Dubai, check in near Downtown", "🏙️ Burj Khalifa At The Top — book sunset slot", "💦 Dubai Fountain show & Souk Al Bahar dinner"),
            ("Day 2", "🕌 Al Fahidi Heritage Area & Dubai Museum", "🛶 Abra (₹5 water taxi) across Dubai Creek", "🥇 Gold Souk & Spice Souk sensory experience"),
            ("Day 3", "🏖️ JBR Beach morning swim & walk", "🛍️ Dubai Mall — Virtual Reality Park & Aquarium", "🌃 Downtown Dubai fountain show from café"),
            ("Day 4", "🏜️ Evening desert safari — dune bashing by 4WD", "🌅 Camel ride, sandboarding & henna tattoo", "🎶 Arabic BBQ dinner with traditional music show"),
            ("Day 5", "🌴 Palm Jumeirah monorail to Atlantis", "🎢 Atlantis Aquaventure Waterpark (full day)", "✈️ Late evening departure from DXB/DWC"),
        ],
        "budget_tips": [
            "IndiGo and Air Arabia fly to Dubai from ₹7,000 return — skip Emirates and FlyDubai for budget travel.",
            "Dubai Metro (NOL card, ₹30–₹60/ride) reaches all major attractions fast and cheaply.",
            "Eat at Al Rigga or Bur Dubai streets — Indian, Pakistani and Lebanese food from ₹150–₹300.",
            "Book Burj Khalifa tickets online in advance (weekday afternoons) — saves 30% vs. at-the-door pricing.",
        ],
    },

    "Vietnam (Hanoi–Hoi An–Ho Chi Minh City)": {
        "scope": "international",
        "types": ["Heritage & Culture", "Food & Culinary", "Nature & Wildlife", "Photography", "Adventure"],
        "seasons": ["Spring", "Autumn", "Winter"],
        "budget_min": "₹50K–₹1L",
        "fitness": ["Light", "Moderate", "Active"],
        "group_fit": ["Solo", "Couple", "Friends Group"],
        "emoji": "🏮",
        "description": "Lantern-lit ancient towns, emerald bays, motorbike chaos, and pho so good it will ruin you for all other soups.",
        "highlights": ["Ha Long Bay 2-night cruise (UNESCO)", "Hoi An Ancient Town & lantern festival", "Mekong Delta day boat tour", "Cu Chi Tunnels of Vietnam War", "Sapa hill tribe village trekking"],
        "hidden_gem": "Ninh Binh — 'Ha Long Bay on land', with dramatic limestone karsts rising from flooded rice paddies; 90% fewer tourists than Ha Long Bay.",
        "cost_breakdown": {"Flights (return)": "₹18,000–₹35,000", "Stay/night": "₹600–₹3,500", "Food/day": "₹300–₹700", "Activities": "₹400–₹2,500"},
        "permit": "Indians need Vietnam e-Visa — apply online at evisa.xuatnhapcanh.gov.vn. Cost $25 USD, ~3 working days.",
        "safety": "Cross roads steadily and confidently — traffic flows around pedestrians; hold bag tightly on motorbikes in cities.",
        "packing": ["Light layers (Hanoi is cooler Nov–Mar)", "Rain jacket", "Modest temple clothes (shoulders/knees)", "Stomach medication (street food-heavy trip)", "USD cash and local VND"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Hanoi — check in Old Quarter", "🌆 Hoan Kiem Lake & Ngoc Son Temple at dusk", "🍜 Pho & Bun Cha dinner on Ta Hien Street"),
            ("Day 2", "🏺 Ho Chi Minh Mausoleum & Temple of Literature", "🚌 Afternoon drive to Ninh Binh (2 hrs)", "🚣 Evening boat through Tam Coc cave systems"),
            ("Day 3", "⛵ Ha Long Bay 2-day cruise departs Hanoi pier", "🦑 Kayaking through hidden lagoons & floating villages", "🌅 Sunset cocktails on upper deck"),
            ("Day 4", "🏝️ Surprise Cave & Ti Top Island swimming", "✈️ Fly Hanoi → Da Nang → transfer to Hoi An", "🏮 Hoi An Ancient Town by lantern light"),
            ("Day 5", "🎨 Lantern-making workshop in Hoi An", "🚲 Cycling through rice paddy countryside", "🍤 White Rose & Cao Lau noodle cooking class"),
            ("Day 6", "✈️ Fly Da Nang → Ho Chi Minh City", "🕳️ Cu Chi Tunnels afternoon tour (sobering & fascinating)", "🌃 Bui Vien Walking Street farewell night"),
        ],
        "budget_tips": [
            "Vietnam Airlines and AirAsia fly Hanoi/HCM from India from ₹16,000 return — book early.",
            "Open Bus Tickets (₹1,500–₹3,000) cover Hanoi→Hoi An→HCM with flexible stopovers.",
            "A bowl of pho costs ₹60–₹100 on the street — eat all meals local and save thousands per day.",
            "Book Ha Long Bay 2-night cruises via Hanoi travel cafés (30% cheaper than hotel desks or OTAs).",
        ],
    },

    "Europe Budget (Prague–Budapest–Vienna)": {
        "scope": "international",
        "types": ["Heritage & Culture", "Food & Culinary", "Art & Entertainment", "Photography", "City & Urban"],
        "seasons": ["Spring", "Summer", "Autumn"],
        "budget_min": "₹1L–₹2L",
        "fitness": ["Light", "Moderate"],
        "group_fit": ["Couple", "Friends Group", "Solo"],
        "emoji": "🏰",
        "description": "The most beautiful budget circuit in Central Europe — fairy-tale castles, grand river promenades, and a world-class café culture.",
        "highlights": ["Prague Old Town Square & Astronomical Clock (1410 AD)", "Budapest Széchenyi thermal baths", "Vienna Schönbrunn Palace & Imperial history", "Charles Bridge at pre-dawn (no crowds)", "Hungarian Parliament illuminated by night"],
        "hidden_gem": "Szentendre — a tiny Serbian-influenced artist village 45 min from Budapest: cobblestone lanes, wine bars, and no tourist buses whatsoever.",
        "cost_breakdown": {"Flights (return)": "₹45,000–₹80,000", "Stay/night": "₹2,000–₹6,000", "Food/day": "₹1,000–₹2,500", "InterRail transport": "₹3,000–₹8,000"},
        "permit": "Schengen Visa required for Indian passport holders — apply 4–6 weeks ahead. Need: bank statement, travel insurance, accommodation bookings.",
        "safety": "Pickpocketing in tourist zones — use neck pouches; taxis from apps (Bolt/Uber) only; never exchange currency at airport booths.",
        "packing": ["Very comfortable walking shoes (cobblestones everywhere)", "Light rain jacket", "Type C European power adapter", "Travel insurance printout", "Some local cash (Koruna, Forint, Euro)"],
        "itinerary_template": [
            ("Day 1", "✈️ Arrive Prague — check in near Old Town", "🏰 Prague Castle & St. Vitus Cathedral (golden hour)", "🍺 Czech pilsner & svíčková (beef in cream sauce) dinner"),
            ("Day 2", "⏰ Astronomical Clock striking ceremony (hourly)", "🌉 Charles Bridge at 6 AM — zero tourists", "🎶 Classical concert in Baroque church evening"),
            ("Day 3", "🚂 Train Prague → Budapest (7 hrs, scenic)", "🌆 Buda Castle & Fisherman's Bastion at sunset", "🔥 Szimpla Kert ruin bar experience"),
            ("Day 4", "🛁 Széchenyi thermal bath — 3 hr soak", "🛳️ Danube Bend river cruise", "🏛️ Walk across Chain Bridge — Parliament at night"),
            ("Day 5", "🚂 Train Budapest → Vienna (2.5 hrs — direct)", "🎨 Vienna MuseumsQuartier contemporary art", "🎹 Vienna State Opera standing tickets (₹400)"),
            ("Day 6", "🏯 Schönbrunn Palace gardens & Gloriette viewpoint", "☕ Viennese coffee house — Café Central or Café Schwarzenberg", "✈️ Departure from Vienna International Airport"),
        ],
        "budget_tips": [
            "Prague and Budapest are 40–50% cheaper than Paris or Amsterdam — perfect first Europe trip for Indian travellers.",
            "Eurail Select Pass covers all 3 countries — buy online before departure for cheaper prices.",
            "Eat lunch at Czech 'bufet' / Hungarian 'étkezde' self-service canteens — full meals for €3–€5.",
            "Apply for Schengen visa with Czech Republic as primary destination — reportedly faster processing.",
        ],
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
BUDGET_ORDER = ["< ₹10K", "₹10K–₹25K", "₹25K–₹50K", "₹50K–₹1L", "₹1L–₹2L", "> ₹2L"]

def budget_index(b):
    try:
        return BUDGET_ORDER.index(b)
    except ValueError:
        return 0

def score_destination(dest_name, data, prefs):
    if data["scope"] != prefs["scope"]:
        return -1
    if budget_index(data["budget_min"]) > budget_index(prefs["budget"]):
        return -1

    score = 0
    season_word = "".join(c for c in prefs["season"].split("(")[0] if c.isalpha() or c == " ").strip()
    for s in data["seasons"]:
        if s.lower() in season_word.lower() or season_word.lower() in s.lower():
            score += 30
            break

    clean_pref_types = [t.split(" ", 1)[1] if " " in t else t for t in prefs["trip_types"]]
    for pt in clean_pref_types:
        if any(pt.lower() in dt.lower() or dt.lower() in pt.lower() for dt in data["types"]):
            score += 20

    clean_group = prefs["group"].split(" ", 1)[1] if " " in prefs["group"] else prefs["group"]
    if clean_group in data.get("group_fit", []):
        score += 15

    if prefs["fitness"] in data.get("fitness", []):
        score += 10

    if prefs["scope"] == "domestic" and prefs.get("origin_state") in data.get("state_tags", []):
        score += 5

    score += random.uniform(0, 3)
    return score

def get_recommendations(prefs, top_n=3):
    scored = [(score_destination(n, d, prefs), n, d) for n, d in DESTINATIONS.items()]
    scored = [x for x in scored if x[0] >= 0]
    scored.sort(key=lambda x: x[0], reverse=True)
    return scored[:top_n]

def build_itinerary(dest_data, duration):
    template = dest_data.get("itinerary_template", [])
    days = []
    for i in range(1, duration + 1):
        if i <= len(template):
            days.append(template[i - 1])
        else:
            days.append((
                f"Day {i}",
                "🌅 Morning: Explore a nearby neighbourhood or local market",
                "🎨 Afternoon: Visit a museum, gallery, or scenic viewpoint",
                "🍽️ Evening: Try a local restaurant or night market",
            ))
    return days


# ─────────────────────────────────────────────────────────────────────────────
# HERO
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>🌍 WanderWise</h1>
    <p>Your personalised travel planner — budget-smart, season-aware, no API key needed</p>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ✈️ Trip Preferences")
    st.markdown("---")

    st.markdown('<div class="sidebar-label">🌐 Trip Scope</div>', unsafe_allow_html=True)
    trip_scope = st.radio("Trip type", ["🏠 Domestic (India)", "🌍 International"], label_visibility="collapsed")
    is_domestic = "Domestic" in trip_scope

    if is_domestic:
        origin_state = st.selectbox("Home state", [
            "Uttar Pradesh","Delhi","Maharashtra","Karnataka","Tamil Nadu",
            "Rajasthan","Gujarat","West Bengal","Telangana","Kerala",
            "Madhya Pradesh","Punjab","Himachal Pradesh","Uttarakhand","Other"])
    else:
        origin_country = st.selectbox("Travelling from", [
            "India","USA","UK","UAE","Germany","Australia","Canada","Singapore","France","Japan","Other"])

    st.markdown("---")
    st.markdown('<div class="sidebar-label">💰 Budget (INR)</div>', unsafe_allow_html=True)
    budget_range = st.select_slider("Budget", options=BUDGET_ORDER, value="₹25K–₹50K", label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">📅 Travel Season</div>', unsafe_allow_html=True)
    season = st.selectbox("Season", [
        "🌸 Spring (Mar–May)","☀️ Summer (Jun–Aug)","🍂 Autumn (Sep–Nov)","❄️ Winter (Dec–Feb)"],
        label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">🗓️ Duration (days)</div>', unsafe_allow_html=True)
    duration = st.slider("Days", 1, 30, 7, label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">🎯 Trip Type</div>', unsafe_allow_html=True)
    trip_types = st.multiselect("Interests", [
        "🏔️ Adventure","🌿 Nature & Wildlife","🕌 Religious & Spiritual",
        "🏖️ Beach & Coastal","🏛️ Heritage & Culture","🍽️ Food & Culinary",
        "🎭 Art & Entertainment","🛍️ Shopping","💆 Wellness & Spa",
        "📸 Photography","🎓 Educational","🌆 City & Urban"],
        default=["🌿 Nature & Wildlife"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">👥 Travelling As</div>', unsafe_allow_html=True)
    travel_group = st.radio("Group", [
        "🧍 Solo","👫 Couple","👨‍👩‍👧‍👦 Family","👯 Friends Group","💼 Business"],
        label_visibility="collapsed")
    group_size = 1
    if "Solo" not in travel_group:
        group_size = st.number_input("Group size", min_value=2, max_value=50, value=4)

    st.markdown("---")
    st.markdown('<div class="sidebar-label">🏨 Accommodation</div>', unsafe_allow_html=True)
    accommodation = st.selectbox("Stay", [
        "🏕️ Camping / Hostel","🏠 Budget Hotel / Guesthouse","🏩 3-Star Hotel",
        "🌟 4–5 Star Hotel","🏡 Homestay / Airbnb","🧘 Resort / Retreat","No preference"],
        label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">💪 Fitness Level</div>', unsafe_allow_html=True)
    fitness = st.select_slider("Fitness", options=["Sedentary","Light","Moderate","Active","Very Active"],
        value="Moderate", label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">⚙️ Special Requirements</div>', unsafe_allow_html=True)
    special = st.multiselect("Needs", [
        "♿ Wheelchair Accessible","👶 Kid Friendly","🐾 Pet Friendly",
        "🌱 Vegan / Vegetarian Food","🍖 Non-veg Food Required","🕌 Halal Food",
        "🚫 Avoid Crowded Places","📵 Off-the-grid"], label_visibility="collapsed")

    st.markdown("---")
    st.markdown('<div class="sidebar-label">📝 Extra Notes</div>', unsafe_allow_html=True)
    extra = st.text_area("Notes", placeholder="E.g. I love waterfalls, hate long drives...",
        label_visibility="collapsed", height=80)

    st.markdown("---")
    generate_btn = st.button("🔮 Find My Perfect Trip", use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# WELCOME SCREEN
# ─────────────────────────────────────────────────────────────────────────────
if not generate_btn:
    c1, c2 = st.columns([2, 1])
    with c1:
        st.markdown("""
        <div style='text-align:center;padding:3rem 1rem;color:#8B949E;'>
            <div style='font-size:4rem;'>🧳</div>
            <h3 style='color:#8B949E;font-family:DM Sans,sans-serif;font-weight:400;'>
                Fill in your preferences on the left and click<br>
                <span style='color:#C9A84C;'>Find My Perfect Trip</span>
            </h3>
            <p style='font-size:0.88rem;'>100% free · No API key · No account needed · Instant results</p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div style='background:#161B22;border:1px solid #30363D;border-radius:12px;padding:1.5rem;'>
            <h3 style='color:#C9A84C;font-family:Playfair Display,serif;margin-top:0;'>What you get</h3>
            <ul style='color:#8B949E;line-height:2.1;list-style:none;padding:0;margin:0;font-size:0.93rem;'>
                <li>✅ Top 3 destination picks</li>
                <li>✅ Day-by-day itinerary</li>
                <li>✅ Cost breakdowns</li>
                <li>✅ Visa &amp; permit info</li>
                <li>✅ Hidden gem per destination</li>
                <li>✅ Safety tips</li>
                <li>✅ Packing list</li>
                <li>✅ Budget-saving tips</li>
                <li>✅ Side-by-side comparison</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.stop()


# ─────────────────────────────────────────────────────────────────────────────
# RESULTS
# ─────────────────────────────────────────────────────────────────────────────
if not trip_types:
    st.warning("⚠️ Please select at least one Trip Type from the sidebar.")
    st.stop()

prefs = {
    "scope": "domestic" if is_domestic else "international",
    "origin_state": origin_state if is_domestic else None,
    "budget": budget_range,
    "season": season,
    "duration": duration,
    "trip_types": trip_types,
    "group": travel_group,
    "group_size": group_size,
    "accommodation": accommodation,
    "fitness": fitness,
    "special": special,
    "extra": extra,
}

results = get_recommendations(prefs, top_n=3)

# Filter tags
clean_group = travel_group.split(" ", 1)[1] if " " in travel_group else travel_group
scope_label = "Domestic 🇮🇳" if is_domestic else "International 🌍"
tags_html = "".join([
    f'<span class="badge">{scope_label}</span>',
    f'<span class="badge">{budget_range}</span>',
    f'<span class="badge badge-blue">{season.split("(")[0].strip()}</span>',
    f'<span class="badge badge-blue">{duration} Days</span>',
    f'<span class="badge badge-green">{clean_group} × {group_size}</span>',
    *[f'<span class="badge">{t}</span>' for t in trip_types],
])
st.markdown(f"""
<div style='margin-bottom:1.5rem;'>
    <span style='color:#8B949E;font-size:0.8rem;font-weight:600;letter-spacing:0.05em;'>YOUR FILTERS &nbsp;</span>
    {tags_html}
</div>
""", unsafe_allow_html=True)

if not results:
    st.error("😕 No destinations matched your filters. Try expanding your budget, changing the season, or selecting different trip types.")
    st.stop()

# ── Destination Cards ─────────────────────────────────────────────────────────
st.markdown('<div class="section-header">🏆 Top Destination Picks For You</div>', unsafe_allow_html=True)
medals = ["🥇", "🥈", "🥉"]

for idx, (score, dest_name, dest_data) in enumerate(results):
    medal = medals[idx] if idx < 3 else "📍"
    st.markdown(f"""
    <div class="dest-card">
        <h2>{medal} {dest_data['emoji']} {dest_name}</h2>
        <div style='margin-bottom:0.8rem;'>
            {''.join([f'<span class="badge">{t}</span>' for t in dest_data["types"]])}
            <span class="badge badge-blue">Best: {', '.join(dest_data['seasons'])}</span>
        </div>
        <p style='color:#E6EDF3;line-height:1.7;margin:0;'>{dest_data['description']}</p>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**🎯 Top Highlights**")
        for h in dest_data["highlights"]:
            st.markdown(f"• {h}")
        st.markdown("**💡 Hidden Gem**")
        st.markdown(f"<div class='tip-box'>🔍 {dest_data['hidden_gem']}</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown("**💰 Estimated Cost Breakdown**")
        for k, v in dest_data["cost_breakdown"].items():
            st.markdown(
                f"<div style='display:flex;justify-content:space-between;font-size:0.9rem;margin-bottom:4px;'>"
                f"<span style='color:#8B949E;'>{k}</span>"
                f"<span style='color:#C9A84C;font-weight:600;'>{v}</span></div>",
                unsafe_allow_html=True)
        st.markdown("**🛂 Visa / Permits**")
        st.markdown(f"<div class='warn-box'>📋 {dest_data['permit']}</div>", unsafe_allow_html=True)
        st.markdown("**🛡️ Safety**")
        st.markdown(f"<div class='warn-box'>⚠️ {dest_data['safety']}</div>", unsafe_allow_html=True)

    st.markdown("---")

# ── Itinerary ─────────────────────────────────────────────────────────────────
top_name, top_data = results[0][1], results[0][2]
st.markdown(f'<div class="section-header">📅 {duration}-Day Itinerary — {top_data["emoji"]} {top_name}</div>', unsafe_allow_html=True)

for day_tuple in build_itinerary(top_data, duration):
    slots_html = "".join(f"<p>{s}</p>" for s in day_tuple[1:])
    st.markdown(f"""
    <div class="itinerary-day">
        <h4>{day_tuple[0]}</h4>
        {slots_html}
    </div>
    """, unsafe_allow_html=True)

# ── Packing ───────────────────────────────────────────────────────────────────
st.markdown(f'<div class="section-header">🎒 Packing Essentials — {top_name}</div>', unsafe_allow_html=True)
packing = top_data.get("packing", [])
pcols = st.columns(min(3, len(packing)))
chunk = max(1, -(-len(packing) // 3))  # ceiling division
for i, col in enumerate(pcols):
    with col:
        for item in packing[i * chunk:(i + 1) * chunk]:
            st.markdown(f"✓ {item}")

# ── Budget Tips ───────────────────────────────────────────────────────────────
st.markdown(f'<div class="section-header">💸 Pro Budget Tips — {top_name}</div>', unsafe_allow_html=True)
for tip in top_data.get("budget_tips", []):
    st.markdown(f"<div class='tip-box'>💡 {tip}</div>", unsafe_allow_html=True)

# ── Quick Comparison ──────────────────────────────────────────────────────────
if len(results) > 1:
    st.markdown('<div class="section-header">⚖️ Quick Comparison</div>', unsafe_allow_html=True)
    ccols = st.columns(len(results))
    for i, (sc, dn, dd) in enumerate(results):
        with ccols[i]:
            st.markdown(f"**{medals[i]} {dd['emoji']} {dn}**")
            st.markdown(f"<span style='color:#8B949E;font-size:0.83rem;'>Seasons: {', '.join(dd['seasons'])}</span>", unsafe_allow_html=True)
            fk, fv = list(dd["cost_breakdown"].items())[0]
            st.markdown(f"<span style='color:#C9A84C;font-size:0.83rem;'>{fk}: {fv}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#8B949E;font-size:0.8rem;'>{dd['description'][:90]}…</span>", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center;color:#8B949E;font-size:0.82rem;padding:1rem 0;'>
    🌍 WanderWise · Built with Streamlit · No API Key · Completely Free<br>
    <span style='color:#C9A84C;'>Adjust any filter on the left and click again to explore new destinations ✈️</span>
</div>
""", unsafe_allow_html=True)
