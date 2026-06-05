def forecast_risk(current_risk, event_count):

    increase = min(
        event_count * 2,
        15
    )

    forecast = min(
        current_risk + increase,
        100
    )

    return forecast


def trend_direction(
    current_risk,
    forecast
):

    if forecast > current_risk:
        return "↑ Rising"

    elif forecast < current_risk:
        return "↓ Falling"

    return "→ Stable"