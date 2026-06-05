from intelligence.forecast_engine import (
    forecast_risk,
    trend_direction
)

def generate_hotspots(
    countries,
    events,
    risk_scores
):

    hotspots = []

    for country in countries:

        country_events = events[
            events["Country"] == country
        ]

        event_count = len(
            country_events
        )

        current_risk = risk_scores[
            country
        ]

        forecast = forecast_risk(
            current_risk,
            event_count
        )

        trend = trend_direction(
            current_risk,
            forecast
        )

        hotspots.append(
            {
                "Country": country,
                "Current Risk": current_risk,
                "Forecast": forecast,
                "Trend": trend
            }
        )

    hotspots.sort(
        key=lambda x: x["Forecast"],
        reverse=True
    )

    return hotspots