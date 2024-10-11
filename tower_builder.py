def tower_builder(n_floors):
    tower = []
    for i in range(1, n_floors + 1):
        stars = "*" * (2 * i - 1)
        spaces = " " * (n_floors - i)
        tower.append(f"{spaces}{stars}{spaces}")
    return tower


print(tower_builder(1)) #['*', ]
print(tower_builder(2)) #[' * ', '***']
print(tower_builder(3)) #['  *  ', ' *** ', '*****']

"""
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
"""