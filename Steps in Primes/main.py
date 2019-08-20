import numpy as np


def generate_primes(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*2::i]=False
    return np.where(is_prime)[0]


def get_prime_in_interval(start, end):
    primes = generate_primes(end)
    for prime in primes:
        if prime >= start:
            yield prime


def step(g, m, n):
    print('g, m, n: {}, {}, {}'.format(g, m, n))
    primes_gen = get_prime_in_interval(m, n)

    primes = []
    while True:
        try:
            primes.append(next(primes_gen))
        except:
            break

    for i, first in enumerate(primes):
        for second in primes[i:]:
            if second - first == g:
                return [first, second]

    return None


if __name__ == "__main__":
    assert step(2,100,110) == [101, 103]
    assert step(4,100,110) == [103, 107]
    assert step(2,5,5) is None
    assert step(6,100,110) == [101, 107]
    assert step(8,300,400) == [359, 367]
    assert step(10,300,400) == [307, 317]
