def is_prime(user_input: int) -> bool:
    for i in range(0, user_input):
        if user_input == 0 or user_input == 1 or user_input % i == 0:
            return False
        return True


x = int(input())
y = is_prime(x)


