#!/bin/bash

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
MEM=$(free -m | awk 'NR==2{printf "%.2f", $3*100/$2 }')
DISK=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

echo "CPU: $CPU%"
echo "Memory: $MEM%"
echo "Disk: $DISK%"

if (( ${CPU%.*} > 80 )); then
  echo "ALERT: CPU usage too high!" >> system_alert.log
fi
if (( ${MEM%.*} > 80 )); then
  echo "ALERT: Memory usage too high!" >> system_alert.log
fi
if (( DISK > 80 )); then
  echo "ALERT: Disk usage too high!" >> system_alert.log
fi
