import random
def generate_random_queen_positions():
    queens = []
    for _ in range(8):
        queens.append((random.randint(1, 8), random.randint(1, 8)))
    return queens