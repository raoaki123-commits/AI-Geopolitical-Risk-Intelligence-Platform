def executive_summary(risk_df, events):

    top_country = risk_df.iloc[0]["Country"]

    top_risk = risk_df.iloc[0]["Risk Score"]

    top_category = (
        events["Category"]
        .value_counts()
        .idxmax()
    )

    summary = f"""
Executive Intelligence Summary

Highest Risk Country:
{top_country} ({top_risk})

Most Common Threat:
{top_category}

Assessment:
Current intelligence indicates elevated activity across multiple domains.
Continued monitoring is recommended.
"""

    return summary