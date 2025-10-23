import timeit
import pandas as pd
import matplotlib.pyplot as plt

# Define test sizes (number of elements in the list)
sizes = [100, 1000, 10000, 20000, 30000, 100000, 200000, 300000]

results = []

for n in sizes:
    data = list(range(n))

    # Test 1: Regular for loop
    t1 = timeit.timeit(lambda: [x * 2 for x in data], number=100)

    # Test 2: Enumerate for loop
    t2 = timeit.timeit(lambda: [i * 2 for i, x in enumerate(data)], number=100)

    # Test 3: Range(len())
    t3 = timeit.timeit(lambda: [data[i] * 2 for i in range(len(data))], number=100)

    results.append((n, t1, t2, t3))

df = pd.DataFrame(results, columns=["N", "Regular for", "Enumerate", "Range(len)"])

# Display DataFrame
print(df)

# Plot performance comparison
plt.figure(figsize=(8, 5))
plt.plot(df["N"], df["Regular for"], label="Regular for")
plt.plot(df["N"], df["Enumerate"], label="Enumerate")
plt.plot(df["N"], df["Range(len)"], label="Range(len)")
plt.xlabel("Number of items")
plt.ylabel("Execution time (seconds, lower is better)")
plt.title("Performance comparison: for vs enumerate vs range(len)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
