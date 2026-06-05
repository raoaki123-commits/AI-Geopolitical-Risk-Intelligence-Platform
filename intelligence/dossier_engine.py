from intelligence.forecast_engine import (
    forecast_risk,
    trend_direction
)

def generate_dossier(
    country,
    risk_score,
    country_events
):

    event_count = len(country_events)

    forecast = forecast_risk(
        risk_score,
        event_count
    )

    trend = trend_direction(
        risk_score,
        forecast
    )

    confidence = "Low"

    if event_count >= 3:
        confidence = "Medium"

    if event_count >= 5:
        confidence = "High"

    event_list = "\n".join(
        [
            f"• {event}"
            for event in country_events["Event"]
        ]
    )

    return f"""
========================================
COUNTRY INTELLIGENCE DOSSIER
========================================

Country:
{country}

----------------------------------------
RISK OVERVIEW
----------------------------------------

Current Risk:
{risk_score}/100

Forecast Risk:
{forecast}/100

Trend:
{trend}

Confidence:
{confidence}

----------------------------------------
RECENT EVENTS
----------------------------------------

{event_list}

----------------------------------------
STRATEGIC DRIVERS
----------------------------------------

• Event Frequency

• Regional Stability

• Economic Conditions

• Cyber Activity

• Diplomatic Relations

----------------------------------------
POLICY IMPLICATIONS
----------------------------------------

• Monitor developments closely

• Assess strategic exposure

• Review critical dependencies

• Strengthen resilience planning

----------------------------------------
INTELLIGENCE OUTLOOK
----------------------------------------

Current indicators suggest continued monitoring
is required.

Future developments may significantly alter
the strategic environment.

========================================
END OF DOSSIER
========================================
"""