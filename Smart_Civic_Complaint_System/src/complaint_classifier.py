def classify_complaint(text):
    text = str(text).lower()

    electricity_keywords = [
        "power", "electricity", "voltage", "current",
        "transformer", "meter"
    ]

    water_keywords = [
        "water", "leak", "pipeline", "tap", "overflow"
    ]

    sanitation_keywords = [
        "garbage", "waste", "toilet", "drain", "sewage"
    ]

    road_keywords = [
        "road", "pothole", "traffic", "street",
        "speed breaker", "signal"
    ]

    if any(word in text for word in electricity_keywords):
        return "Electricity"
    elif any(word in text for word in water_keywords):
        return "Water Supply"
    elif any(word in text for word in sanitation_keywords):
        return "Sanitation"
    elif any(word in text for word in road_keywords):
        return "Roads"
    else:
        return "General"
