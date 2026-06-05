from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def create_report(
    filename,
    summary,
    risk_df
):

    doc = SimpleDocTemplate(
        filename
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Global Intelligence Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            summary.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "Risk Rankings",
            styles["Heading2"]
        )
    )

    for _, row in risk_df.iterrows():

        content.append(
            Paragraph(
                f"{row['Country']} : {row['Risk Score']}",
                styles["BodyText"]
            )
        )

    doc.build(content)