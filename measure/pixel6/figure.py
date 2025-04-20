import pandas as pd
import matplotlib.pyplot as plt


log_path = "/home/serae/Desktop/measure/pixel6/1__log.txt" 


columns = [
    "time", "temp_big", "temp_mid", "temp_little",
    "temp_gpu", "temp_modem", "temp_soc",
    "freq0", "freq1", "freq2", "freq3", "freq4", "freq5", "freq6", "freq7", 
    "cool_req_big", "cool_req_mid", "cool_req_little", "cool_req_gpu"]#, "cool_cur_big", "cool_cur_mid", "cool_cur_little", "cool_cur_gpu"
 # "freq_big_1"


df = pd.read_csv(log_path, names=columns)

# 시간 형식 변환
df["time"] = pd.to_datetime(df["time"], format="%Y-%m-%d %H:%M:%S.%f")

# milli°C → °C
df["temp_big"] /= 1000
df["temp_mid"] /= 1000
df["temp_little"] /= 1000
df["temp_gpu"] /= 1000
df["temp_modem"] /= 1000


# (Hz → MHz)
for i in range(8):
    df[f"freq{i}"] /= 1000000

# 그래프 그리기
fig, ax2 = plt.subplots(figsize=(12,6))


#ax2.axhline(y = 1.803, color="green")
#ax2.axhline(y = 2.253, color="orange")
#ax2.axhline(y = 2.802, color="red")
#ax2.axhline(y = 0.3, color="green")
#ax2.axhline(y = 0.4, color="orange")
#ax2.axhline(y = 0.5, color="red")
#ax2.plot(df["time"].values, df["freq7"].values, label="CPU_BIG1 Freq (MHz)", color="blue", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["freq6"].values, label="CPU_BIG0 Freq (MHz)", color="blue", alpha=0.5, linestyle="--")
#ax2.plot(df["time"].values, df["freq5"].values, label="CPU_MID1 Freq (MHz)", color="orange", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["freq4"].values, label="CPU_MID0 Freq (MHz)", color="orange", alpha=0.5, linestyle="--")
#ax2.plot(df["time"].values, df["freq3"].values, label="CPU_LITTLE3 Freq (MHz)", color="green", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["freq2"].values, label="CPU_LITTLE2 Freq (MHz)", color="green", alpha=0.8, linestyle="--")
#ax2.plot(df["time"].values, df["freq1"].values, label="CPU_LITTLE1 Freq (MHz)", color="green", alpha=0.6, linestyle="--")
#ax2.plot(df["time"].values, df["freq0"].values, label="CPU_LITTLE0 Freq (MHz)", color="green", alpha=0.4, linestyle="--")


#ax2.plot(df["time"].values, df["cool_req_big"].values, label="CPU_BIG req_COOL", color="red", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["cool_req_mid"].values, label="CPU_MID req_COOL", color="orange", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["cool_req_little"].values, label="CPU_LITTLE req_COOL", color="green", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["cool_req_gpu"].values, label="GPU req_COOL", color="pink", alpha=1, linestyle="--")
#ax2.plot(df["time"].values, df["cool_cur_big"].values, label="CPU_BIG cur_COOL", color="red", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_mid"].values, label="CPU_MID cur_COOL", color="orange", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_little"].values, label="CPU_LITTLE cur_COOL", color="green", alpha=1)
#ax2.plot(df["time"].values, df["cool_cur_gpu"].values, label="GPU cur_COOL", color="pink", alpha=1)

ax1 = ax2.twinx()
ax1.plot(df["time"].values, df["temp_big"].values, label="BIG Temp (°C)", color="red")
ax1.plot(df["time"].values, df["temp_mid"].values, label="MID Temp (°C)", color="orange")
ax1.plot(df["time"].values, df["temp_little"].values, label="LITTLE Temp (°C)", color="green")
ax1.plot(df["time"].values, df["temp_gpu"].values, label="GPU Temp (°C)", color="pink")
ax1.plot(df["time"].values, df["temp_modem"].values, label="MODEM Temp (°C)", color="purple")
ax1.set_ylabel("Temperature (°C)")
ax1.set_xlabel("Time")
ax1.legend(loc="upper left")

ax2.set_ylabel("Frequency (MHz) and State")
ax2.legend(loc="upper right")

plt.tight_layout()
plt.show()

