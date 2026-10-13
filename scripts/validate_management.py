"""Fail-closed static validation of the Growth Manager coordination records.

Does not invoke agents, providers, Slack, or write business systems.
"""
from pathlib import Path
import json
import sys

root=Path(__file__).resolve().parents[1]
base=root/"operations"/"management-system"
errors=[]
def load(name):
    path=base/name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{name}: invalid or missing JSON: {exc}")
        return {}

cal=load("operating-calendar.json")
score=load("team-scorecard.json")
board=load("task-board.json")
if cal.get("owner")!="Growth Manager" or score.get("owner")!="Growth Manager" or board.get("owner")!="Growth Manager":
    errors.append("Growth Manager must be the only coordination owner")
events=cal.get("events",[])
if len(events)<5 or len({x.get("id") for x in events})!=len(events):
    errors.append("Expected >=5 distinct calendar events")
for x in events:
    if x.get("autonomous_agent_run") is not False:
        errors.append(f"Calendar item {x.get('id')} must not claim native agent runtime")
    if x.get("activation")=="MANUAL_ONLY" and x.get("status") in ("DONE","COMPLETED","ACTIVE_SCHEDULED"):
        errors.append(f"Manual-only calendar item {x.get('id')} is falsely marked active/done")
    if x.get("activation")=="CHATGPT_AUTOMATION_ENABLED" and x.get("status")!="SCHEDULED_NOT_YET_RUN":
        errors.append(f"Unverified scheduled task {x.get('id')} was misclassified")

# Owner-approved work windows are not native-agent schedules.
by_id={e.get("id"):e for e in events}
expected={
    "CAL-WEBSITE-WEEKLY":("WEEKLY_SUNDAY","22:30","MANUAL_ONLY"),
    "CAL-DATA-WEEKLY":("WEEKLY_MONDAY","APPROX_08:00","CHATGPT_AUTOMATION_ENABLED"),
    "CAL-SEO-WEEKLY":("WEEKLY_MONDAY","APPROX_10:00","CHATGPT_AUTOMATION_ENABLED"),
    "CAL-GROWTH-WEEKLY":("WEEKLY_MONDAY","12:00","MANUAL_ONLY"),
}
for event_id,(cadence,time,activation) in expected.items():
    e=by_id.get(event_id,{})
    if (e.get("cadence"),e.get("time"),e.get("activation"))!=(cadence,time,activation):
        errors.append(f"Owner-approved schedule drift: {event_id}")
    if e.get("approved_time_slot") is not True:
        errors.append(f"Owner-approved time not recorded: {event_id}")
for event_id in ("CAL-WEBSITE-WEEKLY","CAL-GROWTH-WEEKLY"):
    if by_id.get(event_id,{}).get("status")!="OWNER_APPROVED_WINDOW_NOT_AUTOMATED":
        errors.append(f"Native agent falsely marked scheduled: {event_id}")
monthly=by_id.get("CAL-MONTHLY",{})
if monthly.get("time")!="FIRST_MONDAY_12:00_WITHIN_APPROVED_WEEKLY_GROWTH_WINDOW" or monthly.get("activation")!="MANUAL_ONLY":
    errors.append("Monthly review must reuse weekly Growth window without extra native scheduling")
if cal.get("timezone")!="Asia/Jerusalem":
    errors.append("Operating calendar must use Asia/Jerusalem timezone")
if not cal.get("quota_efficiency_policy",{}).get("rerun_policy"):
    errors.append("Missing quota-aware no-retry policy")

metrics=score.get("agent_metrics",[])
if len(metrics)<10 or len({x.get("metric_id") for x in metrics})!=len(metrics):
    errors.append("Metrics missing or duplicate IDs")
for x in metrics:
    if x.get("target_approved") is not False:
        errors.append(f"Unapproved target improperly marked approved: {x.get('metric_id')}")
    if "target_proposed" not in x or "baseline" not in x:
        errors.append(f"Metric lacks explicit proposed-target/baseline fields: {x.get('metric_id')}")
agents={x.get("agent") for x in metrics}
if agents!={"Growth Manager","Data Agent","SEO Agent","Website & Conversion Agent","Festival Sales Agent"}:
    errors.append(f"Unexpected or incomplete agent roles: {agents}")
if score.get("actuals")!=[]:
    errors.append("Actuals must remain empty until an observed review")

tasks=board.get("tasks",[])
allowed=set(board.get("allowed_statuses",[]))
if not tasks or len({x.get("id") for x in tasks})!=len(tasks):
    errors.append("Missing/duplicate tasks")
for x in tasks:
    if x.get("status") not in allowed:
        errors.append(f"Invalid task status: {x.get('id')}")
    for key in ("agent","approver","next_review","priority","evidence","next_step","dispatch_status"):
        if not x.get(key):
            errors.append(f"Task {x.get('id')} missing {key}")
    if x.get("dispatch_status")=="DISPATCHED" and x.get("status")=="BACKLOG":
        errors.append(f"Unverified dispatch: {x.get('id')}")
if errors:
    print("GROWTH MANAGEMENT VALIDATION: FAIL")
    for item in errors: print("ERROR:",item)
    sys.exit(1)
print(f"GROWTH MANAGEMENT VALIDATION: PASS ({len(events)} calendar items, {len(metrics)} KPIs, {len(tasks)} tasks; no native-agent execution claimed)")
