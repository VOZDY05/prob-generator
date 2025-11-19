import random
from math import comb

def binomial_distribution():
    # n trials, probability p, find P(X = k)
    n = random.randint(5, 20)
    p = round(random.uniform(0.2, 0.8), 2)
    k = random.randint(0, n)

    # compute probability
    prob = round(comb(n, k) * (p ** k) * ((1 - p) ** (n - k)), 4)

    problem = (
        f"Let X ~ Binomial(n={n}, p={p}).\n"
        f"Find P(X = {k})."
    )

    steps = (
        f"1. Use the binomial formula:\n"
        f"   P(X = k) = C(n, k) · p^k · (1 - p)^(n - k)\n\n"
        f"2. Substitute values:\n"
        f"   P(X = {k}) = C({n}, {k}) · {p}^{k} · (1 - {p})^({n - k})\n\n"
        f"3. Compute C({n}, {k}) and plug in:\n"
        f"   P(X = {k}) = {prob}"
    )

    answer = f"P(X = {k}) = {prob}"

    return problem, steps, answer
