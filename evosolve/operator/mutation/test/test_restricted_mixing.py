import numpy as np
from evobench import Benchmark, Solution
from pytest import fixture

from ..restricted_mixing import RestrictedMixing


@fixture(scope="module")
def restricted_mixing(benchmark: Benchmark) -> RestrictedMixing:
    return RestrictedMixing(benchmark)


def test_cross(restricted_mixing: RestrictedMixing):
    source = Solution(np.array([1, 0, 0, 0, 0, 0]))
    ils = [1, 5, 2]

    offspring, mask = restricted_mixing(source, ils)

    assert isinstance(offspring, Solution)
    assert offspring.fitness > source.fitness

    assert isinstance(mask, np.ndarray)
    assert mask.dtype == bool
    assert mask.size == restricted_mixing.benchmark.genome_size
