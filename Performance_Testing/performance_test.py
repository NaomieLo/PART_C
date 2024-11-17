import time
from api_calls import create_random_todo
from monitor import log_system_usage
import matplotlib.pyplot as plt
import requests

API_URL = "http://localhost:4567"


def measure_create_time(n):
    ids = []
    start = time.time()
    for _ in range(n):
        ids.append(create_random_todo())
    elapsed = time.time() - start
    return ids, elapsed


def measure_update_time(ids):
    start = time.time()
    for todo_id in ids:
        update_data = {"title": "Updated Title", "description": "Updated Desc"}
        response = requests.put(API_URL + f"/todos/{todo_id}", json=update_data)
        assert response.status_code in [200, 204], f"Failed to update {todo_id}"
    elapsed = time.time() - start
    return elapsed


def measure_delete_time(ids):
    start = time.time()
    for todo_id in ids:
        response = requests.delete(API_URL + f"/todos/{todo_id}")
        assert response.status_code in [200, 204], f"Failed to delete {todo_id}"
    elapsed = time.time() - start
    return elapsed


def run_performance_tests():
    object_counts = [10, 100, 500, 1000]  # Number of objects to test
    results = []

    for n in object_counts:
        print(f"Testing with {n} objects...")
        log_system_usage()  # Log system state before the test

        # Measure create
        ids, create_time = measure_create_time(n)
        log_system_usage()  # Log after create

        # Measure update
        update_time = measure_update_time(ids)
        log_system_usage()  # Log after update

        # Measure delete
        delete_time = measure_delete_time(ids)
        log_system_usage()  # Log after delete

        results.append((n, create_time, update_time, delete_time))

    save_results(results)
    plot_results(results)


def save_results(results):
    with open("results/performance_logs/performance_results.txt", "w") as f:
        for n, create_time, update_time, delete_time in results:
            f.write(
                f"Objects: {n}, Create: {create_time}, Update: {update_time}, Delete: {delete_time}\n"
            )


def plot_results(results):
    counts, create_times, update_times, delete_times = zip(*results)
    plt.plot(counts, create_times, label="Create Time")
    plt.plot(counts, update_times, label="Update Time")
    plt.plot(counts, delete_times, label="Delete Time")
    plt.xlabel("Number of Objects")
    plt.ylabel("Time (seconds)")
    plt.title("Performance of API Operations")
    plt.legend()
    plt.savefig("results/plots/performance_graph.png")
    plt.show()


if __name__ == "__main__":
    run_performance_tests()
