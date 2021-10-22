import numpy as np
from evobench.benchmark import Benchmark
from evobench.model import Solution

from ..operator import Operator


class OptimalMixing(Operator):

    def __init__(self, benchmark: Benchmark):
        super(OptimalMixing, self).__init__(benchmark)

    def apply(self, source: Solution, donor: Solution, mask: np.ndarray) -> Solution:

        assert source.genome.size == donor.genome.size \
            == mask.size == self.benchmark.genome_size
        assert mask.dtype == bool

        offspring = source.genome.copy()
        offspring[mask] = donor.genome[mask]

        offspring = Solution(offspring)
        offspring.fitness = self.benchmark.evaluate_solution(offspring)

        return offspring if offspring.fitness >= source.fitness else source
