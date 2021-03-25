#! /usr/bin/env python3

import sys
from ipaddress import (
    IPv4Network, IPv6Network,
    ip_network, collapse_addresses
)
from typing import List, Union, Any, cast

result4: List[IPv4Network]
result6: List[IPv6Network]

try:
    with open(sys.argv[1], 'r') as f:
        results: List[Union[IPv6Network,IPv4Network]] = [ip_network(line.strip()) for line in f]
    result4 = [r for r in results if isinstance(r, IPv4Network)]
    result6 = [r for r in results if isinstance(r, IPv6Network)]

except Exception as e:
    print(f"Exception translating file {e!r}", file=sys.stderr)
    result = [IPv4Network("0.0.0.0/32")]

result_strings = sorted([str(net) for net in collapse_addresses(result4)])
result_strings.extend(sorted([str(net) for net in collapse_addresses(result6)]))

print(f'# Generated based on data from {sys.argv[2]}')
print('\n'.join(result_strings))
