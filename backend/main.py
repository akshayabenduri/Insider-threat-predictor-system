from fastapi import FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

class SecurityEvent(BaseModel):
    user: str
    event: str
    details: str

def calculate_risk(event_type: str):
    # Your Risk Matrix Logic (Report Page 7)
    risk_map = {
        "login_failure": 5,          # Low Risk
        "privilege_escalation": 20,  # High Risk
        "usb_insert": 25,            # High Risk
        "suspicious_process": 25     # High Risk
    }
    score = risk_map.get(event_type, 1)
    level = "LOW" if score <= 6 else "MEDIUM" if score <= 12 else "HIGH"
    return score, level

@app.post("/event")
async def receive_event(item: SecurityEvent):
    score, level = calculate_risk(item.event)
    return {
        "risk_score": score,
        "risk_level": level,
        "timestamp": str(datetime.datetime.now())
    }