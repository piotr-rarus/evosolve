import numpy as np
from evobench import Benchmark, Population

from ..operator import Operator


class Tournament(Operator):

    def __init__(self, benchmark: Benchmark, pop_size: int, tournament_size: int):
        super(Tournament, self).__init__(benchmark)
        self.POP_SIZE = pop_size
        self.TOURNAMENT_SIZE = tournament_size

    def apply(self, population: Population) -> Population:
        self.benchmark.evaluate_population(population)
        pool = population.solutions
        pool = sorted(pool, key=lambda solution: solution.fitness)

        new_solutions = []
        best_solution = pool[-1]
        new_solutions.append(best_solution)

        pool_idx = np.arange(len(pool))

        while(len(new_solutions) < self.POP_SIZE):
            contestants = self.benchmark.rng.choice(
                pool_idx,
                size=self.TOURNAMENT_SIZE,
                replace=False
            )

            # ! TODO: store info in benchmark whether it's min or max
            max_i = contestants.max()
            best_solution = pool[max_i]
            new_solutions.append(best_solution)

        return Population(new_solutions)
