import numpy as np
from evobench import Benchmark, Solution

from evosolve.linkage import BaseEmpiricalLinkage, LinkageScrap


class EmpiricalLinkage(BaseEmpiricalLinkage):

    def __init__(self, benchmark: Benchmark):
        super(EmpiricalLinkage, self).__init__(benchmark)

    def get_scrap(self, base: Solution, target_index: int) -> LinkageScrap:
        if not base.fitness:
            base.fitness = self.benchmark.evaluate_solution(base)

        perturbed = base.genome.copy()
        perturbed[target_index] = not perturbed[target_index]
        perturbed = Solution(perturbed)
        perturbed.fitness = self.benchmark.evaluate_solution(perturbed)

        base_converged = base.genome.copy()
        perturbed_converged = perturbed.genome.copy()

        for i in range(self.benchmark.genome_size):
            if i == target_index:
                continue

            base_c = base.genome.copy()
            perturbed_c = perturbed.genome.copy()

            base_c[i] = not base_c[i]
            perturbed_c[i] = not perturbed_c[i]

            base_c = Solution(base_c)
            perturbed_c = Solution(perturbed_c)

            base_c.fitness = self.benchmark.evaluate_solution(base_c)
            perturbed_c.fitness = self.benchmark.evaluate_solution(perturbed_c)

            if base_c.fitness > base.fitness:
                base_converged[i] = base_c.genome[i]

            if perturbed_c.fitness > perturbed.fitness:
                perturbed_converged[i] = perturbed_c.genome[i]

        interactions = np.abs(base_converged - perturbed_converged)
        return LinkageScrap(target_index, interactions)
