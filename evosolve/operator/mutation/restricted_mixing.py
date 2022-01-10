from typing import List, Tuple

import numpy as np
from evobench.benchmark import Benchmark

# from evobench.linkage import DependencyStructureMatrix
from evobench.model import Population, Solution

from ..operator import Operator


class RestrictedMixing(Operator):

    def __init__(self, benchmark: Benchmark):
        super(RestrictedMixing, self).__init__(benchmark)

    # def apply(
    #     self,
    #     population: Population,
    #     dsm: DependencyStructureMatrix
    # ) -> Population:

    def mix(
        self,
        source: Solution,
        ils: List[int], population: Population
    ) -> Tuple[Solution, np.ndarray]:

        assert source.genome.size == self.benchmark.genome_size

        if not source.fitness:
            source.fitness = self.benchmark.evaluate_solution(source)

        trial = Solution(source.genome.copy())
        best_fitness = source.fitness
        mask = np.zeros(self.benchmark.genome_size, dtype=bool)

        for gene_index in ils:
            trial.genome[gene_index] = 1 - trial.genome[gene_index]
            fitness = self.benchmark.evaluate_solution(trial)

            # ! TODO: benchmark min/max
            if fitness >= best_fitness and not population.contains(trial):
                best_fitness = fitness
                mask[gene_index] = True
            else:
                trial.genome[gene_index] = 1 - trial.genome[gene_index]

        trial.fitness = best_fitness
        return trial, mask
