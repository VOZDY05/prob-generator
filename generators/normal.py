import random
import math


def normal_distribution():
    mu = random.randint(40, 80)
    sigma = random.randint(5, 15)
    x = random.randint(mu - 20, mu + 20)

    # Z-score
    z = round((x - mu) / sigma, 2)

    # Normal CDF using error function (no scipy needed)
    # Φ(z) = 0.5 * (1 + erf(z / sqrt(2)))
    prob = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    prob = round(prob, 4)

    problem = (
        f"The variable X is normally distributed with:\n"
        f"- mean μ = {mu}\n"
        f"- standard deviation σ = {sigma}\n\n"
        f"Find P(X ≤ {x})."
    )

    steps = (
        f"1. Compute the Z-score:\n"
        f"   Z = (x - μ) / σ = ({x} - {mu}) / {sigma} = {z}\n\n"
        f"2. Use the standard normal CDF approximation:\n"
        f"   P(X ≤ {x}) = Φ({z}) ≈ 0.5 * (1 + erf({z} / √2))\n\n"
        f"3. Compute the value:\n"
        f"   Φ({z}) ≈ {prob}"
    )

    answer = f"P(X ≤ {x}) ≈ {prob}"

    return problem, steps, answer
