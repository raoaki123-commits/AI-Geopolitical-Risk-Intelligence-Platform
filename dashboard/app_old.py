import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import pandas as pd
import plotly.express as px

from intelligence.risk_engine import (
    risk_level,
    country_risk
)

from intelligence.intelligence_feed import (
    generate_alert
)

from intelligence.executive_engine import (
    executive_summary
)

from intelligence.event_manager import (
    add_event
)

from policy.brief_generator import (
    generate_brief
)
from reports.report_generator import (
    create_report
)
from intelligence.strategic_engine import (
    generate_strategic_assessment
)
from intelligence.hotspot_engine import (
    generate_hotspots
)
from intelligence.policy_advisor import (
    policy_advice
)
from intelligence.dossier_engine import (
    generate_dossier
)
# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Global Intelligence AI System",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Global Intelligence AI System")

# ==================================
# LOAD DATA
# ==================================

countries = pd.read_csv(
    "data/countries.csv"
)

events = pd.read_csv(
    "data/events.csv"
)

# ==================================
# AUTO RISK ENGINE
# ==================================

risk_scores = {}

for country in countries["Country"]:

    country_events = events[
        events["Country"] == country
    ]

    risk_scores[country] = country_risk(
        country_events
    )

risk_df = pd.DataFrame({
    "Country": list(risk_scores.keys()),
    "Risk Score": list(risk_scores.values())
})

risk_df = risk_df.sort_values(
    by="Risk Score",
    ascending=False
)

# ==================================
# COUNTRY CODE FUNCTION
# ==================================

def get_country_code(name):

    mapping = {
        "USA": "USA",
        "UK": "GBR",
        "China": "CHN",
        "India": "IND",
        "Russia": "RUS"
    }

    return mapping.get(name)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Overview",
        "Executive Briefing",
        "Global Risk Center",
        "World Risk Map",
        "Intelligence Feed",
        "Policy Advisor",
        "Country Dossier",
        "Add Event",
        "Country Intelligence",
        "Trends",
        "About"
    ]
)

# ==================================
# OVERVIEW
# ==================================

if page == "Overview":

    st.header(
        "📊 Executive Intelligence Dashboard"
    )

    total_events = len(events)

    total_countries = len(countries)

    highest_risk_country = (
        risk_df.iloc[0]["Country"]
    )

    avg_risk = round(
        risk_df["Risk Score"].mean()
    )

    most_active_country = (
        events["Country"]
        .value_counts()
        .idxmax()
    )

    most_common_threat = (
        events["Category"]
        .value_counts()
        .idxmax()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Events",
            total_events
        )

    with c2:
        st.metric(
            "Countries",
            total_countries
        )

    with c3:
        st.metric(
            "Highest Risk",
            highest_risk_country
        )

    with c4:
        st.metric(
            "Average Risk",
            avg_risk
        )

    st.divider()

    c5, c6 = st.columns(2)

    with c5:
        st.metric(
            "Most Active Country",
            most_active_country
        )

    with c6:
        st.metric(
            "Most Common Threat",
            most_common_threat
        )

    st.divider()

    st.subheader(
        "Top Risk Countries"
    )

    st.dataframe(
        risk_df,
        use_container_width=True
    )

    st.divider()

    st.subheader(
        "Executive Summary"
    )
    

    summary = executive_summary(
        risk_df,
        events
    )

    st.text_area(
        "",
        summary,
        height=200
    )
    st.divider()

    st.subheader(
    "🔥 Emerging Global Hotspots"
)

    hotspots = generate_hotspots(
    countries["Country"],
    events,
    risk_scores
)

    for hotspot in hotspots[:5]:

     st.write(
        f"""
  {hotspot['Country']}

Current Risk: {hotspot['Current Risk']}

Forecast: {hotspot['Forecast']}

Trend: {hotspot['Trend']}
"""
    )

    st.divider()
    if st.button("Generate Intelligence PDF Report"):

      filename = "global_intelligence_report.pdf"

    create_report(
        filename,
        summary,
        risk_df
    )

    st.success(
        f"Report created: {filename}"
    )
# ==================================
# EXECUTIVE BRIEFING
# ==================================

elif page == "Executive Briefing":

    st.header(
        "🌍 Executive Intelligence Briefing"
    )

    highest_risk = risk_df.iloc[0]

    dominant_threat = (
        events["Category"]
        .value_counts()
        .idxmax()
    )

    st.subheader(
        "Highest Risk Actor"
    )

    st.write(
        highest_risk["Country"]
    )

    st.write(
        f"Risk Score: {highest_risk['Risk Score']}"
    )

    st.divider()

    st.subheader(
        "Dominant Threat"
    )

    st.write(
        dominant_threat
    )

    st.divider()

    st.subheader(
        "Strategic Outlook"
    )

    st.write(
        """
Global competition remains elevated.

Cyber, economic, and geopolitical risks
continue to influence the strategic landscape.

Continued monitoring is recommended.
"""
    )

    st.divider()

    st.subheader(
        "Recommended Focus Areas"
    )

    st.write(
        """
• Cyber Resilience

• Strategic Technology

• Supply Chain Security

• Regional Stability

• Diplomatic Engagement
"""
    )    

