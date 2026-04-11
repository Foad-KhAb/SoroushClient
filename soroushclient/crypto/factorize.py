def _factorize(pq: int):
    import random

    if pq % 2 == 0:
        return 2, pq // 2

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    x = random.randint(2, pq - 1)
    y, c, d = x, random.randint(1, pq - 1), 1
    while d == 1:
        x = (x * x + c) % pq
        y = (y * y + c) % pq
        y = (y * y + c) % pq
        d = gcd(abs(x - y), pq)
    if d != pq:
        p, q = (d, pq // d) if d < pq // d else (pq // d, d)
        return p, q
    raise ValueError("Factorization failed")
