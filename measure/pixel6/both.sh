#!/system/bin/sh

#for i in $(seq 0 7); do
#  echo performance > /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
#done

# CPU 부하 시작 (백그라운드 실행)
#/data/data/com.termux/files/usr/bin/python3 /data/local/tmp/cpu_burn.py &

# logger script 실행
sh /data/local/tmp/under.sh

#for i in $(seq 0 7); do
#  echo schedutil > /sys/devices/system/cpu/cpu$i/cpufreq/scaling_governor
#done