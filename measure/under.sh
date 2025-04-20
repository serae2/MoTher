###################################################################
#                                                                 #
#    objective: observation in COTS devices                       # 
#    device: pixel6                                               #
#                                                                 #
#    x-axis: time                                                 #
#    y-axis: - temperature[Modem/GPU/CPU/total]                   #
#            - application-level performance                      #
#            - power[Modem/GPU/CPU/total]                         #
#                                                                 #
###################################################################

###command: su -c "sh /data/local/tmp/under.sh"

#!/system/bin/sh

if [ "$(id -u)" != "0" ]; then
    echo "[INFO] Root required. Re-running with su..."
    exec su -c "$0" "$@"
fi

LOG_PATH="/sdcard/MoTher/log.txt"
#INTERVAL=0

while true; do
    TIME=$(date "+%Y-%m-%d %H:%M:%S.%3N")

    TEMP_CPU_BIG=$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null)
    TEMP_CPU_MID=$(cat /sys/class/thermal/thermal_zone1/temp 2>/dev/null)
    TEMP_CPU_LITTLE=$(cat /sys/class/thermal/thermal_zone2/temp 2>/dev/null)
    FREQ_CPU0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU1=$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU2=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU3=$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU4=$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU5=$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU6=$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU7=$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq 2>/dev/null)
    TEMP_GPU=$(cat /sys/class/thermal/thermal_zone3/temp 2>/dev/null)
    TEMP_MODEM=$(cat /sys/class/thermal/thermal_zone15/temp 2>/dev/null)
    TEMP_SOC=$(cat /sys/class/thermal/thermal_zone24/temp 2>/dev/null)

    CURR=$(cat /sys/class/power_supply/battery/current_now 2>/dev/null)
    VOLT=$(cat /sys/class/power_supply/battery/voltage_now 2>/dev/null)

    POWER=$(echo "$CURR * $VOLT / 1000000" | bc)  # μA * μV → mW

    echo "$TIME,$TEMP_CPU_BIG,$TEMP_CPU_MID,$TEMP_CPU_LITTLE,$TEMP_GPU,$TEMP_MODEM,$TEMP_SOC,$FREQ_CPU0,$FREQ_CPU1,$FREQ_CPU2,$FREQ_CPU3,$FREQ_CPU4,$FREQ_CPU5,$FREQ_CPU6,$FREQ_CPU7,$POWER" | tee -a "$LOG_PATH"

    #sleep $INTERVAL
done

