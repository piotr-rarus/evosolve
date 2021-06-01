import numpy as np
from evobench import Benchmark, Population
from pytest import fixture

from evosolve.discrete.hc.fihc import FIHC
from evosolve.discrete.lo3.linkage import get_scraps_for_solution


@fixture(scope="module")
def fihc(benchmark: Benchmark) -> FIHC:
    return FIHC(benchmark)


def test_scraps(fihc: FIHC, population: Population):
    solution = population.solutions[0]
    scraps, interactions = get_scraps_for_solution(solution, fihc)

    genome_size = fihc.benchmark.genome_size

    assert isinstance(scraps, np.ndarray)
    assert isinstance(interactions, np.ndarray)
    assert scraps.shape == (genome_size, genome_size - 1)
    assert interactions.shape == (genome_size, genome_size - 1)
