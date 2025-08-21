# contract address → protocol/token name/type mapping
protocol_map = {
    '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48': {'name': 'USD Coin', 'type': 'ERC20'},
    '0xdac17f958d2ee523a2206206994597c13d831ec7': {'name': 'Tether USD', 'type': 'ERC20'},
    '0x2260fac5e5542a773aa44fbcfedf7c193bc2c599': {'name': 'Wrapped BTC', 'type': 'ERC20'},
    '0xc36442b4a4522e871399cd717abdd847ab11fe88': {'name': 'Uniswap V3: NonfungiblePositionManager', 'type': 'Protocol'},
    '0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2': {'name': 'Aave V3 Pool', 'type': 'Protocol'},
    '0xbebc44782c7db0a1a60cb6fe97d0b483032ff1c7': {'name': 'Curve Protocol', 'type': 'Protocol'},
    '0xbd3fa81b58ba92a82136038b25adec7066af3155': {'name': 'Aave V3 Gateway', 'type': 'Contract'},
    '0xf2614a233c7c3e7f08b1f887ba133a13f1eb2c55': {'name': 'Aave V3 Incentives Controller', 'type': 'Contract'},
    '0x98c23e9d8f34fefb1b7bd6a91b7ff122f4e16f5c': {'name': 'Aave V3 Lending Pool', 'type': 'Contract'},
    '0xc4922d64a24675e16e1586e3e3aa56c06fabe907': {'name': 'Balancer Pool', 'type': 'Protocol'},
    '0xa5201535fbecb9f5139569caf92df9db11a69559': {'name': 'Unknown Protocol', 'type': 'Contract'},
}

def identify_protocol(address: str):
    address = address.lower()
    info = protocol_map.get(address)
    if info:
        return {"name": info["name"], "protocol": info["type"]}
    else:
        return {"name": "Unknown", "protocol": "Unknown"}
