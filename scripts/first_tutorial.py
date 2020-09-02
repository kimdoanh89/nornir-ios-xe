from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


# nr = InitNornir("nornir-local-config.yaml")
# result = nr.run(netmiko_send_command, command_string="sh version")
# print_result(result)


def main():
    nr = InitNornir("nornir-local-config.yaml")
    result = nr.run(netmiko_send_command, command_string="sh version")
    print_result(result)


if __name__ == "__main__":
    main()
