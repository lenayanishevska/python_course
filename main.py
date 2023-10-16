def cats_algo(cats: dict, rounds: int) -> list:
    for round_num in range(1, rounds + 1):
        for cat_num in range(round_num, len(cats) + 1, round_num):
            cats[cat_num] = not cats[cat_num]

    cats_with_hat = []
    for key, value in cats.items():
        if value:
            cats_with_hat.append(key)

    return cats_with_hat


while True:
    try:
        rounds = int(input("Enter number of rounds: "))
        number_of_cats = int(input("Enter number of cats: "))
        cats = {i: False for i in range(1, number_of_cats+1)}
        print(f"Cats with hats at the end: {cats_algo(cats, rounds)}")
        break
    except ValueError as e:
        print(f"Error: {e}. Try again, please!")


