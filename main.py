def prime_or_comp(user_input: int) -> str:
    if user_input == 0 or user_input == 1:
        return "neither prime nor composite"

    if user_input == 2:
        return "prime"

    else:
        for i in range(2, user_input):
            if user_input % i == 0:
                return "composite"
        return "prime"


x = int(input())
y = prime_or_comp(x)


