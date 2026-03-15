import threading
import time

# This is our shared resource
shared_counter = 0
# A lock ensures only one thread touches the counter at a time
counter_lock = threading.Lock()

def print_numbers():
    global shared_counter
    for i in range(1, 6):
        with counter_lock:
            shared_counter += 1
            print(f"[Thread 1] Printing: {i} | Shared Counter is now: {shared_counter}")
        time.sleep(0.5)  # Pause to let the other thread take a turn

def print_message():
    global shared_counter
    for i in range(5):
        with counter_lock:
            shared_counter += 1
            print(f"[Thread 2] Hello from thread! | Shared Counter is now: {shared_counter}")
        time.sleep(0.7) # Slightly different timing to show overlap

# 1. Create the threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_message)

# 2. Start the threads
print("--- Starting Threads ---")
t1.start()
t2.start()

# 3. Wait for both to finish before ending the main program
t1.join()
t2.join()

print("--- All threads finished! Final Counter:", shared_counter, "---")