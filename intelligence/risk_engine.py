def calculate_risk(category):

    scores = {
        "Cyber": 75,
        "Geopolitical": 80,
        "Economic": 60,
        "Climate": 50,
        "Unknown": 20
    }

    return scores.get(category, 20)


def risk_level(score):

    if score >= 80:
        return "CRITICAL"

    elif score >= 60:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    return "LOW"


def country_risk(country_events):

    if len(country_events) == 0:
        return 0

    total = 0

    for _, row in country_events.iterrows():

        total += calculate_risk(
            row["Category"]
        )

    return round(
        total / len(country_events)
    )