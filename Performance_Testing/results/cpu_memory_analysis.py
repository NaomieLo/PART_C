import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the CSV file
file_path = r"C:/Users/deniz/Desktop/performance2.csv"
data = pd.read_csv(file_path, skiprows=1)  # Skip the first descriptive row

data.columns = ["Timestamp", "Available_Memory_MB", "CPU_Usage_Percent"]
data = data.dropna(subset=["CPU_Usage_Percent"])

# Convert the columns to appropriate data types
data["Timestamp"] = pd.to_datetime(data["Timestamp"])
data["Available_Memory_MB"] = pd.to_numeric(data["Available_Memory_MB"], errors="coerce")
data["CPU_Usage_Percent"] = pd.to_numeric(data["CPU_Usage_Percent"], errors="coerce")

# Plot CPU Usage and Available Memory
plt.figure(figsize=(12, 6))

# Plot CPU Usage
plt.subplot(2, 1, 1)
plt.plot(data["Timestamp"], data["CPU_Usage_Percent"], label="CPU Usage (%)", color="blue", marker="o")
plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))  # Format x-axis as HH:MM:SS
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xlabel("Time")
plt.ylabel("CPU Usage (%)")
plt.title("CPU Usage Over Time")
plt.grid()
plt.legend()

# Plot Available Memory
plt.subplot(2, 1, 2)
plt.plot(data["Timestamp"], data["Available_Memory_MB"], label="Available Memory (MB)", color="green", marker="o")
plt.gca().xaxis.set_major_formatter(DateFormatter("%H:%M:%S"))  # Format x-axis as HH:MM:SS
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xlabel("Time")
plt.ylabel("Available Memory (MB)")
plt.title("Available Memory Over Time")
plt.grid()
plt.legend()

# Adjust layout and show the plots
plt.tight_layout()
plt.show()
