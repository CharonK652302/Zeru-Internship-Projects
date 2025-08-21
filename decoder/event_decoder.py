def safe_int(hex_str):
    """Convert hex string to int safely, return 0 if invalid/empty"""
    try:
        if hex_str and hex_str != "0x":
            return int(hex_str, 16)
    except Exception:
        pass
    return 0

def decode_transfer_event(log):
    value = safe_int(log["data"])
    from_addr = "0x" + log["topics"][1][-40:]
    to_addr = "0x" + log["topics"][2][-40:]
    return {"event": "Transfer", "from": from_addr, "to": to_addr, "value": value}

def decode_approval_event(log):
    value = safe_int(log["data"])
    owner = "0x" + log["topics"][1][-40:]
    spender = "0x" + log["topics"][2][-40:]
    return {"event": "Approval", "owner": owner, "spender": spender, "value": value}

def decode_deposit_event(log):
    value = safe_int(log['data'])
    user = "0x" + log["topics"][1][-40:]
    return {"event": "Deposit", "user": user, "value": value}

def decode_withdraw_event(log):
    value = safe_int(log['data'])
    user = "0x" + log["topics"][1][-40:]
    return {"event": "Withdraw", "user": user, "value": value}

# Mapping of event name → decoder
decoders = {
    "Transfer": decode_transfer_event,
    "Approval": decode_approval_event,
    "Deposit": decode_deposit_event,
    "Withdraw": decode_withdraw_event,
}

def decode_event(event_name, topics, data):
    """Decode event data given its name and log structure"""
    log = {"topics": topics, "data": data}
    decoder_func = decoders.get(event_name)
    if decoder_func:
        return decoder_func(log)
    return None
