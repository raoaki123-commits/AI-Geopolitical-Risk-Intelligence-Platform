def generate_alert(country, event, category):

    if category == "Geopolitical":

        severity = "🔴 HIGH"

        analysis = """
Potential impact on regional stability and
international relations.
"""

    elif category == "Cyber":

        severity = "🟠 ELEVATED"

        analysis = """
Potential threat to digital infrastructure and
national security systems.
"""

    elif category == "Economic":

        severity = "🟡 MODERATE"

        analysis = """
May influence markets, trade flows,
and economic performance.
"""

    elif category == "Climate":

        severity = "🟢 WATCH"

        analysis = """
Potential environmental and humanitarian implications.
"""

    else:

        severity = "UNKNOWN"

        analysis = """
Further assessment required.
"""

    return {
        "Severity": severity,
        "Analysis": analysis
    }