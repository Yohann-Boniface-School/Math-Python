# u(34) = 100.00000000000007
# La suite semble converger 100

from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10 ** 8)

"""
@lru_cache est un décorateur permettant l' interaction avec le cache du 
processeur ( cache de niveau 1 ), sous la forme Least Recently Used, 
soit remplacent les valeur les moins utilisé du cache actuel.

Cela permet d' accélérer considérablement la vitesse execution car on 
évite de recalculer chaque terme précédent plus d' une fois au profit
d' une simple demande de mise en cache.

Temps d' exécution sans LRU:

    u(10) => 0.000482500s
    u(20) => 3.200074300s
    u1(25) => 261.418789000s

Temps d' exécution avec LRU:
    ( allocation par défaut de 256 entrées cache )

    u1(10) => 0.000007900s
    u1(100) => 0.000082400s
    u1(1000) => 0.001065000s
"""


@lru_cache
def u(n):
    if n == 1:  # Cas u(1) = 1
        return -4

    if n == 0:  # Cas u(0) = 2
        return 2

    return 111 - (1130 / u(n - 1)) + (3000 / (u(n - 1) * u(n - 2)))


if __name__ == '__main__':
    print(u(450))
