def generate_brief(country, risk, events):

    events_text = "\n".join(
        [f"• {event}" for event in events]
    )

    if country == "China":

        assessment = """
Recent semiconductor restrictions and military drills
suggest rising strategic competition and increasing
regional tensions.
"""

        implications = """
Monitor technology supply chains, regional security
developments, and trade relationships.
"""

        outlook = """
Risk likely to remain elevated over the medium term.
"""

    elif country == "Russia":

        assessment = """
Military activity and geopolitical developments indicate
continued strategic uncertainty.
"""

        implications = """
Monitor regional stability, sanctions, and defense activity.
"""

        outlook = """
Risk expected to remain high.
"""

    elif country == "India":

        assessment = """
Cybersecurity incidents and regional developments
highlight increasing digital security concerns.
"""

        implications = """
Strengthen cyber resilience and monitor regional dynamics.
"""

        outlook = """
Risk likely to remain moderately high.
"""

    elif country == "USA":

        assessment = """
Climate and economic developments continue to shape
strategic priorities.
"""

        implications = """
Monitor economic indicators and climate-related risks.
"""

        outlook = """
Risk expected to remain stable.
"""

    else:

        assessment = """
Current developments require continued monitoring.
"""

        implications = """
Maintain strategic awareness.
"""

        outlook = """
Future developments remain uncertain.
"""

    report = f"""
COUNTRY INTELLIGENCE BRIEF

Country: {country}

Risk Score: {risk}/100

Recent Events

{events_text}

Strategic Assessment

{assessment}

Policy Implications

{implications}

Outlook

{outlook}
"""

    return report