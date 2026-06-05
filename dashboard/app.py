import streamlit as st
import pandas as pd
import plotly.express as px
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Strategic Intelligence Platform",
    page_icon="🌍",
    layout="wide"
)

# =====================================
# DARK THEME
# =====================================

st.markdown("""
<style>

.main {
    background-color: #0A0F1C;
}

.block-container {
    padding-top: 1rem;
    max-width: 95%;
}

/* Remove Streamlit padding */

section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Main title */

.main-title {
    font-size: 38px;
    font-weight: 700;
    color: white;
    padding-bottom: 10px;
}

/* Intelligence cards */

.intel-card {
    background: #141B2D;
    border-left: 5px solid #00C2FF;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 15px;
}

.intel-card h3 {
    color: white;
}

.intel-card p {
    color: #D1D5DB;
}

/* Alert cards */

.alert-critical {
    background:#3A0F0F;
    border-left:6px solid red;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

.alert-high {
    background:#3A240F;
    border-left:6px solid orange;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

.alert-medium {
    background:#1F2937;
    border-left:6px solid yellow;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

.alert-low {
    background:#0F2A1A;
    border-left:6px solid green;
    padding:15px;
    border-radius:10px;
    margin-bottom:10px;
}

/* Metric cards */

.metric-box {
    background:#141B2D;
    border-radius:12px;
    padding:15px;
    text-align:center;
    border:1px solid #25324A;
}

.metric-title {
    color:#9CA3AF;
    font-size:14px;
}

.metric-value {
    color:white;
    font-size:28px;
    font-weight:bold;
}

/* Section headers */

.section-header {
    color:white;
    font-size:24px;
    font-weight:700;
    padding-top:10px;
    padding-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD DATA
# =====================================

countries = pd.read_csv("data/countries.csv")
events = pd.read_csv("data/events.csv")
risks = pd.read_csv("data/risks.csv")
regions = pd.read_csv("data/regions.csv")

risk_dict = dict(
    zip(
        risks["Country"],
        risks["Risk"]
    )
)

# =====================================
# HELPER FUNCTIONS
# =====================================

def threat_level():

    avg_risk = risks["Risk"].mean()

    if avg_risk >= 75:
        return "CRITICAL"

    elif avg_risk >= 60:
        return "ELEVATED"

    return "MODERATE"


def top_hotspots():

    return risks.sort_values(
        by="Risk",
        ascending=False
    ).head(5)


# =====================================
# SIDEBAR
# =====================================

st.sidebar.markdown("""
# 🌍 GICS

### Global Intelligence &
### Command System

---
""")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Briefing",
        "Global Watchlist",
        "Strategic Hotspots",
        "Regional Intelligence",
        "Threat Matrix",
        "World Risk Map",
        "Country Dossiers",
        "Intelligence Feed",
        "Policy Advisor",
        "Reports Center"
        
    ]
)

# =====================================
# EXECUTIVE BRIEFING
# =====================================

if page == "Executive Briefing":

    st.markdown("""
<div class='main-title'>
🌍 STRATEGIC INTELLIGENCE COMMAND CENTER
</div>
""", unsafe_allow_html=True)

    highest_risk = risks.sort_values(
        by="Risk",
        ascending=False
    ).iloc[0]

    current_threat = threat_level()

    if current_threat == "CRITICAL":
        banner_color = "#7F1D1D"

    elif current_threat == "ELEVATED":
        banner_color = "#78350F"

    else:
        banner_color = "#14532D"

    st.markdown(
        f"""
<div style="
background:{banner_color};
padding:20px;
border-radius:12px;
margin-bottom:20px;
">

<h2 style="color:white;">
GLOBAL THREAT LEVEL: {current_threat}
</h2>

</div>
""",
        unsafe_allow_html=True
    )

    # GLOBAL SNAPSHOT

    snapshot1, snapshot2, snapshot3, snapshot4 = st.columns(4)

    with snapshot1:
        st.metric(
            "Avg Risk",
            round(risks["Risk"].mean(), 1)
        )

    with snapshot2:
        st.metric(
            "Countries",
            len(countries)
        )

    with snapshot3:
        st.metric(
            "Events",
            len(events)
        )

    with snapshot4:
        st.metric(
            "Regions",
            len(regions)
        )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
<div class='metric-box'>
<div class='metric-title'>Countries Monitored</div>
<div class='metric-value'>
30
</div>
</div>
""", unsafe_allow_html=True)

    with col2:

        st.markdown(
            f"""
<div class='metric-box'>
<div class='metric-title'>Events Tracked</div>
<div class='metric-value'>
{len(events)}
</div>
</div>
""",
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
<div class='metric-box'>
<div class='metric-title'>Highest Risk Actor</div>
<div class='metric-value'>
{highest_risk['Country']}
</div>
</div>
""",
            unsafe_allow_html=True
        )

    st.divider()

    left, right = st.columns([2, 1])

    with left:

        st.markdown("""
<div class='intel-card'>

<h3>Strategic Outlook</h3>

<p>
Global geopolitical competition remains elevated.

Technology rivalry, cyber operations,
regional conflicts and energy security
continue shaping the strategic environment.

Analysts should monitor escalation risks,
critical infrastructure threats and
major-power competition.
</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class='intel-card'>

<h3>Policy Priorities</h3>

<p>

• Cyber Resilience

• Technology Security

• Supply Chain Protection

• Regional Stability

• Strategic Diplomacy

</p>

</div>
""", unsafe_allow_html=True)

    with right:

        hotspots = top_hotspots()

        st.markdown(
            "<div class='section-header'>Top Strategic Hotspots</div>",
            unsafe_allow_html=True
        )

        for _, row in hotspots.iterrows():

            st.markdown(
                f"""
<div class='alert-high'>

<b>{row['Country']}</b>

<br>

Risk Score: {row['Risk']}

</div>
""",
                unsafe_allow_html=True
            )

    st.divider()

    st.subheader(
        "Latest Intelligence Alerts"
    )

    latest_events = events.tail(5)

    for _, row in latest_events.iterrows():

        severity = row["Severity"]

        css_class = "alert-medium"

        if severity == "Critical":
            css_class = "alert-critical"

        elif severity == "High":
            css_class = "alert-high"

        elif severity == "Low":
            css_class = "alert-low"

        st.markdown(
            f"""
<div class='{css_class}'>

<b>{row['Country']}</b>

<br>

{row['Category']} | {row['Severity']}

<br><br>

{row['Description']}

</div>
""",
            unsafe_allow_html=True
        )

    st.divider()

    st.subheader(
        "Global Risk Ranking"
    )

    ranking = risks.sort_values(
        by="Risk",
        ascending=False
    )

    st.dataframe(
        ranking,
        use_container_width=True
    )
# =====================================
# GLOBAL WATCHLIST
# =====================================

elif page == "Global Watchlist":

    st.title("👁️ Global Watchlist")

    watchlist = risks.sort_values(
        by="Risk",
        ascending=False
    )

    for _, row in watchlist.iterrows():

        country = row["Country"]
        risk = row["Risk"]

        country_data = countries[
            countries["Country"] == country
        ]

        if len(country_data) > 0:

            country_data = country_data.iloc[0]

            st.markdown(
                f"""
### {country}

Risk Score: {risk}/100

Region: {country_data['Region']}

Strategic Importance: {country_data['Strategic_Importance']}
"""
            )

            st.progress(
                min(risk / 100, 1.0)
            )

            st.divider()    

# =====================================
# STRATEGIC HOTSPOTS
# =====================================

elif page == "Strategic Hotspots":

    st.title("🔥 Strategic Hotspots")

    hotspots = risks.sort_values(
        by="Risk",
        ascending=False
    ).head(10)

    for rank, (_, row) in enumerate(
        hotspots.iterrows(),
        start=1
    ):

        country = row["Country"]
        risk = row["Risk"]

        country_events = events[
            events["Country"] == country
        ]

        st.subheader(
            f"{rank}. {country}"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Current Risk",
                risk
            )

        with col2:
            forecast = min(
                risk + len(country_events) * 2,
                100
            )

            st.metric(
                "Forecast Risk",
                forecast
            )

        if len(country_events) > 0:

            latest = country_events.iloc[-1]

            st.write(
                f"**Latest Development:** {latest['Description']}"
            )

            st.caption(
                f"{latest['Category']} | {latest['Severity']} | Confidence: {latest['Confidence']}"
            )

        st.divider()
# =====================================
# REGIONAL INTELLIGENCE
# =====================================

elif page == "Regional Intelligence":

    st.title("🌎 Regional Intelligence Center")

    selected_region = st.selectbox(
        "Select Region",
        regions["Region"]
    )

    region_data = regions[
        regions["Region"] == selected_region
    ].iloc[0]

    st.subheader(
        f"{selected_region} Assessment"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Regional Risk",
            region_data["Risk"]
        )

    with col2:

        countries_in_region = countries[
            countries["Region"] == selected_region
        ]

        st.metric(
            "Countries Monitored",
            len(countries_in_region)
        )

    st.divider()

    st.subheader(
        "Strategic Assessment"
    )

    st.info(
        region_data["Summary"]
    )

    st.divider()

    st.subheader(
        "Regional Countries"
    )

    if len(countries_in_region) > 0:

        display = countries_in_region[
            [
                "Country",
                "Political_Stability",
                "Technology_Index",
                "Strategic_Importance"
            ]
        ]

        st.dataframe(
            display,
            use_container_width=True
        )  
# =====================================
# WORLD RISK MAP
# =====================================

elif page == "World Risk Map":

    st.title("🌍 Global Strategic Risk Map")

    map_df = risks.copy()

    fig = px.choropleth(
        map_df,
        locations="Country",
        locationmode="country names",
        color="Risk",
        hover_name="Country",
        color_continuous_scale="Reds",
        title="Global Risk Distribution"
    )

    fig.update_layout(
        height=700,
        margin=dict(
            l=0,
            r=0,
            t=50,
            b=0
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "Highest Risk Countries"
    )

    st.dataframe(
        risks.sort_values(
            by="Risk",
            ascending=False
        ).head(10),
        use_container_width=True
    )              


# =====================================
# THREAT MATRIX
# =====================================

elif page == "Threat Matrix":

    st.title("⚠️ Global Threat Matrix")

    threat_data = []

    for category in events["Category"].unique():

        count = len(
            events[
                events["Category"] == category
            ]
        )

        if count >= 5:
            risk_level = "High"
            trend = "↑"

        elif count >= 2:
            risk_level = "Medium"
            trend = "→"

        else:
            risk_level = "Low"
            trend = "↓"

        threat_data.append(
            {
                "Threat Area": category,
                "Risk Level": risk_level,
                "Trend": trend,
                "Events": count
            }
        )

    threat_df = pd.DataFrame(
        threat_data
    )

    st.dataframe(
        threat_df,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "Assessment"
    )

    st.info("""
The threat matrix summarizes the most active
global risk categories currently being monitored.

Categories with increasing event frequency
should be prioritized for strategic assessment.
""")        
# =====================================
# COUNTRY DOSSIERS
# =====================================

elif page == "Country Dossiers":

    st.title("📁 Country Intelligence Dossier")

    selected_country = st.selectbox(
        "Select Country",
        countries["Country"].sort_values()
    )

    country_data = countries[
        countries["Country"] == selected_country
    ].iloc[0]

    risk = risk_dict.get(
        selected_country,
        50
    )

    country_events = events[
        events["Country"] == selected_country
    ]

    forecast = min(
        risk + len(country_events) * 2,
        100
    )

    st.divider()

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Executive Summary")

        st.write(
            f"""
{selected_country} is a strategically important actor
within the {country_data['Region']} region.

Current monitoring indicates a risk score of {risk}/100,
with forecast indicators suggesting a projected risk
level of {forecast}/100.

Analysts should continue monitoring political,
economic, cyber and geopolitical developments.
"""
        )

        st.subheader("Strategic Indicators")

        indicators = pd.DataFrame(
            {
                "Indicator": [
                    "Political Stability",
                    "Technology Index",
                    "Energy Security",
                    "Climate Risk",
                    "Cyber Risk"
                ],
                "Score": [
                    country_data["Political_Stability"],
                    country_data["Technology_Index"],
                    country_data["Energy_Security"],
                    country_data["Climate_Risk"],
                    country_data["Cyber_Risk"]
                ]
            }
        )

        st.dataframe(
            indicators,
            use_container_width=True
        )

    with right:

        st.subheader("Country Profile")

        st.write(
            f"**Region:** {country_data['Region']}"
        )

        st.write(
            f"**Population:** {country_data['Population']:,}"
        )

        st.write(
            f"**GDP:** ${country_data['GDP']:,}"
        )

        st.write(
            f"**Military Spending:** ${country_data['Military_Spending']:,}"
        )

        st.metric(
            "Current Risk",
            risk
        )

        st.metric(
            "Forecast Risk",
            forecast
        )

    st.divider()

    st.subheader(
        "Recent Intelligence Developments"
    )

    if len(country_events) > 0:

        for _, event in country_events.iterrows():

            st.markdown(
                f"""
### {event['Category']} | {event['Severity']}

**Actor:** {event['Actor']}

**Target:** {event['Target']}

**Impact Score:** {event['Impact_Score']}

**Confidence:** {event['Confidence']}

{event['Description']}
"""
            )

            st.divider()

    else:

        st.info(
            "No intelligence events available."
        )

    st.subheader(
        "Policy Implications"
    )

    st.info(
        f"""
Strategic monitoring of {selected_country}
should prioritize cyber resilience,
regional stability, economic security
and technology competition.

Current indicators suggest continued
assessment is recommended.
"""
    )

# =====================================
# INTELLIGENCE FEED
# =====================================

elif page == "Intelligence Feed":

    st.title("📡 Global Intelligence Feed")

    feed = events.sort_values(
        by="Date",
        ascending=False
    )

    for _, event in feed.iterrows():

        severity = event["Severity"]

        if severity == "Critical":

            st.error(
                f"{event['Country']} | {event['Category']}"
            )

        elif severity == "High":

            st.warning(
                f"{event['Country']} | {event['Category']}"
            )

        else:

            st.info(
                f"{event['Country']} | {event['Category']}"
            )

        st.write(
            f"**Date:** {event['Date']}"
        )

        st.write(
            f"**Actor:** {event['Actor']}"
        )

        st.write(
            f"**Target:** {event['Target']}"
        )

        st.write(
            f"**Impact Score:** {event['Impact_Score']}"
        )

        st.write(
            event["Description"]
        )

        st.caption(
            f"Confidence: {event['Confidence']}"
        )

        st.divider()
# =====================================
# POLICY ADVISOR
# =====================================

elif page == "Policy Advisor":

    st.title("🧠 Strategic Policy Advisor")

    selected_country = st.selectbox(
        "Policy Target Country",
        countries["Country"].sort_values(),
        key="policy_country"
    )

    country_data = countries[
        countries["Country"] == selected_country
    ].iloc[0]

    risk = risk_dict.get(
        selected_country,
        50
    )

    st.subheader(
        f"Policy Assessment: {selected_country}"
    )

    if risk >= 85:

        recommendation = """
Priority attention recommended.

Escalation risks are significant.
Increase monitoring, strengthen diplomatic
engagement and prepare contingency planning.
"""

    elif risk >= 70:

        recommendation = """
Enhanced monitoring recommended.

Maintain active engagement and assess
emerging security, economic and cyber risks.
"""

    elif risk >= 50:

        recommendation = """
Routine monitoring recommended.

Track developments and maintain
regional awareness.
"""

    else:

        recommendation = """
Low immediate concern.

Maintain strategic observation
and periodic review.
"""

    st.info(recommendation)

    st.divider()

    st.subheader("Strategic Indicators")

    st.write(
        f"Cyber Risk: {country_data['Cyber_Risk']}"
    )

    st.write(
        f"Political Stability: {country_data['Political_Stability']}"
    )

    st.write(
        f"Technology Index: {country_data['Technology_Index']}"
    )

    st.write(
        f"Energy Security: {country_data['Energy_Security']}"
    )

    st.write(
        f"Strategic Importance: {country_data['Strategic_Importance']}"
    )

    st.divider()

    st.subheader("Policy Priorities")

    priorities = []

    if country_data["Cyber_Risk"] >= 70:
        priorities.append("Cyber Security")

    if country_data["Climate_Risk"] >= 70:
        priorities.append("Climate Resilience")

    if country_data["Strategic_Importance"] >= 85:
        priorities.append("Strategic Engagement")

    if country_data["Political_Stability"] <= 50:
        priorities.append("Political Risk Monitoring")

    if len(priorities) == 0:
        priorities.append("Routine Strategic Monitoring")

    for item in priorities:
        st.success(item)


# =====================================
# REPORTS CENTER
# =====================================

elif page == "Reports Center":

    st.title("📄 Intelligence Reports Center")

    st.subheader("Global Risk Overview")

    top_risks = risks.sort_values(
        by="Risk",
        ascending=False
    ).head(10)

    st.dataframe(
        top_risks,
        use_container_width=True
    )

    st.divider()

    st.subheader("Executive Assessment")

    highest = top_risks.iloc[0]["Country"]

    st.info(
        f"""
Current assessment indicates elevated
global strategic competition.

Highest monitored risk:
{highest}

Primary drivers include:

• Geopolitical competition

• Cyber operations

• Regional conflicts

• Technology security

• Supply chain resilience

Analysts should continue monitoring
high-risk actors and emerging hotspots.
"""
    )

    st.divider()

    st.subheader("Top 10 Strategic Risks")

    for rank, (_, row) in enumerate(
        top_risks.iterrows(),
        start=1
    ):

        st.write(
            f"{rank}. {row['Country']} — Risk {row['Risk']}"
        )

    st.divider()

    st.subheader("Dataset Summary")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Countries",
            len(countries)
        )

    with col2:
        st.metric(
            "Events",
            len(events)
        )

    with col3:
        st.metric(
            "Average Risk",
            round(risks["Risk"].mean(), 1)
        )      
