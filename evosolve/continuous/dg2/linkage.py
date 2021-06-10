import itertools
import math
from sys import float_info

import numpy as np
from evobench import Benchmark, Solution

from evosolve.linkage import BaseEmpiricalLinkage, LinkageScrap


class EmpiricalLinkage(BaseEmpiricalLinkage):

    def __init__(self, benchmark: Benchmark):
        assert hasattr(benchmark, "lower_bound")
        assert hasattr(benchmark, "upper_bound")

        super(EmpiricalLinkage, self).__init__(benchmark)

    def get_scrap(self, base: Solution, target_index: int) -> LinkageScrap:
        if not base.fitness:
            base.fitness = self.benchmark.evaluate_solution(base)

        float_eps = float_info.epsilon

        context = (self.benchmark.lower_bound + self.benchmark.upper_bound) / 2
        gene_idx = set(range(self.benchmark.genome_size))
        gene_idx.remove(self.gene_index)
        pairs = itertools.product([target_index], gene_idx)

        interactions = np.zeros(self.benchmark.genome_size, dtype=bool)

        for p1, p2 in pairs:
            s1 = base.genome.copy()
            s1[p1] = context[p1]
            s1 = Solution(s1)

            s2 = base.genome.copy()
            s2[p2] = context[p2]
            s2 = Solution(s2)

            s3 = base.genome.copy()
            s3[[p1, p2]] = context[[p1, p2]]
            s3 = Solution(s3)

            s1.fitness = self.benchmark.evaluate_solution(s1)
            s2.fitness = self.benchmark.evaluate_solution(s2)
            s3.fitness = self.benchmark.evaluate_solution(s3)

            d1 = s1.fitness - base.fitness
            d2 = s3.fitness - s2.fitness

            f_sum = np.array([base.fitness, s1.fitness, s2.fitness, s3.fitness])
            f_sum = np.abs(f_sum).sum()

            eps = self._gamma(float_eps / 2, math.sqrt(self.benchmark.genome_size) + 2)
            eps *= f_sum
            diff = abs(d1 - d2)

            interactions[target_index] = diff > eps

        return LinkageScrap(target_index, interactions)

    def _gamma(self, shape: float, scale: float) -> float:
        return (shape * scale) / (1.0 - shape * scale)
