from nornir import InitNornir
from nornir.plugins.functions.text import print_result


import httpx


def fetch_and_parse_lldp_data(task):
    url = f"https://{task.host.hostname}/restconf/data/Cisco-IOS-XE-lldp-oper:lldp-entries/lldp-entry"
    headers = {
        "Accept": "application/yang-data+json"
    }
    response = httpx.get(
        url,
        headers=headers,
        auth=(task.host.username, task.host.password),
        verify=False
    )
    data = response.json()
    return data


def main():
    nr = InitNornir("nornir-local-config.yaml")
    result = nr.run(fetch_and_parse_lldp_data)
    print_result(result)


if __name__ == "__main__":
    main()
