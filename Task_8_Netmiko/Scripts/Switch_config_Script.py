from netmiko import ConnectHandler
config_file = "iosv_l2-confi.txt"
cisco_Switch = {
    "device_type": "cisco_ios",
    "host": "192.168.10.98",
    "username": "admindaan",
    "password": "Cisco",
    "secret": "cisco"}

with ConnectHandler(**cisco_Switch) as net_connect:
    
    net_connect.enable()
    output = net_connect.send_config_from_file(config_file)

    print (output)
    net_connect.disconnect()
