import random
import time

# -----------------------------
# Randomized Quickselect
# -----------------------------
def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))


# -----------------------------
# Deterministic (Median of Medians)
# -----------------------------
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Step 1: divide into groups of 5
    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(group)[len(group)//2] for group in groups]

    # Step 2: find pivot (median of medians)
    pivot = deterministic_select(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))


# -----------------------------
# TEST
# -----------------------------

def run_tests():
    sizes = [100, 1000, 5000]

    for n in sizes:
        arr = [random.randint(1, 10000) for _ in range(n)]
        k = n // 2

        # Randomized
        start = time.time()
        randomized_select(arr, k)
        end = time.time()
        print(f"Randomized (n={n}): {end - start:.6f} sec")

        # Deterministic
        start = time.time()
        deterministic_select(arr, k)
        end = time.time()
        print(f"Deterministic (n={n}): {end - start:.6f} sec")

        print("-" * 40)


if __name__ == "__main__":
    run_tests()