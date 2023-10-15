
def earliestFellows(fellowTimes):
    # fellowTimes = {"oliver": 3, "tobey": 3}
    result = []
    earliestTime = float("inf")
    for fellow,time in fellowTimes.items():
        if time < earliestTime:
            earliestTime = time
            result = [fellow]
        elif time == earliestTime:
            result.append(fellow)
    return result

print(earliestFellows({"oliver": 1, "pixel": 2, "pinky": 1}))


