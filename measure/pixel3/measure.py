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

import time
from datetime import datetime
LOG_PATH = "log.txt"

###################################################################
#                            CPU freq                             #
###################################################################

CPUS = range(8) # 0-3:little, 4-5:mid, 6-7:big
CPU_BASE = "/sys/devices/system/cpu"

def cpu_get_online(cpu):
    try:
        with open(f"{CPU_BASE}/cpu{cpu}/online") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "N" #"1"

def cpu_get_freq(cpu):
    try:
        with open(f"{CPU_BASE}/cpu{cpu}/cpufreq/scaling_cur_freq") as f:
            return f.read().strip()
    except FileNotFoundError:
            return "N" #"0"

###################################################################
#                   thermal[cpu/gpu/modem]                        #
###################################################################

THERMALS = {
    "cpu_big": 0,
    "cpu_mid": 1,
    "cpu_little": 2,
    "gpu": 3,
    "modem": 15,
    "soc": 24
}
THERMAL_PATH = "/sys/class/thermal"

def get_temp(zone):
    try:
        print(f"{THERMAL_PATH}/thermal_zone{zone}/temp")
        with open(f"{THERMAL_PATH}/thermal_zone{zone}/temp") as f:
            print(f.read())
            return str(int(f.read().strip()) / 1000.0)
    except:
        return "N" #"0"


###################################################################
#                     power[cpu/gpu/modem]                        #
#               will be replaced with monsoom...                  #
###################################################################

POWER_PATH = "/sys/class/power_supply/battery"

def get_power():
    try:
        with open(f"{POWER_PATH}/current_now") as f_curr, \
             open(f"{POWER_PATH}/voltage_now") as f_volt: ## microA*microV
            print(f_current.read(),f_volt.read())
            return str(int(f_curr.read().strip())*int(f_volt.read().strip()) // 1e6) #mW
    except:
        return "0"

#-----------------------------------------------------------------#
with open(LOG_PATH, "a") as logfile:
    try:
        while True:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            row = [now]
            
            for cpu in CPUS:
                row.append(cpu_get_online(cpu))
                row.append(cpu_get_freq(cpu))
            
            for _, zone in THERMALS.items():   
                row.append(get_temp(zone)) 
            
            row.append(get_power())
            line = ",".join(row)
            print(line)

            logfile.write(line + "\n")

            time.sleep(0.1) 
    except KeyboardInterrupt:
        print("Stopped.")