# ==================================
# GLOBAL RISK CENTER
# ==================================

elif page == "Global Risk Center":

    st.header(
        "🌍 Global Risk Center"
    )

    st.dataframe(
        risk_df,
        use_container_width=True
    )

    fig = px.bar(
        risk_df,
        x="Country",
        y="Risk Score",
        title="Country Risk Scores"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================
# WORLD RISK MAP
# ==================================

elif page == "World Risk Map":

    st.header(
        "🌍 World Risk Map"
    )

    map_df = risk_df.copy()

    map_df["ISO"] = (
        map_df["Country"]
        .apply(get_country_code)
    )

    fig = px.choropleth(
        map_df,
        locations="ISO",
        color="Risk Score",
        hover_name="Country",
        color_continuous_scale="Reds",
        title="Global Risk Map"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================
# INTELLIGENCE FEED
# ==================================

elif page == "Intelligence Feed":

    st.header(
        "🧠 Global Intelligence Feed"
    )

    for _, row in events.iterrows():

        alert = generate_alert(
            row["Country"],
            row["Event"],
            row["Category"]
        )

        st.subheader(
            f"{alert['Severity']} | {row['Country']}"
        )

        st.write(
            f"**Event:** {row['Event']}"
        )

        st.write(
            f"**Category:** {row['Category']}"
        )

        st.write(
            f"**Strategic Significance:** {alert['Analysis']}"
        )

        st.divider()
# ==================================
# POLICY ADVISOR
# ==================================

elif page == "Policy Advisor":

    st.header(
        "🧠 AI Policy Advisor"
    )

    query = st.text_area(
        "Enter policy question"
    )

    if st.button(
        "Generate Assessment"
    ):

        result = policy_advice(
            query
        )

        st.text_area(
            "",
            result,
            height=400
        )     
# ==================================
# COUNTRY DOSSIER
# ==================================

elif page == "Country Dossier":

    st.header(
        "📁 Country Intelligence Dossier"
    )

    selected_country = st.selectbox(
        "Select Country",
        countries["Country"]
    )

    country_events = events[
        events["Country"] == selected_country
    ]

    risk = risk_scores[
        selected_country
    ]

    dossier = generate_dossier(
        selected_country,
        risk,
        country_events
    )

    st.text_area(
        "",
        dossier,
        height=700
    )           

# ==================================
# ADD EVENT
# ==================================

elif page == "Add Event":

    st.header(
        "➕ Add Intelligence Event"
    )

    event_date = st.date_input(
        "Date"
    )

    country = st.selectbox(
        "Country",
        countries["Country"]
    )

    event_text = st.text_input(
        "Event Description"
    )

    category = st.selectbox(
        "Category",
        [
            "Geopolitical",
            "Cyber",
            "Economic",
            "Climate"
        ]
    )

    if st.button(
        "Add Event"
    ):

        add_event(
            str(event_date),
            country,
            event_text,
            category
        )

        st.success(
            "Event Added Successfully!"
        )

        st.info(
            "Refresh the page to see updated rankings."
        )

# ==================================
# COUNTRY INTELLIGENCE
# ==================================

elif page == "Country Intelligence":

    st.header(
        "Country Intelligence"
    )

    country = st.selectbox(
        "Select Country",
        countries["Country"]
    )

    country_info = countries[
        countries["Country"] == country
    ].iloc[0]

    auto_risk = risk_scores[country]

    level = risk_level(
        auto_risk
    )

    st.metric(
        "Country Risk",
        auto_risk
    )

    st.success(
        f"Risk Level: {level}"
    )

    st.subheader(
        "Country Statistics"
    )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Population",
            f"{country_info['Population']:,}"
        )

        st.metric(
            "GDP",
            f"${country_info['GDP']:,}"
        )

    with c2:

        st.metric(
            "Military Spending",
            f"${country_info['Military_Spending']:,}"
        )

        st.metric(
            "Region",
            country_info["Region"]
        )

        st.divider()

    country_events = events[
        events["Country"] == country
    ]

    st.dataframe(
        country_events
    )

    event_list = (
        country_events["Event"]
        .tolist()
    )

    assessment = generate_strategic_assessment(
        country,
        auto_risk,
        event_list
    )

    st.subheader(
        "Strategic Assessment"
    )

    st.text_area(
        "",
        assessment,
        height=500
    )

# ==================================
# TRENDS
# ==================================

elif page == "Trends":

    st.header(
        "Trend Analysis"
    )

    counts = (
        events["Category"]
        .value_counts()
        .reset_index()
    )

    counts.columns = [
        "Category",
        "Count"
    ]

    fig = px.bar(
        counts,
        x="Category",
        y="Count",
        title="Events by Category"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.dataframe(
        counts
    )

# ==================================
# ABOUT
# ==================================

elif page == "About":

    st.header(
        "About This Project"
    )

    st.write("""
Global Intelligence AI System

Features:
- Executive Dashboard
- Risk Engine
- Intelligence Feed
- World Risk Map
- Event Submission System
- Policy Brief Generator
- Trend Analysis

Developed by Akhilesh
""")