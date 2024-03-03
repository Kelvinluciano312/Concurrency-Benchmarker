# Concurrency Benchmarker: Exploring CPU Performance in FLOPS and IOPS

## Author
- **Kelvyn Luciano**
- Dept. of Computer Science
- Southern Connecticut State University
- New Haven, United States
- Email: lucianok4@southernct.edu

## I. INTRODUCTION TO PROJECT
The goal of this project is to create a benchmarking program that measures the computational performance of a computer, particularly focusing on CPU speed. The benchmarking program measures (Giga FLOPS per second) and (Giga IOPS per second) as a key indicator of the processor's capability in processing data. Additionally, the program evaluates the processor’s speed under different levels of concurrency, using 1, 2, 4, and 8 threads.

## II. DESIGN
### A. Overall Program Design
The program utilizes Python’s threading module to implement concurrent processing. It consists of functions that compute both floating points per second (FLOPS) and integer operations per second (IOPS). The main part of the program is the “run_benchmark” function, which creates threads, each dedicated to a specific computation task, and measures their execution time to calculate the average duration and standard deviation.

The advantages of using Python for such a task include its threading capabilities, facilitating a straightforward implementation of concurrent benchmarks.

### B. Design Tradeoffs
In the current design, each thread performs a fixed number of operations as specified by the `operation_count` parameter. This fixed granularity might lead to suboptimal performance in scenarios where the workload per thread varies significantly.

### C. Possible Improvements and Extensions
1. **Graphical User Interface (GUI):** Enhance the user experience by developing a simple GUI for configuring and running benchmarks in a visually intuitive manner.

2. **Additional Benchmarking Metrics:** Implement additional performance metrics, such as memory bandwidth, cache performance, or other relevant measures.

3. **Parameterized Test Cases:** Allow users to define custom test cases by providing their own functions for FLOPS and IOPS computation.

4. **Command-line Argument Parsing:** Consider incorporating argparse for more user-friendly configuration.

### D. Consideration of argparse
While argparse is a powerful tool for handling command-line arguments, the decision not to use it in this design was made to maintain simplicity. The program aims to be straightforward and easily understandable.

## III. MANUAL
### A. Introduction
This manual provides detailed instructions on how to run the benchmarking program designed to assess the computational performance of your computer, focusing on CPU speed. The program measures both Floating Point Operations per second and Integer Operations per Second with different levels of concurrency using threads.

**Prerequisites:** Python 3.x installed on the system (suggest using Anaconda; none of its libraries are being used, but it could be handy in case of future implementations such as argparse.)

### B. Steps to Run the Benchmark
1. Download the benchmarking program code from the source.
2. Navigate to the directory where the benchmarking program code is located using the terminal or command prompt.
3. Execute the following command to run the benchmarking program: `python benchmark.py`.

### C. Benchmark Configuration
The program is set to run four benchmarks with different thread counts (1, 2, 4, and 8 threads). Modify the ‘thread_counts_custom’ list in the code to include different thread counts.

Adjust the ‘operation_count’ parameter in the ‘main’ function to change the number of operations performed during the benchmark; the default is set to 10,000,000 operations.

### D. Run and Results
- Save the changes and rerun the program using the command mentioned before.
- The program will output the average duration and standard deviation for each benchmarked scenario. Results will be displayed for both FLOPS and IOPS, with varying thread counts.

