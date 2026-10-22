import threading, time

# Fibonacci Function
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Recursion = Function calling itself, function within a function
# Dis function doesn't run only once, it runs multiple times until the condition is met (n <= 0 or n == 1)
# 0 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765

# WITH MULTITHREADING -------------
def calculate_fibonacci(n, results, timings):
    start_time = time.perf_counter_ns() # Perform a counter start in nanosec

    result = fibonacci(n)

    end_time = time.perf_counter_ns() # Perform a counter end in nanosec

    # Save the result and timing information
    results[n] = result
    timings[n] = (start_time, end_time)


# Run the three Fibonacci calculations using threads
def run_multithreading():
    numbers = [35, 38, 40]

    results = {} # Dict
    timings = {} # Dict
    threads = [] # List

    # Create one separate thread for each Fibonacci calculation
    for n in numbers:
        thread = threading.Thread( # One Thread
            target=calculate_fibonacci,
            args=(n, results, timings)
        )
        threads.append(thread) # Add thread into the 3 threads

    # Start all three threads
    for thread in threads:
        thread.start()

    # Wait for all three threads to finish
    for thread in threads:
        thread.join()

    # Earliest thread start and latest thread finish
    first_start = min(start for start, end in timings.values())
    last_finish = max(end for start, end in timings.values())

    elapsed_time = last_finish - first_start

    return results, elapsed_time

def useMultiThread():
    total_times = []

    print("== Fibonacci WITH Multithreading ==")

    for round_number in range(1, 11):
        results, elapsed_time = run_multithreading()

        total_times.append(elapsed_time)

        print(f"\nRound {round_number}")
        print(f"Fibonacci(35) = {results[35]}")
        print(f"Fibonacci(38) = {results[38]}")
        print(f"Fibonacci(40) = {results[40]}")
        print(f"Total elapsed time: {elapsed_time:,} ns [{elapsed_time / 1_000_000_000:.6f} s]")

    # Calculate the average time across all 10 rounds
    average_time = sum(total_times) / len(total_times)

    print("\n===== Final Results =====")
    print(f"Total rounds: {len(total_times)}")
    print(f"Average elapsed time (WITH MULTITHREADING): {average_time:,.2f} ns [{elapsed_time / 1_000_000_000:.6f} s]")


# WITHOUT MULTITHREADING -------------

def without_multiThread():
    numbers = [35, 38, 40]
    results = {}

    start_time = time.perf_counter_ns()

    # Calculate one by one, sequentially
    for n in numbers:
        results[n] = fibonacci(n)

    end_time = time.perf_counter_ns()

    elapsed_time = end_time - start_time

    return results, elapsed_time


def withoutMultiThreading():
    total_times = []

    print("== Fibonacci Without Multithreading ==")

    # 10 Rounds Loop
    for round_number in range(1, 11):
        results, elapsed_time = without_multiThread() # Return one round of data
        total_times.append(elapsed_time)

        print(f"\nRound {round_number}")
        print(f"Fibonacci(35) = {results[35]}")
        print(f"Fibonacci(38) = {results[38]}")
        print(f"Fibonacci(40) = {results[40]}")
        print(f"Total elapsed time: {elapsed_time:,} ns [{elapsed_time / 1_000_000_000:.6f} s]")

    average_time = sum(total_times) / len(total_times)

    print("\n===== Final Results =====")
    print(f"Total rounds: {len(total_times)}")
    print(f"Average elapsed time: {average_time:,.2f} ns [{elapsed_time / 1_000_000_000:.6f} s]")


# Repeat the experiment for 10 rounds
def main():
    useMultiThread()
    withoutMultiThreading()    

if __name__ == "__main__":
    main()