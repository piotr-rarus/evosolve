import numpy as np
from evobench import Benchmark, Solution
from pytest import fixture

from ..optimal_mixing import OptimalMixing


@fixture(scope="module")
def optimal_mixing(benchmark: Benchmark) -> OptimalMixing:
    return OptimalMixing(benchmark)


def test_apply(optimal_mixing: OptimalMixing, benchmark: Benchmark):
    source = np.array([1, 0, 0, 0, 0, 0])
    donor = np.array([1, 1, 1, 0, 0, 0])
    mask = np.array([True, True, False, False, False, False])

    source = Solution(source)
    donor = Solution(donor)
    source.fitness = benchmark.evaluate_solution(source)
    donor.fitness = benchmark.evaluate_solution(donor)

    offspring = optimal_mixing(source, donor, mask)

    assert isinstance(offspring, Solution)
    assert all(offspring.genome == [1, 1, 0, 0, 0, 0])
