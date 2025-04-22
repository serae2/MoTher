import pandas as pd
import matplotlib.pyplot as plt


log_path = "/home/serae/Desktop/measure/pixel3/T5/log.txt" 

columns = [
    "time", "temp_little0", "temp_little1", "temp_little2", "temp_little3", "temp_big0", "temp_big1", "temp_big2", "temp_big3", 
    "temp_gpu", "temp_modem0", "temp_modem1",
    "freq0", "freq1", "freq2", "freq3", "freq4", "freq5", "freq6", "freq7", "freq_gpu",
    "cool_cur_cpu0", "cool_cur_cpu1", "cool_cur_cpu2", "cool_cur_cpu3", "cool_cur_cpu4", "cool_cur_cpu5", "cool_cur_cpu6", "cool_cur_cpu7",
    "cool_cur_gpu", "cool_cur_modem_pa", "cool_cur_modem_proc", "util_gpu"
] # "freq_big_1"


df = pd.read_csv(log_path, names=columns)

# 시간 형식 변환
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S.%f")

# milli°C → °C
df["temp_big0"] /= 1000
df["temp_big1"] /= 1000
df["temp_big2"] /= 1000
df["temp_big3"] /= 1000
df["temp_little0"] /= 1000
df["temp_little1"] /= 1000
df["temp_little2"] /= 1000
df["temp_little3"] /= 1000
df["temp_gpu"] /= 1000
df["temp_modem0"] /= 1000
df["temp_modem1"] /= 1000


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
#ax2.plot(df["time"].values, df["freq4"].values, label="CPU_BIG0 Freq (MHz)", color="blue", alpha=1, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq5"].values, label="CPU_BIG1 Freq (MHz)", color="blue", alpha=0.8, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq6"].values, label="CPU_BIG2 Freq (MHz)", color="blue", alpha=0.6, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq7"].values, label="CPU_BIG3 Freq (MHz)", color="blue", alpha=0.4, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq0"].values, label="CPU_LITTLE0 Freq (MHz)", color="red", alpha=1, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq1"].values, label="CPU_LITTLE1 Freq (MHz)", color="red", alpha=0.8, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq2"].values, label="CPU_LITTLE2 Freq (MHz)", color="red", alpha=0.6, linestyle="--", zorder=1)
#ax2.plot(df["time"].values, df["freq3"].values, label="CPU_LITTLE3 Freq (MHz)", color="red", alpha=0.4, linestyle="--", zorder=1)
ax2.plot(df["time"].values, df["freq_gpu"].values, label="GPU Freq (MHz)", color="green", alpha=1, linestyle="--", zorder=1)

#ax2.plot(df["time"].values, df["cool_cur_cpu4"].values, label="CPU_BIG0 cur_COOL", color="red", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu5"].values, label="CPU_BIG1 cur_COOL", color="red", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu6"].values, label="CPU_BIG2 cur_COOL", color="red", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu7"].values, label="CPU_BIG3 cur_COOL", color="red", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu0"].values, label="CPU_LITTLE0 cur_COOL", color="green", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu1"].values, label="CPU_LITTLE1 cur_COOL", color="green", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu2"].values, label="CPU_LITTLE2 cur_COOL", color="green", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_cpu3"].values, label="CPU_LITTLE3 cur_COOL", color="green", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_gpu"].values, label="GPU cur_COOL", color="pink", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_modem_pa"].values, label="MODEM_PA cur_COOL", color="purple", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_modem_proc"].values, label="MODEM_PROC cur_COOL", color="purple", alpha=1)

ax2.set_ylabel("Frequency (MHz)")
ax2.legend(loc="upper right")

ax1 = ax2.twinx()
#ax1.plot(df["time"].values, df["temp_big0"].values, label="BIG0 Temp (°C)", color="red", zorder=100)
#ax1.plot(df["time"].values, df["temp_big1"].values, label="BIG1 Temp (°C)", color="red", zorder=100)
#ax1.plot(df["time"].values, df["temp_big2"].values, label="BIG2 Temp (°C)", color="red", zorder=100)
#ax1.plot(df["time"].values, df["temp_big3"].values, label="BIG3 Temp (°C)", color="red", zorder=100)
#ax1.plot(df["time"].values, df["temp_little0"].values, label="LITTLE0 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little1"].values, label="LITTLE0 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little2"].values, label="LITTLE0 Temp (°C)", color="green", zorder=10)
#ax1.plot(df["time"].values, df["temp_little3"].values, label="LITTLE0 Temp (°C)", color="green", zorder=10)
ax1.plot(df["time"].values, df["temp_gpu"].values, label="GPU0 Temp (°C)", color="pink", zorder=10)
#ax1.plot(df["time"].values, df["temp_modem0"].values, label="MODEM0 Temp (°C)", color="purple", zorder=10)
ax1.plot(df["time"].values, df["util_gpu"].values, label="GPU UTIL(%)", color="gray", zorder=10)
#ax1.plot(df["time"].values, df["temp_modem1"].values, label="MODEM1 Temp (°C)", color="purple")
ax1.set_ylabel("Temperature (°C)")
ax1.set_xlabel("Time")
ax1.legend(loc="upper left")




plt.tight_layout()
plt.show()