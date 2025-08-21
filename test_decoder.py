import pytest
from decoder.protocol_mapper import identify_protocol
from decoder.event_signatures import get_event_name
from decoder.event_decoder import decode_event

def test_protocol_known():
    addr = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"
    result = identify_protocol(addr)
    assert result["name"] == "USD Coin"
    assert result["protocol"] == "ERC20"

def test_protocol_unknown():
    addr = "0x1234567890abcdef1234567890abcdef12345678"
    result = identify_protocol(addr)
    assert result["name"] == "Unknown"
    assert result["protocol"] == "Unknown"

def test_event_transfer_signature():
    sig = ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]
    assert get_event_name(sig) == "Transfer"

def test_event_unknown_signature():
    sig = ["0xabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcdefabcd"]
    assert get_event_name(sig) == "Unknown Event"

def test_decode_transfer_event():
    topics = [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x0000000000000000000000001111111111111111111111111111111111111111",
        "0x0000000000000000000000002222222222222222222222222222222222222222",
    ]
    data = "0x5f5e100"  # 100000000 in hex
    decoded = decode_event("Transfer", topics, data)
    assert decoded["event"] == "Transfer"
    assert decoded["from"].endswith("1111")
    assert decoded["to"].endswith("2222")
    assert isinstance(decoded["value"], int)

def test_decode_empty_data():
    decoded = decode_event("Transfer", [
        "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
        "0x0000000000000000000000001111111111111111111111111111111111111111",
        "0x0000000000000000000000002222222222222222222222222222222222222222",
    ], "0x")
    assert decoded["value"] == 0
