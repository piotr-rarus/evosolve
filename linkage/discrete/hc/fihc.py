from copy import deepcopy

import numpy as np
from evobench import Benchmark
from evobench.model import Solution

from .hc import HillClimber


class FIHC(HillClimber):

    def __init__(self, benchmark: Benchmark):
        super().__init__(benchmark)

    def __call__(self, solution: Solution) -> Solution:
        solution = deepcopy(solution)
        loci = solution.genome
        loci_order = np.arange(start=0, stop=loci.size)
        self.benchmark.random_state.shuffle(loci_order)

        improved_score = self.benchmark.evaluate_solution(solution)
        loci_improved = True

        while loci_improved:

            loci_improved = False

            for index in loci_order:
                loci[index] = not loci[index]
                loci_score = self.benchmark.evaluate_solution(solution)

                if loci_score > improved_score:
                    improved_score = loci_score
                    loci_improved = True
                else:
                    loci[index] = not loci[index]

        return Solution(loci, improved_score)
