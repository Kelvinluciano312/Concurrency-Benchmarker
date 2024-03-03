import threading
import time
import numpy as np
import matplotlib.pyplot as plt

# Flops count per second
def compute_flops(count):
    result = 0.0
    for i in range(count):
        result += (i * 1.1) / (i + 1.1) - (i * 1.1)

# IOPs count per second
def compute_iops(count):
    result = 0
    for i in range(count):
        result += (i * 2) // (i + 1) - (i * 2)

# Check the time and see how long it took to accomplish the task
class BenchmarkThread(threading.Thread):
    def __init__(self, function, count):
        super().__init__()
        self.function = function
        self.count = count

    def run(self):
        start_time = time.perf_counter()
        self.function(self.count)
        self.duration = time.perf_counter() - start_time

def run_benchmark(thread_count, operation_count, is_flops=True):
    threads = [BenchmarkThread(compute_flops if is_flops else compute_iops, operation_count) for _ in range(thread_count)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    durations = [thread.duration for thread in threads]

    return np.mean(durations), np.std(durations)

def main(thread_counts, operation_count=10000000, is_flops=True):
    avg_durations = []
    std_devs = []

    for thread_count in thread_counts:
        avg_duration, std_dev = run_benchmark(thread_count, operation_count, is_flops)
        avg_durations.append(avg_duration)
        std_devs.append(std_dev)
        print(f"{ 'FLOPS' if is_flops else 'IOPS' } Benchmark with {thread_count} threads: Avg duration = {avg_duration:.4f}s, Std Dev = {std_dev:.4f}")

    return avg_durations, std_devs

# Number of Threads being used
if __name__ == "__main__":
    thread_counts_custom = [1, 2, 4, 8]
    flops_avg, flops_std = main(thread_counts_custom, is_flops=True)
    iops_avg, iops_std = main(thread_counts_custom, is_flops=False)

    # Plotting results
    plt.figure(figsize=(10, 6))

    plt.errorbar(thread_counts_custom, flops_avg, yerr=flops_std, label='FLOPS', marker='o')
    plt.errorbar(thread_counts_custom, iops_avg, yerr=iops_std, label='IOPS', marker='o')

    plt.title('Benchmark Results')
    plt.xlabel('Thread Count')
    plt.ylabel('Duration (s)')
    plt.legend()
    plt.grid(True)
    plt.show()
