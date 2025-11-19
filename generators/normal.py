import random
from scipy.stats import norm

def normal_distribution():
    mu = random.randint(40, 80)
    sigma = random.randint(5, 15)
    x = random.randint(mu - 20, mu + 20)

    z = round((x - mu) / sigma, 2)
    prob = round(norm.cdf(z), 4)

    problem = (
        f"The height X is normally distributed with:\n"
        f"- mean μ = {mu}\n"
        f"- standard deviation σ = {sigma}\n\n"
        f"Find P(X ≤ {x})."
    )

    steps = (
        f"1. Compute the Z-score:\n"
        f"   Z = (x - μ) / σ = ({x} - {mu}) / {sigma} = {z}\n\n"
        f"2. Use the standard normal table or CDF:\n"
        f"   P(X ≤ {x}) = Φ({z})\n\n"
        f"3. From the normal CDF:\n"
        f"   Φ({z}) = {prob}"
    )

    answer = f"P(X ≤ {x}) = {prob}"

    return problem, steps, answer
