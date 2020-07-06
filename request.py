import base64
import requests
import urllib3

### API SETTINGS
api_usr = ""
api_pwd = ""
message_id = 1
message_type = 9000 # 9000 echo test request
interface_id_hex = "D004005" # hex format
interface_id_dec = int(interface_id_hex, 16) # transfer into dec
remote_address = "127.0.0.1"

### Form <authdata> Tag.
authdata = '<authdata msg_id="{msg_id}" user="{user}" password="{password}" msg_type="{msg_type}" user_ip="{user_ip}" />'.format(
    msg_id = message_id,
    user = api_usr,
    password = api_pwd,
    msg_type = message_type,
    user_ip = remote_address
)

### Convert <authdata> to base64 and put in <auth> Tag.
authdata_bytes = authdata.encode('ascii')
base64_bytes = base64.b64encode(authdata_bytes)
base64_authdata = base64_bytes.decode('ascii')

xml = """<?xml version="1.0" encoding="UTF-8"?>
<sbapi>
    <header>
        <interface id="{interface_id}" version="8" />
        <message id="{message_id}" ignore_id="yes" type="{message_type}" created="2023-10-23T12:34:56Z" />
        <error id="0" />
        <auth pwd="open">{authdata}</auth>
    </header>
    <body>Hello Simbase!</body>
</sbapi>""".format(
    interface_id = interface_id_dec,
    message_id = message_id,
    message_type = message_type,
    authdata = base64_authdata
)

### Check XML structure
print(xml)

### Request
headers = {'Content-Type': 'text/xml'}
api_sb_url = "https://demo-api.simbase.eu"
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

### Send
responnse = requests.post(api_sb_url, data=data, headers=headers, verify=False)

### Check Response
print(responnse.text)
