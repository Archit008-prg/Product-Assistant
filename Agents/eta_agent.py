def estimate_resolution_time(category):
    avg_times = {
        "Smartphones": "1 business day",
        "Televisions": "2 business days",
        "Air Conditioners": "3 business days"
    }
    return avg_times.get(category, "2-3 business days")
