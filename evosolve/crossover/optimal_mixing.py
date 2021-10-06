# from typing import Tuple

import numpy as np
from evobench.benchmark import Benchmark
from evobench.model import Solution

from .crossover import Crossover


class OptimalMixing(Crossover):

    def __init__(self):
        super(Crossover, self).__init__()

    def cross(
        self,
        source: Solution, donor: Solution,
        mask: np.ndarray,
        benchmark: Benchmark
    ) -> Solution:

        assert source.genome.size == donor.genome.size \
            == mask.size == benchmark.genome_size
        assert mask.dtype == bool

        offspring = source.genome.copy()
        offspring[mask] = donor.genome[mask]

        offspring = Solution(offspring)
        offspring.fitness = benchmark.evaluate_solution(offspring)

        return offspring if offspring.fitness >= source.fitness else source
