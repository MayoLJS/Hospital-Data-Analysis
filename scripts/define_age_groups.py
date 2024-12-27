# Define age groups
def age_group(age):
    if age <= 20:
        return "0-20"
    elif age <= 40:
        return "21-40"
    elif age <= 60:
        return "41-60"
    else:
        return "61+"
