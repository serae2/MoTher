import time
#import numpy as np
import tflite_runtime.interpreter as tflite

interpreter = tflite.Interpreter(model_path="/data/local/tmp/yolov5s-fp16-320.tflite", experimental_delegates=[tflite.load_delegate("libtensorflowlite_gpu_delegate.so")])
interpreter.allocate_tensors()

for i in range(100):
    t0 = time.time()
    interpreter.invoke()
    t1 = time.time()
    latency_ms = (t1 - t0) * 1000
    print(f"Inference {i}: [{t0}] {latency_ms:.3f} ms")
    time.sleep(0.033)