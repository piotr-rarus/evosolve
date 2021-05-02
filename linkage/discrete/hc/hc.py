from abc import ABC, abstractmethod
from typing import List

from evobench import Benchmark
from evobench.model import Solution


class HillClimber(ABC):

    def __init__(self, benchmark: Benchmark):
        self.benchmark = benchmark

    @abstractmethod
    def __call__(self, solution: Solution) -> Solution:
        pass

    def apply(self, solutions: List[Solution]) -> List[Solution]:
        hc_solutions: List[Solution] = []

        for solution in solutions:
            hc_solution = self.__call__(solution)
            hc_solutions.append(hc_solution)

        return hc_solutions
