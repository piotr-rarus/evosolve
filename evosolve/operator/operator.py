from abc import ABC, abstractmethod
from typing import Tuple, Union

from evobench.benchmark import Benchmark, Population, Solution


class Operator(ABC):

    def __init__(self, benchmark: Benchmark):
        super(Operator, self).__init__()
        self.benchmark = benchmark

    def __call__(self, *args, **kwargs) -> Union[Solution, Tuple[Solution], Population]:
        return self.apply(*args, **kwargs)

    @abstractmethod
    def apply(
        self, *args, **kwargs
    ) -> Union[Solution, Tuple[Solution, ...], Population]:
        pass
