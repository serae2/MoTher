import pandas as pd
import matplotlib.pyplot as plt
##test

log_path = "/home/serae/Desktop/measure/log.txt" 


columns = [
    "time", "temp_big", "temp_mid", "temp_little",
    "temp_gpu", "temp_modem", "temp_soc",
    "freq0", "freq1", "freq2", "freq3", "freq4", "freq5", "freq6", "freq7", "freq_gpu", "power"
] # "freq_big_1"


df = pd.read_csv(log_path, names=columns)

# 시간 형식 변환
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S.%f")

# milli°C → °C
df["temp_big"] /= 1000
df["temp_mid"] /= 1000
df["temp_little"] /= 1000

# (Hz → MHz)
for i in range(8):
    df[f"freq{i}"] /= 1000000

# 그래프 그리기
fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(df["time"].values, df["temp_big"].values, label="BIG Temp (°C)", color="red")
ax1.plot(df["time"].values, df["temp_mid"].values, label="MID Temp (°C)", color="orange")
ax1.plot(df["time"].values, df["temp_little"].values, label="LITTLE Temp (°C)", color="green")
ax1.plot(df["time"].values, df["temp_gpu"].values, label="GPU Temp (°C)", color="pink")
ax1.plot(df["time"].values, df["temp_modem"].values, label="MODEM Temp (°C)", color="purple")
ax1.set_ylabel("Temperature (°C)")
ax1.set_xlabel("Time")
ax1.legend(loc="upper left")

ax2 = ax1.twinx()
#ax2.axhline(y = 1.803, color="green")
#ax2.axhline(y = 2.253, color="orange")
#ax2.axhline(y = 2.802, color="red")
ax2.axhline(y = 0.3, color="green")
ax2.axhline(y = 0.4, color="orange")
ax2.axhline(y = 0.5, color="red")
ax2.plot(df["time"].values, df["freq7"].values, label="CPU_BIG1 Freq (MHz)", color="red", alpha=1, linestyle="--")
ax2.plot(df["time"].values, df["freq6"].values, label="CPU_BIG0 Freq (MHz)", color="red", alpha=0.5, linestyle="--")
ax2.plot(df["time"].values, df["freq5"].values, label="CPU_MID1 Freq (MHz)", color="orange", alpha=1, linestyle="--")
ax2.plot(df["time"].values, df["freq4"].values, label="CPU_MID0 Freq (MHz)", color="orange", alpha=0.5, linestyle="--")
ax2.plot(df["time"].values, df["freq3"].values, label="CPU_LITTLE3 Freq (MHz)", color="green", alpha=1, linestyle="--")
ax2.plot(df["time"].values, df["freq2"].values, label="CPU_LITTLE2 Freq (MHz)", color="green", alpha=0.8, linestyle="--")
ax2.plot(df["time"].values, df["freq1"].values, label="CPU_LITTLE1 Freq (MHz)", color="green", alpha=0.6, linestyle="--")
ax2.plot(df["time"].values, df["freq0"].values, label="CPU_LITTLE0 Freq (MHz)", color="green", alpha=0.4, linestyle="--")
ax2.plot(df["time"].values, df["freq_gpu"].values, label="GPU Freq (MHz)", color="green", alpha=1, linestyle="--", zorder=1)
ax2.set_ylabel("Frequency (MHz)")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.show()

