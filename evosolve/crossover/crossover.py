from abc import ABC, abstractmethod
from typing import Tuple

# from evobench.benchmark import Benchmark
from evobench.model import Solution


class Crossover(ABC):

    def __init__(self):
        super(Crossover, self).__init__()

    @abstractmethod
    def cross(
        self,
        p1: Solution, p2: Solution,
        # benchmark: Benchmark
    ) -> Tuple[Solution, Solution]:
        pass
