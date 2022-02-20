# ░█████╗░██╗░░░██╗███╗░░░███╗░█████╗░██╗░░██╗░█████╗░███╗░░██╗░░░░░░░██████╗██████╗░██╗░░██╗
# ██╔══██╗╚██╗░██╔╝████╗░████║██╔══██╗██║░██╔╝██╔══██╗████╗░██║░░░░░░██╔════╝██╔══██╗██║░██╔╝
# ███████║░╚████╔╝░██╔████╔██║███████║█████═╝░███████║██╔██╗██║█████╗╚█████╗░██║░░██║█████═╝░
# ██╔══██║░░╚██╔╝░░██║╚██╔╝██║██╔══██║██╔═██╗░██╔══██║██║╚████║╚════╝░╚═══██╗██║░░██║██╔═██╗░
# ██║░░██║░░░██║░░░██║░╚═╝░██║██║░░██║██║░╚██╗██║░░██║██║░╚███║░░░░░░██████╔╝██████╔╝██║░╚██╗
# ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═════╝░╚═════╝░╚═╝░░╚═╝

"""
AyMakan SDK Library
~~~~~~~~~~~~~~~~~~~~~

This is the official Aymakan Python SDK. It can be used to integrate with Aymakan APIs.
Basic usage:

from aymakan-sdk import Client

client = Client()

client.setSandBox()
client.setApiKey(token)

data = {
    request data
    ...
    ...
}

res = client.createShipment(data)

print(res.url)         <-- for response URL
print(res.status_code) <-- for response status code
print(res.json())      <-- for response data in JSON format

for the other usages - see the full documentation at <https://github.com/aymakan/python-sdk/>.

:copyright: (c) 2022 by Abdullah AlQattan.
:license: Apache 2.0, see LICENSE for more details.
"""
from src.Client import Client