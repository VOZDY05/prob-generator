import random

def conditional_probability():
    # Generate random probabilities that make sense
    P_A = round(random.uniform(0.2, 0.9), 2)
    P_B_given_A = round(random.uniform(0.1, 0.9), 2)

    # Compute P(A∩B) = P(B|A) * P(A)
    P_A_and_B = round(P_B_given_A * P_A, 2)

    problem = (
        f"Given:\n"
        f"- P(A) = {P_A}\n"
        f"- P(B | A) = {P_B_given_A}\n\n"
        f"Find P(A ∩ B)."
    )

    steps = (
        f"1. Use the formula: P(A ∩ B) = P(B | A) × P(A)\n\n"
        f"2. Substitute:\n"
        f"P(A ∩ B) = {P_B_given_A} × {P_A}\n\n"
        f"3. Compute:\n"
        f"{P_B_given_A} × {P_A} = {P_A_and_B}"
    )

    answer = f"P(A ∩ B) = {P_A_and_B}"

    return problem, steps, answer
