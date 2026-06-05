def classify_event(text):

    text = text.lower()

    if "cyber" in text or "ransomware" in text:
        return "Cyber"

    elif "military" in text or "border" in text:
        return "Geopolitical"

    elif "climate" in text:
        return "Climate"

    elif "export" in text or "economy" in text:
        return "Economic"

    return "Unknown"