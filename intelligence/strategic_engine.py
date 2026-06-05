def generate_strategic_assessment(
    country,
    risk_score,
    events
):

    event_text = "\n".join(
        [f"• {e}" for e in events]
    )

    # ==========================
    # COUNTRY-SPECIFIC LOGIC
    # ==========================

    if country == "China":

        assessment = """
Recent geopolitical and cyber developments indicate
increasing strategic competition across the Indo-Pacific.

Military activities and technology restrictions suggest
continued pressure on regional stability.
"""

        drivers = """
• Military modernization
• Taiwan-related tensions
• Technology competition
• Cyber activity
"""

        implications = """
• Monitor regional security developments

• Assess supply-chain vulnerabilities

• Strengthen cyber resilience

• Track diplomatic engagement
"""

        forecast = """
Risk expected to remain elevated over the next 6–12 months.
"""

    elif country == "Russia":

        assessment = """
Military activity and geopolitical developments continue
to create elevated uncertainty across multiple regions.
"""

        drivers = """
• Defense activity
• Geopolitical tensions
• Strategic competition
"""

        implications = """
• Monitor sanctions environment

• Track defense developments

• Assess regional stability risks
"""

        forecast = """
Risk expected to remain high.
"""

    elif country == "India":

        assessment = """
Cyber incidents and regional developments indicate
increasing importance of digital and strategic security.
"""

        drivers = """
• Cybersecurity threats
• Digital infrastructure exposure
• Regional security concerns
"""

        implications = """
• Strengthen cyber defenses

• Monitor critical infrastructure

• Improve digital resilience
"""

        forecast = """
Moderately elevated risk expected.
"""

    elif country == "USA":

        assessment = """
Economic and climate-related developments continue
to influence strategic priorities.
"""

        drivers = """
• Economic conditions
• Climate challenges
• Strategic competition
"""

        implications = """
• Monitor economic indicators

• Assess climate resilience

• Track strategic partnerships
"""

        forecast = """
Risk expected to remain relatively stable.
"""

    else:

        assessment = """
Current developments require continued monitoring.
"""

        drivers = """
• Limited intelligence available
"""

        implications = """
• Maintain strategic awareness
"""

        forecast = """
Future developments remain uncertain.
"""

    return f"""
========================================
STRATEGIC ASSESSMENT
========================================

Country:
{country}

Risk Score:
{risk_score}/100

Recent Events:
{event_text}

----------------------------------------
ASSESSMENT
----------------------------------------

{assessment}

----------------------------------------
KEY DRIVERS
----------------------------------------

{drivers}

----------------------------------------
POLICY IMPLICATIONS
----------------------------------------

{implications}

----------------------------------------
FORECAST
----------------------------------------

{forecast}
"""