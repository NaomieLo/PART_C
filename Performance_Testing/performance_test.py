import time
import matplotlib.pyplot as plt
import psutil
from api_calls import (
    create_random_todo,
    create_random_project,
    update_todo,
    update_project,
    delete_todo,
    delete_project,
)

# Measure create time
def measure_create_time(create_func, n):
    ids = []
    start = time.time()
    for _ in range(n):
        ids.append(create_func())
    elapsed = time.time() - start
    return ids, elapsed

# Measure update time
def measure_update_time(ids, update_func):
    start = time.time()
    for obj_id in ids:
        update_func(obj_id)
    elapsed = time.time() - start
    return elapsed

# Measure delete time
def measure_delete_time(ids, delete_func):
    start = time.time()
    for obj_id in ids:
        delete_func(obj_id)
    elapsed = time.time() - start
    return elapsed

# Log system resource usage
def log_system_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory

# Run performance tests
def run_performance_tests():
    object_counts = [10, 100, 500, 1000] 
    results = {"todos": [], "projects": []}

    for n in object_counts:
        print(f"\n=== Testing with {n} Objects ===\n")

        # Measure Todos
        print("[Todos]")
        cpu_before, mem_before = log_system_usage()
        todo_ids, todo_create_time = measure_create_time(create_random_todo, n)
        todo_update_time = measure_update_time(todo_ids, update_todo)
        todo_delete_time = measure_delete_time(todo_ids, delete_todo)
        cpu_after, mem_after = log_system_usage()
        results["todos"].append((n, todo_create_time, todo_update_time, todo_delete_time))

        print(f"Create Time: {todo_create_time:.2f}s, Update Time: {todo_update_time:.2f}s, Delete Time: {todo_delete_time:.2f}s")
        print(f"CPU Usage: Before {cpu_before}%, After {cpu_after}%")
        print(f"Memory Usage: Before {mem_before}%, After {mem_after}%\n")

        # Measure Projects
        print("[Projects]")
        cpu_before, mem_before = log_system_usage()
        project_ids, project_create_time = measure_create_time(create_random_project, n)
        project_update_time = measure_update_time(project_ids, update_project)
        project_delete_time = measure_delete_time(project_ids, delete_project)
        cpu_after, mem_after = log_system_usage()
        results["projects"].append((n, project_create_time, project_update_time, project_delete_time))

        print(f"Create Time: {project_create_time:.2f}s, Update Time: {project_update_time:.2f}s, Delete Time: {project_delete_time:.2f}s")
        print(f"CPU Usage: Before {cpu_before}%, After {cpu_after}%")
        print(f"Memory Usage: Before {mem_before}%, After {mem_after}%\n")

    save_results(results)
    plot_results(results)

# Save results to a file
def save_results(results):
    with open("results/performance_logs/performance_results.txt", "w") as f:
        for operation, data in results.items():
            for n, create_time, update_time, delete_time in data:
                f.write(
                    f"{operation.capitalize()} - Objects: {n}, Create: {create_time:.2f}s, Update: {update_time:.2f}s, Delete: {delete_time:.2f}s\n"
                )

# Plot results
def plot_results(results):
    for operation, data in results.items():
        counts, create_times, update_times, delete_times = zip(*data)
        plt.figure()
        plt.plot(counts, create_times, label="Create Time")
        plt.plot(counts, update_times, label="Update Time")
        plt.plot(counts, delete_times, label="Delete Time")
        plt.xlabel("Number of Objects")
        plt.ylabel("Time (seconds)")
        plt.title(f"Performance of {operation.capitalize()} Operations")
        plt.legend()
        plt.savefig(f"results/plots/{operation}_performance.png")
        plt.show()

if __name__ == "__main__":
    run_performance_tests()
