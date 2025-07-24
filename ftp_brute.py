from ftplib import FTP, error_perm, all_errors

# Загрузка IP-адресов из файла
with open("ips/ftp_ips.txt", "r") as f:
    ips = [line.strip() for line in f if line.strip()]

# Учетные данные
username = "admin"
password = "admin"

# Открываем файл для записи успешных IP
with open("success/ftp_success.txt", "w") as success_file:
    for ip in ips:
        try:
            print(f"[.] Пробую {ip} ...")
            try:
                ftp = FTP()
                ftp.connect(ip, 21, timeout=5)
                ftp.login(user=username, passwd=password)
                print(f"[+] УСПЕШНО: {ip} — FTP доступен с {username}:{password}")
                success_file.write(ip + "\n")
                ftp.quit()
            except error_perm as e:
                print(f"[-] ОТКАЗ: {ip} — Неверный логин или права: {e}")
            except all_errors as e:
                print(f"[!] Ошибка подключения к {ip}: {e}")
        except Exception as e:
            print(f"[!!!] Непредвиденная ошибка с {ip}: {e}")
                                                              
