# Technical Report: Multi-Protocol Blockchain Event Decoder

## 1. Introduction
Blockchain ecosystems consist of multiple protocols and tokens, each emitting different types of on-chain events. A common challenge is to decode raw Ethereum logs into structured, human-readable data that can be analyzed and categorized.

This project implements a **multi-protocol blockchain event decoder** capable of:
- Identifying protocols and tokens based on contract addresses.
- Mapping event signatures to event names and ABIs.
- Decoding key events (`Transfer`, `Approval`, `Deposit`, `Withdraw`).
- Organizing events by protocol type.
- Producing both a **summary report** and a **detailed JSON output** for downstream analytics.

The solution is modular, extensible, and designed to handle both known and unknown protocols gracefully.

---

## 2. Design and Architecture

### 2.1 Modular Structure
The project follows a modular architecture for clarity and scalability:

- **`protocol_mapper.py`**  
  Maps known contract addresses to their corresponding protocol or token names and types (e.g., ERC20, Protocol, Contract).  
  Unknown contracts are labeled `"Unknown"`.

- **`event_signatures.py`**  
  Maintains a mapping between event signature hashes (Keccak-256 of the event ABI) and human-readable event names.  
  Example:  
Transfer(address indexed from, address indexed to, uint256 value)
→ 0xddf252ad1b...

markdown
Copy
Edit

- **`event_decoder.py`**  
Contains decoding functions for supported events. Each function extracts parameters from `topics` and `data`, returning structured output.  

- **`main.py`**  
The entry point of the system.  
Steps:
1. Loads raw logs from `sample.json`.  
2. Identifies the protocol using `protocol_mapper`.  
3. Resolves the event name using `event_signatures`.  
4. Decodes event data via `event_decoder`.  
5. Builds a **human-readable summary** for each event.  
6. Groups events by protocol type.  
7. Generates a **summary** with statistics and writes the results to `output/decoded_events.json`.

---

### 2.2 Data Flow
1. **Input:** `sample.json` containing Ethereum logs.  
2. **Processing:** Iterative decoding of each log entry.  
3. **Output:** `decoded_events.json` with two sections:  
 - `summary` → global statistics.  
 - `eventsByProtocol` → detailed event breakdown.

---

## 3. Multi-Protocol Approach

The key challenge was handling multiple protocols consistently. Our approach included:

### 3.1 Protocol Identification
- Used **contract address mapping** to identify well-known tokens and protocols (USDC, USDT, WBTC, Uniswap, Aave, Curve, Balancer).
- Source: verified contracts on **Etherscan** and official protocol documentation.
- Unrecognized addresses default to `"Unknown"` ensuring robustness.

### 3.2 Event Recognition
- Event signatures were mapped to names via their **Keccak-256 hashes**.
- This ensures even if the source ABI is not available, the event can be matched and labeled.

### 3.3 Event Decoding
- Decoders implemented for:
- **Transfer** → Extracts sender, recipient, amount.  
- **Approval** → Extracts owner, spender, value.  
- **Deposit** → Extracts user, deposited amount.  
- **Withdraw** → Extracts user, withdrawn amount.  
- Other events are gracefully ignored but logged as `"Unknown Event"`.

### 3.4 Human-Readable Interpretations
- Each decoded event is translated into a friendly text summary.  
Example:  
{
"action": "Transfer of 100 tokens",
"from": "0xabc...",
"to": "0xdef...",
"amount": 100
}

yaml
Copy
Edit

---

## 4. Edge Case Handling

### 4.1 Unknown Protocols
- If a contract address is not recognized, the event is still logged with `"Unknown"` protocol.  
- This ensures data completeness even for unfamiliar protocols.

### 4.2 Missing or Invalid Topics
- If topics are missing, the event defaults to `"Unknown Event"`.  

### 4.3 Empty Data Field
- Hex `"0x"` is interpreted as `0` instead of throwing an error.  
- Prevents crashes when value fields are unused or optional.

### 4.4 Unsupported Events
- Unsupported events are skipped with a `"Unknown Event"` label, ensuring the decoder remains stable.

---

## 5. Testing

### 5.1 Unit Tests
We implemented **test cases** using `pytest`:
- Protocol identification (known and unknown).
- Event recognition (valid and invalid signatures).
- Event decoding (Transfer, Approval).
- Edge cases (empty data, missing topics).

### 5.2 Example Test
```python
def test_protocol_unknown():
  addr = "0x1234567890abcdef1234567890abcdef12345678"
  result = identify_protocol(addr)
  assert result["protocol"] == "Unknown"
6. Results
6.1 Output Structure
The final JSON output (decoded_events.json) includes:

Summary:

Total logs processed

Total events decoded

Protocols identified

Event type distribution

Processing timestamp

EventsByProtocol:

Each event with transaction details, protocol info, event name, decoded data, and a human-readable description.

6.2 Example Output Snippet
json
Copy
Edit
{
  "transactionHash": "0x123...",
  "protocol": "USD Coin",
  "protocolType": "ERC20",
  "eventName": "Transfer",
  "decodedData": {
    "event": "Transfer",
    "from": "0xabc...",
    "to": "0xdef...",
    "value": 100
  },
  "humanReadable": {
    "action": "Transfer of 100 tokens",
    "from": "0xabc...",
    "to": "0xdef...",
    "amount": 100
  }
}
7. Conclusion
This project demonstrates a modular and extensible blockchain event decoder that can:

Handle multiple protocols.

Map event signatures to names.

Decode and interpret core events.

Export structured, human-readable data.

The architecture allows easy extension: new protocols can be added to protocol_mapper, and new event decoders can be registered in event_decoder.

The system ensures robustness by handling edge cases gracefully, making it suitable for real-world blockchain log analysis.