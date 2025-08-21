# Blockchain Event Log Decoder Challenge

## Overview
This is a technical assessment for AI engineers to evaluate their ability to work with blockchain data, specifically decoding raw event logs from various DeFi protocols. The challenge involves building a service that can identify, classify, and decode lending protocol events from raw transaction logs stored in S3.

## Problem Statement

### Background
We have millions of raw transaction logs stored in S3 from various blockchain protocols including:
- **Lending protocols** (Aave, Compound, etc.)
- **DEX protocols** (Uniswap, SushiSwap, etc.)
- **Staking protocols** (Lido, RocketPool, etc.)
- **Restaking protocols** (EigenLayer, etc.)

Your task is to build a service that can read these logs and decode **ALL events** present in the dataset, automatically identifying which protocol each event belongs to and providing comprehensive decoding.

### Sample Data
A sample dataset is provided in the file:
```
sample.json
```

This file contains:
- **162 total logs** from Polygon blockchain
- **66 relevant logs** for the wallet `0xBF0eCCD64bB1b5Ff949f55467E5BBE4376587c23`
- Raw event logs with topics, data, and basic decoding attempts
- Mix of lending, DEX, system, and other DeFi protocol events
- Events from multiple protocols requiring different decoding strategies

### Data Structure
Each log entry contains:
```json
{
  "removed": false,
  "logIndex": 234,
  "transactionIndex": 33,
  "transactionHash": "0x...",
  "blockHash": "0x...",
  "blockNumber": 35285936,
  "address": "0x...",
  "data": "0x...",
  "topics": ["0x...", "0x...", "0x...", null]
}
```

## Challenge Requirements

### Phase 1: Protocol Identification (25 points)
1. **Analyze the sample data** and identify ALL protocols present (lending, DEX, system, etc.)
2. **Research and classify** each contract address to its corresponding protocol
3. **Create a comprehensive mapping** of contract addresses to protocol names and types
4. **Handle unknown protocols** gracefully with fallback identification strategies

### Phase 2: Event Signature Recognition (25 points)
1. **Identify ALL event signatures** from the `topics[0]` field across different protocol types
2. **Map event signatures** to their corresponding event names (e.g., `Transfer`, `Swap`, `Deposit`, `Withdraw`, `Approval`)
3. **Handle signature collisions** where the same signature is used across different protocols
4. **Build a multi-protocol event signature database** covering all DeFi categories

### Phase 3: Universal Event Decoding (40 points)
1. **Decode ALL raw event data** into human-readable format across all protocol types
2. **Extract protocol-specific parameters** such as:
   - **DEX events**: Token pairs, amounts, fees, slippage
   - **Lending events**: User addresses, collateral, interest rates
   - **System events**: Gas fees, state changes, transfers
   - **Token events**: Transfers, approvals, mints, burns
3. **Handle diverse ABI formats** and parameter types across different protocols
4. **Implement fallback decoding** for unknown or custom event formats
5. **Validate decoded data** for consistency across different event types

### Phase 4: Comprehensive Output Generation (10 points)
1. **Generate a structured JSON output** containing ALL decoded events organized by protocol type
2. **Include rich metadata** about each protocol, event type, and decoded parameters
3. **Provide analytics summary** with event distribution and protocol usage statistics
4. **Ensure data quality** and completeness across all event categories

## Expected Output Format

```json
{
  "summary": {
    "totalLogsProcessed": 162,
    "totalEventsDecoded": 145,
    "protocolsIdentified": {
      "lending": ["Aave", "Compound"],
      "dex": ["Uniswap", "SushiSwap"],
      "system": ["Polygon"],
      "unknown": 3
    },
    "eventTypeDistribution": {
      "Transfer": 45,
      "Approval": 23,
      "Swap": 18,
      "Deposit": 12,
      "Withdraw": 8,
      "Unknown": 39
    },
    "processingTimestamp": "2025-08-19T10:00:00Z"
  },
  "eventsByProtocol": {
    "lending": [
      {
        "transactionHash": "0x...",
        "blockNumber": 35285936,
        "logIndex": 234,
        "protocol": "Aave",
        "protocolType": "lending",
        "contractAddress": "0x...",
        "eventName": "Deposit",
        "eventSignature": "0x...",
        "decodedData": {
          "user": "0x...",
          "reserve": "0x...",
          "amount": "1000000000000000000",
          "onBehalfOf": "0x...",
          "referralCode": 0
        },
        "humanReadable": {
          "action": "User deposited 1.0 WETH into Aave",
          "user": "0xBF0e...",
          "token": "WETH",
          "amount": "1.0",
          "protocol": "Aave"
        }
      }
    ],
    "dex": [
      {
        "transactionHash": "0x...",
        "blockNumber": 35286080,
        "logIndex": 425,
        "protocol": "Uniswap V3",
        "protocolType": "dex",
        "contractAddress": "0x...",
        "eventName": "Swap",
        "eventSignature": "0x...",
        "decodedData": {
          "sender": "0x...",
          "recipient": "0x...",
          "amount0": "-4000000000000000000",
          "amount1": "695839922833653019",
          "sqrtPriceX96": "...",
          "liquidity": "...",
          "tick": 123456
        },
        "humanReadable": {
          "action": "Swapped 4.0 WMATIC for 0.696 USDC on Uniswap V3",
          "user": "0xBF0e...",
          "tokenIn": "WMATIC",
          "tokenOut": "USDC",
          "amountIn": "4.0",
          "amountOut": "0.696"
        }
      }
    ],
    "system": [
      {
        "transactionHash": "0x...",
        "blockNumber": 35285936,
        "logIndex": 234,
        "protocol": "Polygon",
        "protocolType": "system",
        "contractAddress": "0x0000000000000000000000000000000000001010",
        "eventName": "Transfer",
        "eventSignature": "0x...",
        "decodedData": {
          "from": "0x...",
          "to": "0x...",
          "value": "11253333330000000000"
        },
        "humanReadable": {
          "action": "System transfer of 11.25 MATIC for gas fees",
          "from": "0xBF0e...",
          "to": "0xe780...",
          "amount": "11.25",
          "token": "MATIC"
        }
      }
    ],
    "unknown": [
      {
        "transactionHash": "0x...",
        "blockNumber": 35286080,
        "logIndex": 423,
        "protocol": "Unknown",
        "protocolType": "unknown",
        "contractAddress": "0x...",
        "eventName": "Unknown Event",
        "eventSignature": "0x458f5fa412d0f69b08dd84872b0215675cc67bc1d5b6fd93300a1c3878b86196",
        "rawData": {
          "topics": ["0x458f5fa412d0f69b08dd84872b0215675cc67bc1d5b6fd93300a1c3878b86196", "0x...", "0x...", null],
          "data": "0x..."
        },
        "note": "Could not identify protocol or decode event signature"
      }
    ]
  }
}
```

