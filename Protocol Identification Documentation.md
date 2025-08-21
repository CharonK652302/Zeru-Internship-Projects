# Protocol Identification Documentation

## Methodology
Protocol and token identification was done by mapping known Ethereum contract addresses to their corresponding protocol or token name.  

The sources include:
- [Etherscan.io](https://etherscan.io/) verified contract addresses
- Official protocol documentation (Aave, Uniswap, Curve, Balancer, etc.)
- Token contract registries (for stablecoins like USDC, USDT, and WBTC)

## Mapped Contracts
- **USD Coin (USDC)**  
  Contract: `0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48`  
  Type: ERC20 Token  

- **Tether (USDT)**  
  Contract: `0xdac17f958d2ee523a2206206994597c13d831ec7`  
  Type: ERC20 Token  

- **Wrapped Bitcoin (WBTC)**  
  Contract: `0x2260fac5e5542a773aa44fbcfedf7c193bc2c599`  
  Type: ERC20 Token  

- **Uniswap V3: NonfungiblePositionManager**  
  Contract: `0xc36442b4a4522e871399cd717abdd847ab11fe88`  
  Type: Protocol  

- **Aave V3 Pool**  
  Contract: `0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2`  
  Type: Protocol  

- **Curve Protocol**  
  Contract: `0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7`  
  Type: Protocol  

- **Balancer Pool**  
  Contract: `0xc4922d64a24675e16e1586e3e3aa56c06fabe907`  
  Type: Protocol  

- **Other Aave Contracts**  
  (Gateway, Incentives Controller, Lending Pool) — mapped for completeness.

## Unknown Contracts
If a contract address is not found in the mapping, it defaults to:
```json
{"name": "Unknown", "protocol": "Unknown"}
