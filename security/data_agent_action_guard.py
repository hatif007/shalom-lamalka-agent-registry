"""Fail-closed reference guard for Data Agent v2 connector calls.

IMPORTANT: this module is NOT automatically connected to ChatGPT/Workspace Agent
connector execution. CI testing it proves reference policy logic, not deployed
backend enforcement. Only a trusted runtime mediator can invoke allow() BEFORE
each connector operation and maintain task state independently of the agent.
"""
import re
from datetime import date

SITE_ID = "03b550bb-4ab1-4854-99b8-8bb153c4431e"
PROPERTY_ID = "558438175"
REPO = "hatif007/shalom-lamalka-agent-registry"
BRANCH = "fix/registry-v0.2-structure"
CHANNELS = {"C0C87EKC71R", "C0C86D1C3D5"}
PRODUCT_URL = "https://www.wixapis.com/stores/v3/products/query"
ORDERS_URL = "https://www.wixapis.com/ecom/v1/orders/search"

WIX_CONTEXT = "mcp__Wix___Shalom_La_Malka__GetSiteContext"
WIX_CALL = "mcp__Wix___Shalom_La_Malka__CallWixSiteAPI"
GA4_SUMMARY = "mcp__Vosik_Signals___Hosted_GA4_MCP__get_account_summaries"
GA4_REPORT = "mcp__Vosik_Signals___Hosted_GA4_MCP__run_report"
GIT_READ = "mcp__GitHub__fetch_file"
SLACK_READ = "mcp__Slack__slack_read_channel"
SLACK_THREAD = "mcp__Slack__slack_read_thread"
SLACK_SEND = "mcp__Slack__slack_send_message"

METRICS = {"sessions", "activeUsers", "screenPageViews", "eventCount",
           "transactions", "purchaseRevenue", "keyEvents"}
DIMENSIONS = {"date", "eventName", "sessionSourceMedium", "landingPage"}


def _paging(value):
    if not isinstance(value, dict) or not set(value) <= {"limit", "cursor"}:
        return False
    limit = value.get("limit")
    return (type(limit) is int and 1 <= limit <= 100 and
            (not "cursor" in value or (isinstance(value["cursor"], str) and
             0 < len(value["cursor"]) <= 4096)))


def _wix_query(args):
    if args.get("siteId") != SITE_ID or args.get("method") != "POST":
        return False
    url = args.get("url")
    if url not in (PRODUCT_URL, ORDERS_URL):
        return False
    body = args.get("body")
    if not isinstance(body, dict):
        return False
    root = "query" if url == PRODUCT_URL else "search"
    if set(body) != {root} or not isinstance(body[root], dict):
        return False
    query = body[root]
    allowed = {"cursorPaging"} if root == "query" else {"cursorPaging", "filter"}
    if not set(query) <= allowed or not _paging(query.get("cursorPaging")):
        return False
    if "filter" in query:
        f = query["filter"]
        if root != "search" or not isinstance(f, dict) or set(f) != {"status"}:
            return False
        if f["status"] not in ("APPROVED", "PENDING", "REJECTED"):
            return False
    return True


def _ga4_report(args):
    if str(args.get("propertyId")) not in (PROPERTY_ID, "properties/" + PROPERTY_ID):
        return False
    metrics = args.get("metrics")
    dims = args.get("dimensions", [])
    ranges = args.get("dateRanges")
    if (not isinstance(metrics, list) or not metrics or
        not set(metrics) <= METRICS or not isinstance(dims, list) or
        not set(dims) <= DIMENSIONS or not isinstance(ranges, list) or
        not 1 <= len(ranges) <= 2):
        return False
    for r in ranges:
        if not isinstance(r, dict) or not set(r) <= {"startDate", "endDate", "name"}:
            return False
        try:
            start = date.fromisoformat(r["startDate"])
            end = date.fromisoformat(r["endDate"])
            if start > end:
                return False
        except (TypeError, KeyError, ValueError):
            return False
    limit = args.get("limit", 100)
    return type(limit) is int and 1 <= limit <= 1000


