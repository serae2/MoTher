import pandas as pd
import matplotlib.pyplot as plt


log_path = "/home/serae/Desktop/MoTher/measure/pixel5/T1/log.txt" 

columns = [
    "time", "temp_cpu_little_tot", "temp_cpu_bigmid_tot", "temp_little0", "temp_little1", "temp_little2", "temp_little3", "temp_little4", "temp_little5", "temp_mid", "temp_big", "temp_cpu8", "temp_cpu9",
    "temp_gpu0", "temp_gpu1", "temp_modem0", "temp_modem1", "temp_modem2", "temp_modem3", "temp_modem4", "temp_modem5", "temp_modem6", "temp_modem7", "temp_modem8", "temp_modem9",
    "freq0", "freq1", "freq2", "freq3", "freq4", "freq5", "freq6", "freq7", "freq_gpu",
    "cool_cur_cpu0", "cool_cur_cpu1", "cool_cur_cpu2", "cool_cur_cpu3", "cool_cur_cpu4", "cool_cur_gpu", "cool_cur_modem0", "cool_cur_modem1", "cool_cur_modem2", "cool_cur_modem3",
    "util_gpu"
] 


df = pd.read_csv(log_path, names=columns)

# 시간 형식 변환
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S.%f")

# milli°C → °C
df["temp_cpu_little_tot"] /= 1000
df["temp_cpu_bigmid_tot"] /= 1000
df["temp_little0"] /= 1000
df["temp_little1"] /= 1000
df["temp_little2"] /= 1000
df["temp_little3"] /= 1000
df["temp_little4"] /= 1000
df["temp_little5"] /= 1000
df["temp_mid"] /= 1000
df["temp_big"] /= 1000
df["temp_cpu8"] /= 1000
df["temp_cpu9"] /= 1000

df["temp_gpu0"] /= 1000
df["temp_gpu1"] /= 1000

df["temp_modem0"] /= 1000
df["temp_modem1"] /= 1000
df["temp_modem2"] /= 1000
df["temp_modem3"] /= 1000
df["temp_modem4"] /= 1000
df["temp_modem5"] /= 1000
df["temp_modem6"] /= 1000
df["temp_modem7"] /= 1000
df["temp_modem8"] /= 1000
df["temp_modem9"] /= 1000

# (Hz → MHz)
for i in range(8):
    df[f"freq{i}"] /= 1000000
df["freq_gpu"] /= 1000000

df["util_gpu"] = df["util_gpu"].str.replace(" %", "").astype(int)

# 그래프 그리기
fig, ax2 = plt.subplots(figsize=(12,6))


#ax2.axhline(y = 2.8032, color="red")
#ax2.axhline(y = 1.7664, color="green")
#ax2.axhline(y = 0.8256, color="red")
#ax2.axhline(y = 0.576, color="green")
#ax2.plot(df["time"].values, df["freq7"].values, label="CPU_BIG Freq (MHz)", color="blue", alpha=1, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq6"].values, label="CPU_MID Freq (MHz)", color="orange", alpha=0.8, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq0"].values, label="CPU_LITTLE0 Freq (MHz)", color="red", alpha=0.6, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq1"].values, label="CPU_LITTLE1 Freq (MHz)", color="red", alpha=0.4, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq2"].values, label="CPU_LITTLE2 Freq (MHz)", color="red", alpha=1, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq3"].values, label="CPU_LITTLE3 Freq (MHz)", color="red", alpha=0.8, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq4"].values, label="CPU_LITTLE4 Freq (MHz)", color="red", alpha=0.6, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq5"].values, label="CPU_LITTLE5 Freq (MHz)", color="red", alpha=0.4, linestyle="--", zorder=1)
ax2.plot(df["time"].values, df["freq_gpu"].values, label="GPU Freq (MHz)", color="green", alpha=1, linestyle="--", zorder=1)

#ax2.plot(df["time"].values, df["cool_cur_cpu2"].values, label="CPU_BIG cur_COOL", color="blue", alpha=1, linewidth=5)
#ax2.plot(df["time"].values, df["cool_cur_cpu1"].values, label="CPU_MID cur_COOL", color="orange", alpha=1, linewidth=3)
#ax2.plot(df["time"].values, df["cool_cur_cpu0"].values, label="CPU_LITTLE cur_COOL", color="red", alpha=1, linewidth=3)
###ax2.plot(df["time"].values, df["cool_cur_cpu4"].values, label="CPU_BM_VDD cur_COOL", color="blue", alpha=1) inactive
###ax2.plot(df["time"].values, df["cool_cur_cpu3"].values, label="CPU_L_VDD cur_COOL", color="red", alpha=1) inactive

