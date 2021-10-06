import numpy as np
from evobench import Benchmark, Solution
from pytest import fixture

from ..optimal_mixing import OptimalMixing


@fixture(scope="module")
def optimal_mixing() -> OptimalMixing:
    return OptimalMixing()


def test_cross(optimal_mixing: OptimalMixing, benchmark: Benchmark):
    source = np.array([1, 0, 0, 0, 0])
    donor = np.array([1, 1, 1, 0, 0])
    mask = np.array([True, True, False, False, False])

    source = Solution(source)
    donor = Solution(donor)
    source.fitness = benchmark.evaluate_solution(source)
    donor.fitness = benchmark.evaluate_solution(donor)

    offspring = optimal_mixing.cross(source, donor, mask, benchmark)

    assert isinstance(offspring, Solution)
    assert all(offspring.genome == [1, 1, 0, 0, 0])
