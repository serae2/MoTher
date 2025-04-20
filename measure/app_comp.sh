###command: su -c "sh /data/local/tmp/app_comp.sh"

#!/system/bin/sh

MODEL=/data/local/tmp/yolov5s-fp16-320.tflite
BIN=/data/local/tmp/benchmark_model
OUT=/data/local/tmp/lat_30fps.csv

echo "timestamp,latency_ms" > $OUT

for i in $(seq 1 100); do
  /data/local/tmp/benchmark_model \
    --graph=/data/local/tmp/yolov5s-fp16-320.tflite \
    --use_gpu=true \
    --num_runs=1 \
    --run_delay=0 \
    2>&1 | grep "Inference (avg):" | \
    while read line; do
        LATENCY_US=$(echo $line | sed -E 's/.*Inference \(avg\): ([0-9.]+).*/\1/')
        LATENCY_MS=$(echo "$LATENCY_US / 1000" | bc -l)
        NOW=$(date "+%Y-%m-%d %H:%M:%S")
        echo "$NOW,$LATENCY_MS" >> $OUT
    done
  sleep 0.033
done