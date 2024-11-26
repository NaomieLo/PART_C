import os
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
file_path = "Performance_Testing/results/performance.csv"
data = pd.read_csv(file_path, skiprows=1)

# Rename columns
data.columns = ["Timestamp", "Available_Memory_MB", "CPU_Usage_Percent"]

# Drop missing values
data = data.dropna(subset=["CPU_Usage_Percent"])

# Convert to appropriate data types
data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data["Available_Memory_MB"] = pd.to_numeric(data["Available_Memory_MB"], errors="coerce")
data["CPU_Usage_Percent"] = pd.to_numeric(data["CPU_Usage_Percent"], errors="coerce")

# Debugging - Check if data is loaded correctly
print(data.head())

# Ensure output directory exists
plot_dir = "Performance_Testing/results/plots"
os.makedirs(plot_dir, exist_ok=True)

# Create the plot
plt.figure(figsize=(12, 8))  # Increased figure height for better spacing

# Plot CPU Usage
plt.subplot(2, 1, 1)
plt.plot(data["Timestamp"], data["CPU_Usage_Percent"], label="CPU Usage (%)", color="blue")
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.grid()
plt.legend()

# Plot Available Memory
plt.subplot(2, 1, 2)
plt.plot(data["Timestamp"], data["Available_Memory_MB"], label="Available Memory (MB)", color="green")
plt.xlabel("Time")
plt.ylabel("Available Memory (MB)")
plt.title("Available Memory Over Time")
plt.grid()
plt.legend()

# Adjust layout and save the plot
plt.tight_layout()
plt.subplots_adjust(hspace=0.5)  # Add more vertical space between plots
save_path = os.path.join(plot_dir, "cpu_memory_analysis.png")
plt.savefig(save_path)  # Save the plot BEFORE showing it

# Display the plot for debugging
plt.show()

print(f"Plot saved successfully at: {save_path}")
