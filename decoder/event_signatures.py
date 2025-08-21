event_signatures = {
    '0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef': {
        'name': 'Transfer',
        'abi': 'event Transfer(address indexed from, address indexed to, uint256 value)'
    },
    '0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925': {
        'name': 'Approval',
        'abi': 'event Approval(address indexed owner, address indexed spender, uint256 value)'
    },
    '0xab8530f87dc9b59234c4623bf917212bb2536d647574c8e7e5da92c2ede0c9f8': {
        'name': 'Deposit',
        'abi': 'event Deposit(address indexed user, uint256 amount)'
    },
    '0x1b2a7ff080b8cb6ff436ce0372e399692bbfb6d4ae5766fd8d58a7b8cc6142e6': {
        'name': 'Withdraw',
        'abi': 'event Withdraw(address indexed user, uint256 amount)'
    },
}

def get_event_name(topics):
    if not topics or len(topics) == 0:
        return "Unknown Event"
    event_hash = topics[0].lower()
    event_info = event_signatures.get(event_hash)
    if event_info:
        return event_info["name"]
    else:
        return "Unknown Event"
