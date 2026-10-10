class InvalidIncidentError(Exception):
    pass

def classify_severity(temp: float) -> str:
    if temp >= 100:
        return "critical"
    if temp >= 85:
        return "warning"
    return "normal"

def get_temp(incident: dict) -> float:
    if "temp" not in incident:
        raise InvalidIncidentError(f"Incident {incident.get('id')} has no temp")
    return incident["temp"]

records = [{"id": 1, "temp": 90}, {"id": 2}, {"id": 3, "temp": 110}]

for r in records:
    try:
        print(r["id"], classify_severity(get_temp(r)))
    except InvalidIncidentError as e:
        print("SKIPPED:", e)