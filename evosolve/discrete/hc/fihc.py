import numpy as np
from evobench import Benchmark
from evobench.model import Solution

from .hc import HillClimber


class FIHC(HillClimber):

    def __init__(self, benchmark: Benchmark):
        super().__init__(benchmark)

    def __call__(self, solution: Solution, loci_order: np.ndarray = None) -> Solution:
        assert loci_order.size == self.benchmark.genome_size
        assert solution.genome.size == self.benchmark.genome_size

        if not solution.fitness:
            solution.fitness = self.benchmark.evaluate_solution(solution)

        loci = solution.genome.copy()

        if loci_order is None:
            loci_order = self.get_loci_order()

        improved_score = solution.fitness
        loci_improved = True

        while loci_improved:

            loci_improved = False

            for index in loci_order:
                loci[index] = not loci[index]
                loci_solution = Solution(loci)
                loci_score = self.benchmark.evaluate_solution(loci_solution)

                if loci_score > improved_score:
                    improved_score = loci_score
                    loci_improved = True
                else:
                    loci[index] = not loci[index]

        return Solution(loci, improved_score)

    def get_loci_order(self) -> np.ndarray:
        loci_order = np.arange(start=0, stop=self.benchmark.genome_size)
        self.benchmark.random_state.shuffle(loci_order)
        return loci_order
