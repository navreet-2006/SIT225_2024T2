import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "navreet.csv"  # Change this to your actual file path
df = pd.read_csv(file_path)

# Convert Timestamp to datetime format
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Plot the data
plt.figure(figsize=(12, 6))
plt.plot(df["Timestamp"], df["X"], label="X-axis", marker='o', linestyle='-')
plt.plot(df["Timestamp"], df["Y"], label="Y-axis", marker='s', linestyle='--')
plt.plot(df["Timestamp"], df["Z"], label="Z-axis", marker='^', linestyle='-.')

plt.xlabel("Time")
plt.ylabel("Sensor Readings")
plt.title("Sensor Data Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()
