import json
from decoder.protocol_mapper import identify_protocol
from decoder.event_signatures import get_event_name
from decoder.event_decoder import decode_event

# Load logs from sample.json
with open("sample.json") as f:
    raw = json.load(f)

logs = raw.get("logs", [])

events_by_protocol = {}
summary = {
    "totalLogsProcessed": len(logs),
    "totalEventsDecoded": 0,
    "protocolsIdentified": {},
    "eventTypeDistribution": {},
    "processingTimestamp": "2025-08-21T12:30:00Z"
}

for log in logs:
    address = log["address"]
    protocol_info = identify_protocol(address)
    event_sig = log["topics"] if log["topics"] else None
    event_name = get_event_name(event_sig) if event_sig else "Unknown Event"
    decoded = decode_event(event_name, log["topics"], log["data"])

    # --- FIX: define ptype before using ---
    ptype = protocol_info["protocol"]

    # Build a human-readable summary
    human_readable = {"action": "Unknown event"}
    if decoded:
        if event_name == "Transfer":
            human_readable = {
                "action": f"Transfer of {decoded['value']} tokens",
                "from": decoded["from"],
                "to": decoded["to"],
                "amount": decoded["value"]
            }
        elif event_name == "Approval":
            human_readable = {
                "action": f"Approval of {decoded['value']} tokens",
                "owner": decoded["owner"],
                "spender": decoded["spender"],
                "amount": decoded["value"]
            }
        elif event_name == "Deposit":
            human_readable = {
                "action": f"Deposit of {decoded['value']} tokens",
                "user": decoded["user"],
                "amount": decoded["value"]
            }
        elif event_name == "Withdraw":
            human_readable = {
                "action": f"Withdrawal of {decoded['value']} tokens",
                "user": decoded["user"],
                "amount": decoded["value"]
            }

    # Add event to events_by_protocol
    events_by_protocol.setdefault(ptype, []).append({
        "transactionHash": log["transactionHash"],
        "blockNumber": log["blockNumber"],
        "logIndex": log["logIndex"],
        "protocol": protocol_info["name"],
        "protocolType": ptype,
        "contractAddress": address,
        "eventName": event_name,
        "eventSignature": event_sig,
        "decodedData": decoded,
        "humanReadable": human_readable
    })

    # Update summary
    summary["eventTypeDistribution"].setdefault(event_name, 0)
    summary["eventTypeDistribution"][event_name] += 1

summary["totalEventsDecoded"] = sum(summary["eventTypeDistribution"].values())
summary["protocolsIdentified"] = {
    ptype: list({e["protocol"] for e in evs})
    for ptype, evs in events_by_protocol.items()
}

# Save results
output = {"summary": summary, "eventsByProtocol": events_by_protocol}
with open("output/decoded_events.json", "w") as f:
    json.dump(output, f, indent=2)

print("✅ Decoding complete. See output/decoded_events.json")
