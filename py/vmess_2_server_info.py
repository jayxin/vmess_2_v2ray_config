import base64
import json
import re
import sys


def extract_vmess_info(vmess_address):
    """
    Extract information from VMESS address
    """

    """
    Regular expression pattern to match the base64-encoded JSON payload
    """
    pattern = r"vmess://(.*)"
    match = re.match(pattern, vmess_address)

    if match:
        base64_payload = match.group(1)
        try:
            decoded_payload = base64.b64decode(base64_payload).decode('utf-8')
            """
            Parse the decoded payload JSON to extract the information you need
            """
            vmess_info = json.loads(decoded_payload)
            # server = vmess_info['add']
            # port = vmess_info['port']
            # user_id = vmess_info['id']
            # security = vmess_info.get('tls', '')
            print(vmess_info)

            # return server, port, user_id, security
        except ValueError as e:
            print("Invalid VMESS address:", e)
    else:
        print("Invalid VMESS address")


def vmess_2_server_info(argv):
    if len(argv) < 2:
        print(f"Usage: {argv[0]} filename")
        sys.exit(-1)
    else:
        with open(argv[1], "r") as f:
            lines = f.readlines()
            for vmess_address in lines:
                # Extract information from VMESS address
                extract_vmess_info(vmess_address)


if __name__ == "__main__":
    argv = sys.argv
    vmess_2_server_info(argv)
