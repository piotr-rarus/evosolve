from typing import List, Tuple

import numpy as np
from evobench.benchmark import Benchmark
from evobench.model import Solution

from ..operator import Operator


class BackMixing(Operator):

    def __init__(self, benchmark: Benchmark):
        super(BackMixing, self).__init__(benchmark)

    def apply(self, source: Solution, ils: List[int]) -> Tuple[Solution, np.ndarray]:

        assert source.genome.size == self.benchmark.genome_size

        if not source.fitness:
            source.fitness = self.benchmark.evaluate_solution(source)

        modified = Solution(source.genome.copy())
        best_fitness = source.fitness
        mask = np.zeros(self.benchmark.genome_size, dtype=bool)

        for gene_index in ils:
            modified.genome[gene_index] = 1 - modified.genome[gene_index]
            fitness = self.benchmark.evaluate_solution(modified)

            # ! TODO: benchmark min/max
            if fitness >= best_fitness:
                best_fitness = fitness
                mask[gene_index] = True
            else:
                modified.genome[gene_index] = 1 - modified.genome[gene_index]

        modified.fitness = best_fitness
        return modified, mask