def allow(tool, args, context=None):
    """Boolean preflight decision. Unrecognized tools fail closed.

    context is provided by a trusted mediator, NEVER by model text or tool args.
    Do not use without a trusted mediator and authenticated source authorization.
    """
    context = context or {}
    if not isinstance(args, dict) or not isinstance(context, dict):
        return False
    if tool == WIX_CONTEXT:
        return args.get("siteId") == SITE_ID and not args.get("siteName")
    if tool == WIX_CALL:
        return _wix_query(args)
    if tool == GA4_SUMMARY:
        return args == {}
    if tool == GA4_REPORT:
        return _ga4_report(args)
    if tool == GIT_READ:
        return (args.get("repository_full_name") == REPO and
                args.get("path") == "skills/data-agent/SKILL.md" and
                args.get("ref") == BRANCH)
    if tool == SLACK_READ:
        return args.get("channel_id") in CHANNELS and set(args) <= {
            "channel_id", "limit", "cursor", "response_format", "latest", "oldest"}
    if tool == SLACK_THREAD:
        return (args.get("channel_id") in CHANNELS and
                isinstance(args.get("message_ts"), str) and
                bool(re.fullmatch(r"\d+\.\d+", args["message_ts"])) and
                set(args) <= {"channel_id", "message_ts", "limit", "response_format",
                              "latest", "oldest"})
    if tool == SLACK_SEND:
        msg = args.get("message")
        return (
            args.get("channel_id") in CHANNELS and
            set(args) <= {"channel_id", "message", "unfurl_app_links"} and
            args.get("unfurl_app_links") is not True and
            isinstance(msg, str) and 1 <= len(msg) <= 2000 and
            not re.search(r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", msg) and
            context.get("approved_channel") == args["channel_id"] and
            isinstance(context.get("authorized_task_id"), str) and
            bool(context["authorized_task_id"].strip()) and
            context.get("authorization_verified") is True and
            context.get("messages_already_sent_for_task") == 0 and
            context.get("pii_review_passed") is True
        )
    return False


def self_test():
    good = [
        (WIX_CONTEXT, {"siteId": SITE_ID}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "POST", "url": PRODUCT_URL,
                    "body": {"query": {"cursorPaging": {"limit": 5}}}}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "POST", "url": ORDERS_URL,
                    "body": {"search": {"filter": {"status": "PENDING"},
                                        "cursorPaging": {"limit": 1}}}}, {}),
        (GA4_SUMMARY, {}, {}),
        (GA4_REPORT, {"propertyId": PROPERTY_ID, "dateRanges":
                      [{"startDate": "2026-10-06", "endDate": "2026-10-12"}],
                      "metrics": ["sessions", "activeUsers"]}, {}),
        (GIT_READ, {"repository_full_name": REPO,
                    "path": "skills/data-agent/SKILL.md", "ref": BRANCH}, {}),
        (SLACK_READ, {"channel_id": "C0C87EKC71R"}, {}),
        (SLACK_SEND, {"channel_id": "C0C87EKC71R", "message": "Test result: PASS"},
         {"approved_channel": "C0C87EKC71R", "authorized_task_id": "TEST-001",
          "authorization_verified": True, "messages_already_sent_for_task": 0,
          "pii_review_passed": True})
    ]
    for tool, args, ctx in good:
        assert allow(tool, args, ctx), f"Expected allow: {tool}"
    bad = [
        ("mcp__Wix___Shalom_La_Malka__ExecuteWixAPI", {"hasMutations": False}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "DELETE", "url": PRODUCT_URL,
                    "body": {"query": {"cursorPaging": {"limit": 1}}}}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "POST",
                    "url": "https://www.wixapis.com/stores/v3/products/create",
                    "body": {"query": {"cursorPaging": {"limit": 1}}}}, {}),
        (WIX_CALL, {"siteId": "other", "method": "POST", "url": PRODUCT_URL,
                    "body": {"query": {"cursorPaging": {"limit": 1}}}}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "POST", "url": ORDERS_URL,
                    "body": {"search": {"filter": {"buyerInfo.email": "x@example.com"},
                                        "cursorPaging": {"limit": 1}}}}, {}),
        (WIX_CALL, {"siteId": SITE_ID, "method": "POST", "url": PRODUCT_URL,
                    "body": {"query": {"cursorPaging": {"limit": 0}}}}, {}),
        (GA4_REPORT, {"propertyId": "999", "dateRanges":
                      [{"startDate": "2026-10-06", "endDate": "2026-10-12"}],
                      "metrics": ["sessions"]}, {}),
        ("mcp__GitHub__update_file", {"path": "skills/data-agent/SKILL.md"}, {}),
        (GIT_READ, {"repository_full_name": REPO, "path": "registries/tests.json",
                    "ref": BRANCH}, {}),
        (SLACK_SEND, {"channel_id": "FORBIDDEN", "message": "Test"},
         {"approved_channel": "FORBIDDEN", "authorized_task_id": "TEST",
          "authorization_verified": True, "messages_already_sent_for_task": 0,
          "pii_review_passed": True}),
        (SLACK_SEND, {"channel_id": "C0C87EKC71R", "message": "Test"}, {}),
        (SLACK_SEND, {"channel_id": "C0C87EKC71R", "message": "Test"},
         {"approved_channel": "C0C87EKC71R", "authorized_task_id": "TEST",
          "authorization_verified": True, "messages_already_sent_for_task": 1,
          "pii_review_passed": True}),
        (SLACK_SEND, {"channel_id": "C0C87EKC71R", "message": "Test",
                      "reply_broadcast": True},
         {"approved_channel": "C0C87EKC71R", "authorized_task_id": "TEST",
          "authorization_verified": True, "messages_already_sent_for_task": 0,
          "pii_review_passed": True}),
        (SLACK_SEND, {"channel_id": "C0C87EKC71R", "message": "client@example.org"},
         {"approved_channel": "C0C87EKC71R", "authorized_task_id": "TEST",
          "authorization_verified": True, "messages_already_sent_for_task": 0,
          "pii_review_passed": True}),
        ("mcp__Slack__slack_delete_message", {"channel_id": "C0C87EKC71R"}, {}),
        ("unknown_tool", {}, {})
    ]
    for tool, args, ctx in bad:
        assert not allow(tool, args, ctx), f"Expected deny: {tool}"
    print(f"REFERENCE ACTION GUARD SELF TEST: PASS ({len(good)} allow, {len(bad)} deny)")
    print("This does not verify enforcement by connected Workspace Agent or provider OAuth.")


if __name__ == "__main__":
    self_test()
