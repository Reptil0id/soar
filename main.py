import netmiko

def connect_to_cisco():
    device = {
        'device_type': 'cisco_ios',
        'ip': '192.168.253.2',
        'username': 'administrator',
        'password': 'admin',
        'port': 22,         
        'secret': '',        
        'verbose': False,    
    }

    connection = netmiko.ConnectHandler(**device)
    return connection

def main():
    connection = connect_to_cisco()
    version_info = connection.send_command('show version')
    startup_config = connection.send_command('show startup-config')
    running_config = connection.send_command('show running-config')
    acl_info = connection.send_command('show ip access-lists')
    interfaces_info = connection.send_command('show interfaces')
    

    print("Версия коммутатора:\n", version_info)
    print("\nСтартовая конфигурация:\n", startup_config)
    print("\nТекущая конфигурация:\n", running_config)
    print("\nСведения о списках контроля доступа:\n", acl_info)
    print("\nСведения об интерфейсах:\n", interfaces_info)

if __name__ == "__main__":
    main()
