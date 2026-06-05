def policy_advice(query):

    q = query.lower()

    if "cyber" in q:

        return """
ASSESSMENT

Increasing cyber activity may threaten critical
infrastructure and digital resilience.

POLICY OPTIONS

1. Expand cyber cooperation

2. Improve intelligence sharing

3. Strengthen infrastructure protection

RECOMMENDATION

Prioritize cyber resilience and monitoring.

OUTLOOK

Elevated vigilance recommended.
"""

    elif "china" in q:

        return """
ASSESSMENT

Developments involving China may affect regional
security and economic relationships.

POLICY OPTIONS

1. Diplomatic engagement

2. Economic diversification

3. Strategic coordination

RECOMMENDATION

Balance engagement with risk management.

OUTLOOK

Monitor developments closely.
"""

    elif "russia" in q:

        return """
ASSESSMENT

Geopolitical developments may increase strategic
uncertainty.

POLICY OPTIONS

1. Monitor defense activity

2. Coordinate with allies

3. Assess economic impacts

RECOMMENDATION

Maintain strategic awareness.

OUTLOOK

Risk remains elevated.
"""

    return """
ASSESSMENT

Further analysis required.

POLICY OPTIONS

1. Collect additional intelligence

2. Monitor developments

3. Review strategic implications

RECOMMENDATION

Maintain awareness.

OUTLOOK

Uncertain.
"""
print(policy_advice("cyber"))