## Technical Constraints

### Must Use
- **Any programming language** (Python, JavaScript, Rust, Go, etc.)
- **Standard libraries** for JSON processing and HTTP requests
- **Open source ABI decoding libraries** (ethers.js, web3.py, etc.)

### Cannot Use
- **Existing blockchain indexing services** (The Graph, Moralis, etc.)
- **Pre-built protocol-specific SDKs** (Aave SDK, Compound SDK, etc.)
- **Paid APIs** for event decoding

### Performance Requirements
- Process the sample dataset (162 logs) in **under 60 seconds** (increased due to comprehensive decoding)
- Handle **malformed or incomplete data** gracefully across all protocol types
- **Memory efficient** processing for large datasets with diverse event formats
- **Scalable architecture** that can handle addition of new protocols

## Evaluation Criteria

### Code Quality (25%)
- Clean, readable, and well-documented code
- Proper error handling and edge case management
- Modular design with separation of concerns
- Unit tests for critical functions

### Accuracy (30%)
- Correct identification of ALL protocols (lending, DEX, system, etc.)
- Accurate event decoding across different protocol types
- Proper handling of diverse data types and ABI formats
- Validation of decoded results across all event categories

### Completeness (25%)
- ALL events in the dataset identified and decoded (not just lending)
- Comprehensive coverage of all protocol types present
- Detailed output with rich metadata and analytics
- Documentation of methodology for handling diverse protocols

### Innovation (20%)
- Creative approaches to universal protocol identification
- Efficient algorithms for multi-protocol event processing
- Cross-protocol analytics and insights
- Extensible architecture for adding new protocol types

## Bonus Challenges (Optional)

### Advanced Features (+10 points each)
1. **Multi-chain support**: Extend to handle events from different blockchains
2. **Real-time processing**: Design for streaming event processing from multiple protocols
3. **Protocol versioning**: Handle different versions of the same protocol (Uniswap V2 vs V3)
4. **Cross-protocol analytics**: Identify MEV, arbitrage, and complex DeFi strategies
5. **Auto-discovery**: Automatically identify new/unknown protocols from event patterns

### Research Components (+5 points each)
1. **Gas optimization analysis**: Calculate gas costs across different protocol interactions
2. **DeFi strategy detection**: Identify complex strategies (yield farming, arbitrage, liquidations)
3. **Protocol interaction analysis**: Map relationships and dependencies between protocols
4. **User behavior analytics**: Track user patterns across different protocol types
5. **MEV detection**: Identify Maximum Extractable Value opportunities from event sequences

## Submission Requirements

### Deliverables
1. **Source code** with clear documentation and modular architecture
2. **README** with setup and execution instructions
3. **Output JSON file** with ALL decoded events organized by protocol type
4. **Technical report** (3-4 pages) explaining your multi-protocol approach
5. **Test cases** demonstrating edge case handling across different protocols
6. **Protocol identification documentation** with methodology and sources

### Timeline
- **Estimated time**: 6-8 hours for core requirements (increased due to comprehensive scope)

## Getting Started

1. **Download the sample data** from the provided path
2. **Analyze the data structure** and identify all event patterns
3. **Research ALL protocols** present in the dataset (not just lending)
4. **Start with common event signatures** (Transfer, Approval) and expand
5. **Build a modular decoder** that can handle different protocol types
6. **Test with known signatures** before tackling unknown events
