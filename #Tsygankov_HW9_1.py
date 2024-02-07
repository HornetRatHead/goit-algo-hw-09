#Tsygankov_HW9_1
import timeit

def find_coins_greedy(amounts):
    coins = [50, 25, 10, 5, 2, 1]
    results = []
    for amount in amounts:
        result = {}
        print(f"Amount: {amount}")
        print("Greedy algorithm:")
        print("Coins used:")
        for coin in coins:
            count = amount // coin
            if count > 0:
                result[coin] = count
                amount -= count * coin
                print(f"{coin}: {count}")
        print(f"Total coins: {sum(result.values())}")
        print(f"Result: {result}\n")
        results.append(result)
    return results

def find_min_coins(amounts):
    coins = [50, 25, 10, 5, 2, 1]
    results = []
    for amount in amounts:
        dp = [0] + [float('inf')] * amount
        result = {}
        print(f"Amount: {amount}")
        print("Dynamic programming algorithm:")
        print("Coins used:")
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        for coin in coins:
            count = amount // coin
            if count > 0:
                result[coin] = count
                amount -= count * coin
                print(f"{coin}: {count}")
        print(f"Total coins: {sum(result.values())}")
        print(f"Result: {result}\n")
        results.append(result)
    return results

if __name__ == "__main__":
    # Test input amounts
    amounts = [101, 257, 649, 9091, 9871]
    
    # Time the execution of find_coins_greedy function
    greedy_time = timeit.timeit("find_coins_greedy(amounts)", globals=globals(), number=1)
    print(f"Greedy algorithm execution time: {greedy_time} seconds\n")

    # Time the execution of find_min_coins function
    dp_time = timeit.timeit("find_min_coins(amounts)", globals=globals(), number=1)
    print(f"Dynamic programming algorithm execution time: {dp_time} seconds\n")