ax2.plot(df["time"].values, df["cool_cur_gpu"].values, label="CPU_GPU cur_COOL", color="pink", alpha=1, linewidth=3)

#ax2.plot(df["time"].values, df["cool_cur_modem0"].values, label="MODEM_PA cur_COOL", color="purple", alpha=1, linewidth=3)
#ax2.plot(df["time"].values, df["cool_cur_modem1"].values, label="MODEM_PA_FR1 cur_COOL", color="purple", alpha=1, linewidth=3)
#ax2.plot(df["time"].values, df["cool_cur_modem2"].values, label="MODEM_DIEG cur_COOL", color="purple", alpha=1, linewidth=3)
#ax2.plot(df["time"].values, df["cool_cur_modem3"].values, label="MODEM_VDD cur_COOL", color="purple", alpha=1, linewidth=3)

ax2.set_ylabel("Frequency (MHz)")
ax2.legend(loc="upper right")

ax1 = ax2.twinx()
#ax1.plot(df["time"].values, df["temp_cpu_bigmid_tot"].values, label="BIG0 Temp (°C)", color="blue", zorder=100)
#ax1.plot(df["time"].values, df["temp_cpu_little_tot"].values, label="BIG0 Temp (°C)", color="red", zorder=100)
##ax1.plot(df["time"].values, df["temp_cpu8"].values, label="CPU9 Temp (°C)", color="black", zorder=100)
##ax1.plot(df["time"].values, df["temp_cpu9"].values, label="CPU8 Temp (°C)", color="black", zorder=100)
#ax1.plot(df["time"].values, df["temp_big"].values, label="BIG Temp (°C)", color="red", zorder=100)
#ax1.plot(df["time"].values, df["temp_mid"].values, label="MID Temp (°C)", color="blue", zorder=100)
#ax1.plot(df["time"].values, df["temp_little0"].values, label="LITTLE0 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little1"].values, label="LITTLE1 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little2"].values, label="LITTLE2 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little3"].values, label="LITTLE3 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little4"].values, label="LITTLE4 Temp (°C)", color="green", zorder=100)
#ax1.plot(df["time"].values, df["temp_little5"].values, label="LITTLE5 Temp (°C)", color="green", zorder=100)
ax1.plot(df["time"].values, df["temp_gpu0"].values, label="GPU0 Temp (°C)", color="pink", zorder=10)
ax1.plot(df["time"].values, df["temp_gpu1"].values, label="GPU1 Temp (°C)", color="pink", zorder=10)
#ax1.plot(df["time"].values, df["temp_modem0"].values, label="MODEM0 Temp (°C)", color="purple", zorder=10) #modem-lte-sub6-pa1 
##ax1.plot(df["time"].values, df["temp_modem1"].values, label="MODEM1 Temp (°C)", color="purple", zorder=10) #modem-lte-sub6-pa2
###ax1.plot(df["time"].values, df["temp_modem2"].values, label="MODEM2 Temp (°C)", color="purple", zorder=10) inactive
###ax1.plot(df["time"].values, df["temp_modem3"].values, label="MODEM3 Temp (°C)", color="purple", zorder=10) inactive
###ax1.plot(df["time"].values, df["temp_modem4"].values, label="MODEM4 Temp (°C)", color="purple", zorder=10) inactive
###ax1.plot(df["time"].values, df["temp_modem5"].values, label="MODEM5 Temp (°C)", color="purple", zorder=10) inactive
#ax1.plot(df["time"].values, df["temp_modem6"].values, label="MODEM6 Temp (°C)", color="purple", zorder=10) #close to other processor (modem-0-usr)
#ax1.plot(df["time"].values, df["temp_modem7"].values, label="MODEM7 Temp (°C)", color="purple", zorder=10) #close to other processor (modem-1-usr)
#ax1.plot(df["time"].values, df["temp_modem8"].values, label="MODEM8 Temp (°C)", color="purple", zorder=10) #mmw-side-therm
#ax1.plot(df["time"].values, df["temp_modem9"].values, label="MODEM9 Temp (°C)", color="purple", zorder=10) #pa-therm1
ax1.plot(df["time"].values, df["util_gpu"].values, label="GPU UTIL(%)", color="gray", zorder=10)
ax1.set_ylabel("Temperature (°C)")
ax1.set_xlabel("Time")
ax1.legend(loc="upper left")




plt.tight_layout()
plt.show()