"""
    The Knapsack Problem is a classic optimization problem in computer science and mathematics.
    It gets its name from the concept of a knapsack, which is a container with a limited capacity.
    The problem involves selecting a set of items with maximum value to fit into the knapsack,
    given that each item has a weight and value associated with it.

    The goal of the Knapsack Problem is to determine the optimal selection of items that maximizes
    the total value while ensuring that the total weight of the selected items does not exceed the
    knapsack's capacity.

    The problem is usually formulated in two variations:
        0/1 Knapsack Problem: In this variation, each item can only be selected either entirely (0)
        or not at all (1). In other words, there are no fractional selections of items. The problem
        seeks to find the combination of items that yields the maximum value without exceeding the 
        knapsack's capacity.

        Fractional Knapsack Problem: In this variation, fractional selections of items are allowed.
        It means that an item can be divided into fractions to fit into the knapsack. The problem
        involves determining the fractions of each item to include that maximize the total value
        without surpassing the capacity.

    The Knapsack Problem has numerous practical applications, such as resource allocation, financial
    portfolio optimization, project selection, and scheduling. It is also used as a benchmark for 
    testing algorithms and serves as an example of an NP-hard problem, which means it is computationally
    challenging and has no known polynomial-time algorithm to solve it optimally for all cases.

    To solve the Knapsack Problem, various techniques can be employed, including dynamic programming, 
    greedy algorithms, branch and bound, and heuristics. The choice of approach depends on the problem
    constraints, the size of the problem, and the desired level of optimality.
"""

#it use a dynamic programming
def knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize a 2D table to store the maximum values for different capacities and items
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Traceback to find the items included in the knapsack
    included_items = []
    i = n
    w = capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            included_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    included_items.reverse()
    return dp[n][capacity], included_items


# Example usage:
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
max_value, items = knapsack(weights, values, capacity)
print("Maximum value:", max_value)
print("Included items:", items)
