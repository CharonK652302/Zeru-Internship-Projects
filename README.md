# Blockchain Event Decoder

## Overview
This project is a multi-protocol blockchain event decoder that:
- Processes Ethereum logs from a JSON file.
- Identifies the protocol or token for each log using contract address mappings.
- Maps event signatures to event names.
- Decodes events such as `Transfer`, `Approval`, `Deposit`, and `Withdraw`.
- Produces a structured JSON output grouped by protocol type with a human-readable summary.

---

## Setup Instructions

### Prerequisites
- Python 3.8+
- `pip` installed

### Installation
1. Clone or download this repository.
2. Navigate to the project directory:
   ```bash
   cd blockchain_event_decoder
(Optional but recommended) Create a virtual environment:

3
python -m venv venvvenv\Scripts\activate       # Windows



4. pip install -r requirements.txt

5.python main.py


6.output/decoded_events.json