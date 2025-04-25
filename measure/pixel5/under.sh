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

declare -a PREV_TOTAL PREV_IDLE

if [ "$(id -u)" != "0" ]; then
    echo "[INFO] Root required. Re-running with su..."
    exec su -c "$0" "$@"
fi

LOG_PATH="/sdcard/MoTher/log.txt"
#INTERVAL=0

#cpuN user nice system idle iowait irq softirq steal guest guest_nice
for i in $(seq 0 8); do
    LINE=($(grep "^cpu$i " /proc/stat))
    IDLE=$((LINE[4] + LINE[5]))
    TOTAL=0
    for val in "${LINE[@]:1:8}"; do TOTAL=$((TOTAL + val)); done
    PREV_TOTAL[$i]=$TOTAL
    PREV_IDLE[$i]=$IDLE
done

while true; do
    TIME=$(date "+%Y-%m-%d %H:%M:%S.%3N")

    TEMP_CPU_LITTLE_TOT=$(cat /sys/class/thermal/thermal_zone23/temp 2>/dev/null)
    TEMP_CPU_BIGMID_TOT=$(cat /sys/class/thermal/thermal_zone24/temp 2>/dev/null)
    TEMP_CPU0=$(cat /sys/class/thermal/thermal_zone17/temp 2>/dev/null) #little0
    TEMP_CPU1=$(cat /sys/class/thermal/thermal_zone18/temp 2>/dev/null) #little1
    TEMP_CPU2=$(cat /sys/class/thermal/thermal_zone19/temp 2>/dev/null) #little2
    TEMP_CPU3=$(cat /sys/class/thermal/thermal_zone20/temp 2>/dev/null) #little3
    TEMP_CPU4=$(cat /sys/class/thermal/thermal_zone21/temp 2>/dev/null) #little4
    TEMP_CPU5=$(cat /sys/class/thermal/thermal_zone22/temp 2>/dev/null) #little5
    TEMP_CPU6=$(cat /sys/class/thermal/thermal_zone25/temp 2>/dev/null) #mid
    TEMP_CPU7=$(cat /sys/class/thermal/thermal_zone26/temp 2>/dev/null) #big
    TEMP_CPU8=$(cat /sys/class/thermal/thermal_zone27/temp 2>/dev/null) #??
    TEMP_CPU9=$(cat /sys/class/thermal/thermal_zone28/temp 2>/dev/null) #??

    TEMP_GPU0=$(cat /sys/class/thermal/thermal_zone29/temp 2>/dev/null)
    TEMP_GPU1=$(cat /sys/class/thermal/thermal_zone30/temp 2>/dev/null)
    
    TEMP_MODEM0=$(cat /sys/class/thermal/thermal_zone0/temp 2>/dev/null) #modem-lte-sub6-pa1
    TEMP_MODEM1=$(cat /sys/class/thermal/thermal_zone1/temp 2>/dev/null) #modem-lte-sub6-pa2
    TEMP_MODEM2=$(cat /sys/class/thermal/thermal_zone2/temp 2>/dev/null) #modem-mmw0-usr
    TEMP_MODEM3=$(cat /sys/class/thermal/thermal_zone3/temp 2>/dev/null) #modem-mmw1-usr
    TEMP_MODEM4=$(cat /sys/class/thermal/thermal_zone4/temp 2>/dev/null) #modem-mmw2-usr
    TEMP_MODEM5=$(cat /sys/class/thermal/thermal_zone5/temp 2>/dev/null) #modem-mmw3-usr
    TEMP_MODEM6=$(cat /sys/class/thermal/thermal_zone9/temp 2>/dev/null) #modem-0-usr
    TEMP_MODEM7=$(cat /sys/class/thermal/thermal_zone10/temp 2>/dev/null) #modem-1-usr
    TEMP_MODEM8=$(cat /sys/class/thermal/thermal_zone89/temp 2>/dev/null) #mmw-side-therm
    TEMP_MODEM9=$(cat /sys/class/thermal/thermal_zone90/temp 2>/dev/null) #	pa-therm1


    FREQ_CPU0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU1=$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU2=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU3=$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU4=$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU5=$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_cur_freq 2>/dev/null) #little
    FREQ_CPU6=$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_cur_freq 2>/dev/null) #middle
    FREQ_CPU7=$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_cur_freq 2>/dev/null) #big
    FREQ_GPU=$(cat /sys/class/kgsl/kgsl-3d0/devfreq/cur_freq 2>/dev/null)
    

    UTIL_GPU=$(cat /sys/class/kgsl/kgsl-3d0/gpu_busy_percentage 2>/dev/null)

    for i in $(seq 0 8); do
        LINE=($(grep "^cpu$i " /proc/stat))
        CUR_IDLE=$((LINE[4] + LINE[5]))

        LINE=($(grep "^cpu$i " /proc/stat))
        CUR_IDLE=$((LINE[4] + LINE[5]))
        CUR_TOTAL=0
        for val in "${LINE[@]:1:8}"; do CUR_TOTAL=$((CUR_TOTAL + val)); done

        DIFF_IDLE=$((CUR_IDLE - PREV_IDLE[$i]))
        DIFF_TOTAL=$((CUR_TOTAL - PREV_TOTAL[$i]))

        if [ "$DIFF_TOTAL" -gt 0 ]; then
            UTIL=$((100 * (DIFF_TOTAL - DIFF_IDLE) / DIFF_TOTAL))
        else
            UTIL=0
        fi

        eval UTIL_CPU$i=$UTIL
        
        PREV_TOTAL[$i]=$CUR_TOTAL
        PREV_IDLE[$i]=$CUR_IDLE

    done

