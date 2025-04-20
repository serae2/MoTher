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

    TEMP_CPU0=$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null)
    TEMP_CPU1=$(cat /sys/class/thermal/thermal_zone1/temp 2>/dev/null)
    TEMP_CPU2=$(cat /sys/class/thermal/thermal_zone2/temp 2>/dev/null)
    TEMP_CPU3=$(cat /sys/class/thermal/thermal_zone3/temp 2>/dev/null)
    TEMP_CPU4=$(cat /sys/class/thermal/thermal_zone4/temp 2>/dev/null)
    TEMP_CPU5=$(cat /sys/class/thermal/thermal_zone5/temp 2>/dev/null)
    TEMP_CPU6=$(cat /sys/class/thermal/thermal_zone6/temp 2>/dev/null)
    TEMP_CPU7=$(cat /sys/class/thermal/thermal_zone7/temp 2>/dev/null)

    FREQ_CPU0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU1=$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU2=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU3=$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU4=$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU5=$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU6=$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq 2>/dev/null)
    FREQ_CPU7=$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq 2>/dev/null)


    TEMP_GPU0=$(cat /sys/class/thermal/thermal_zone8/temp 2>/dev/null)
    FREQ_GPU=$(cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq 2>/dev/null)
    UTIL_GPU=$(cat /sys/class/kgsl/kgsl-3d0/gpu_busy_percentage 2>/dev/null)

    TEMP_MODEM0=$(cat /sys/class/thermal/thermal_zone37/temp 2>/dev/null)
    TEMP_MODEM1=$(cat /sys/class/thermal/thermal_zone43/temp 2>/dev/null)

    COOL_CUR_GPU=$(cat /sys/class/thermal/cooling_device1/cur_state 2>/dev/null)
    COOL_CUR_CPU0=$(cat /sys/class/thermal/cooling_device3/cur_state 2>/dev/null)
    COOL_CUR_CPU1=$(cat /sys/class/thermal/cooling_device4/cur_state 2>/dev/null)
    COOL_CUR_CPU2=$(cat /sys/class/thermal/cooling_device5/cur_state 2>/dev/null)
    COOL_CUR_CPU3=$(cat /sys/class/thermal/cooling_device6/cur_state 2>/dev/null)
    COOL_CUR_CPU4=$(cat /sys/class/thermal/cooling_device7/cur_state 2>/dev/null)
    COOL_CUR_CPU5=$(cat /sys/class/thermal/cooling_device8/cur_state 2>/dev/null)
    COOL_CUR_CPU6=$(cat /sys/class/thermal/cooling_device9/cur_state 2>/dev/null)
    COOL_CUR_CPU7=$(cat /sys/class/thermal/cooling_device10/cur_state 2>/dev/null)
    COOL_CUR_MODEM_PA=$(cat /sys/class/thermal/cooling_device17/cur_state 2>/dev/null)
    COOL_CUR_MODEM_PROC=$(cat /sys/class/thermal/cooling_device18/cur_state 2>/dev/null)

    CURR=$(cat /sys/class/power_supply/battery/current_now 2>/dev/null)
    VOLT=$(cat /sys/class/power_supply/battery/voltage_now 2>/dev/null)

    POWER=$(echo "$CURR * $VOLT / 1000000" | bc)  # μA * μV → mW

    echo "$TIME,$TEMP_CPU0,$TEMP_CPU1,$TEMP_CPU2,$TEMP_CPU3,$TEMP_CPU4,$TEMP_CPU5,$TEMP_CPU6,$TEMP_CPU7,$TEMP_GPU0,$TEMP_MODEM0,$TEMP_MODEM1,$FREQ_CPU0,$FREQ_CPU1,$FREQ_CPU2,$FREQ_CPU3,$FREQ_CPU4,$FREQ_CPU5,$FREQ_CPU6,$FREQ_CPU7,$FREQ_GPU,$COOL_CUR_CPU0,$COOL_CUR_CPU1,$COOL_CUR_CPU2,$COOL_CUR_CPU3,$COOL_CUR_CPU4,$COOL_CUR_CPU5,$COOL_CUR_CPU6,$COOL_CUR_CPU7,$COOL_CUR_GPU,$COOL_CUR_MODEM_PA,$COOL_CUR_MODEM_PROC,$UTIL_GPU" | tee -a "$LOG_PATH"

    #sleep $INTERVAL
done