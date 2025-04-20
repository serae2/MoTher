import subprocess
import time
import re

INTERVAL = 1

def find_layer_name():
    output = subprocess.check_output([
        "dumpsys SurfaceFlinger --list"
    ]).decode()

    pattern = re.compile(r"SurfaceView\[com\.miHoYo\.GenshinImpact/.+?\]\(BLAST\)#\d+")
    matches = pattern.findall(output)

    if matches:
        return matches[-1]  
    return None

def measure_fps(layer_name):
    # latency-clear
    subprocess.run([
        f"dumpsys SurfaceFlinger --latency-clear '{layer_name}'"
    ], shell=True)

    time.sleep(INTERVAL)

    result = subprocess.check_output([
        f"dumpsys SurfaceFlinger --latency '{layer_name}'"
    ], shell=True).decode()

    lines = result.strip().split("\n")[1:]
    timestamps = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 3:
            timestamps.append(int(parts[2]))

    if len(timestamps) >= 2:
        duration_ns = timestamps[-1] - timestamps[0]
        frame_count = len(timestamps)
        fps = (frame_count - 1) / (duration_ns / 1e9)
        print(f"[{time.strftime('%H:%M:%S')}] FPS: {fps:.2f}")
    else:
        print(f"[{time.strftime('%H:%M:%S')}] Not enough frames")

if __name__ == "__main__":
    print("Start monitoring FPS every second...\n(Press Ctrl+C to stop)")
    try:
        while True:
            layer_name = find_layer_name()
            if not layer_name:
                print("GenshinImpact SurfaceView not found.")
                time.sleep(INTERVAL)
                continue
            measure_fps(layer_name)
    except KeyboardInterrupt:
        print("\nStopped.")