############
    
    FREQ_MIN_CPU0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU1=$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU2=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU3=$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU4=$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU5=$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_min_freq 2>/dev/null) #little
    FREQ_MIN_CPU6=$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_min_freq 2>/dev/null) #middle
    FREQ_MIN_CPU7=$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_min_freq 2>/dev/null) #big

    FREQ_MIN_GPU=$(cat /sys/class/kgsl/kgsl-3d0/devfreq/min_freq 2>/dev/null)

    FREQ_MAX_CPU0=$(cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU1=$(cat /sys/devices/system/cpu/cpu1/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU2=$(cat /sys/devices/system/cpu/cpu2/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU3=$(cat /sys/devices/system/cpu/cpu3/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU4=$(cat /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU5=$(cat /sys/devices/system/cpu/cpu5/cpufreq/scaling_max_freq 2>/dev/null) #little
    FREQ_MAX_CPU6=$(cat /sys/devices/system/cpu/cpu6/cpufreq/scaling_max_freq 2>/dev/null) #middle
    FREQ_MAX_CPU7=$(cat /sys/devices/system/cpu/cpu7/cpufreq/scaling_max_freq 2>/dev/null) #big

    FREQ_MAX_GPU=$(cat /sys/class/kgsl/kgsl-3d0/devfreq/max_freq 2>/dev/null)
    
############

    COOL_CUR_GPU=$(cat /sys/class/thermal/cooling_device14/cur_state 2>/dev/null)
    COOL_CUR_CPU0=$(cat /sys/class/thermal/cooling_device0/cur_state 2>/dev/null) #little
    COOL_CUR_CPU1=$(cat /sys/class/thermal/cooling_device1/cur_state 2>/dev/null) #middle
    COOL_CUR_CPU2=$(cat /sys/class/thermal/cooling_device2/cur_state 2>/dev/null) #big
    COOL_CUR_CPU3=$(cat /sys/class/thermal/cooling_device11/cur_state 2>/dev/null) #little_vdd
    COOL_CUR_CPU4=$(cat /sys/class/thermal/cooling_device12/cur_state 2>/dev/null) #big/mid_vdd
    COOL_CUR_MODEM0=$(cat /sys/class/thermal/cooling_device24/cur_state 2>/dev/null) #_PA
    COOL_CUR_MODEM1=$(cat /sys/class/thermal/cooling_device25/cur_state 2>/dev/null) #_PA_FR1
    COOL_CUR_MODEM2=$(cat /sys/class/thermal/cooling_device26/cur_state 2>/dev/null) #modem die
    COOL_CUR_MODEM3=$(cat /sys/class/thermal/cooling_device27/cur_state 2>/dev/null) #modem_vdd

    CURR=$(cat /sys/class/power_supply/battery/current_now 2>/dev/null)
    VOLT=$(cat /sys/class/power_supply/battery/voltage_now 2>/dev/null)

    POWER=$(echo "$CURR * $VOLT / 1000000" | bc)  # μA * μV → mW

    echo "$TIME,$TEMP_CPU_LITTLE_TOT,$TEMP_CPU_BIGMID_TOT,$TEMP_CPU0,$TEMP_CPU1,$TEMP_CPU2,$TEMP_CPU3,$TEMP_CPU4,$TEMP_CPU5,$TEMP_CPU6,$TEMP_CPU7,$TEMP_CPU8,$TEMP_CPU9,$TEMP_GPU0,$TEMP_GPU1,$TEMP_MODEM0,$TEMP_MODEM1,$TEMP_MODEM2,$TEMP_MODEM3,$TEMP_MODEM4,$TEMP_MODEM5,$TEMP_MODEM6,$TEMP_MODEM7,$TEMP_MODEM8,$TEMP_MODEM9,$FREQ_CPU0,$FREQ_CPU1,$FREQ_CPU2,$FREQ_CPU3,$FREQ_CPU4,$FREQ_CPU5,$FREQ_CPU6,$FREQ_CPU7,$FREQ_GPU,$FREQ_MIN_CPU0,$FREQ_MIN_CPU1,$FREQ_MIN_CPU2,$FREQ_MIN_CPU3,$FREQ_MIN_CPU4,$FREQ_MIN_CPU5,$FREQ_MIN_CPU6,$FREQ_MIN_CPU7,$FREQ_MIN_GPU,$FREQ_MAX_CPU0,$FREQ_MAX_CPU1,$FREQ_MAX_CPU2,$FREQ_MAX_CPU3,$FREQ_MAX_CPU4,$FREQ_MAX_CPU5,$FREQ_MAX_CPU6,$FREQ_MAX_CPU7,$FREQ_MAX_GPU,$COOL_CUR_CPU0,$COOL_CUR_CPU1,$COOL_CUR_CPU2,$COOL_CUR_CPU3,$COOL_CUR_CPU4,$COOL_CUR_GPU,$COOL_CUR_MODEM0,$COOL_CUR_MODEM1,$COOL_CUR_MODEM2,$COOL_CUR_MODEM3,$UTIL_CPU0,$UTIL_CPU1,$UTIL_CPU2,$UTIL_CPU3,$UTIL_CPU4,$UTIL_CPU5,$UTIL_CPU6,$UTIL_CPU7,$UTIL_GPU,$POWER" | tee -a "$LOG_PATH"

    #sleep $INTERVAL
done
