import logging
import time
from functools import lru_cache

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s",
)
logger = logging.getLogger(__name__)

# To jest funkcja rekurencyjna obliczająca n-ty wyraz ciągu Fibonacciego.
# Dla n=5 zwróci 5, ponieważ ciąg zaczyna się od 0, 1, 1, 2, 3, 5...
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        logger.debug("fib %s", n)
        return fib(n - 1) + fib(n - 2)

# Funkcja z memoizacją: czyste ponowne obliczanie jest unikane.
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

@lru_cache(maxsize=None)
def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        logger.debug("fibo %s", n)
        return fibo(n - 1) + fibo(n - 2)


def measure(func, n):
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    elapsed = end - start
    logger.info("%s(%s) = %s, czas: %.6f s", func.__name__, n, result, elapsed)
    return elapsed


if __name__ == "__main__":
    n = 5
    logger.info("Porównanie czasów dla n=%s", n)

    # Wartość n=30 dla fib() i fibo() może już być widocznie wolna, ale to dobrze pokazuje różnicę.
    measure(fib, n)
    measure(fibo, n)
    measure(fib_memo, n)

