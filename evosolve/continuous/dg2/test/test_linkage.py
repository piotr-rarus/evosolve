import numpy as np
from evobench import Benchmark, Population

from evosolve.continuous.dg2.linkage import get_scraps_for_solution


def test_scraps(benchmark: Benchmark, population: Population):
    solution = population.solutions[0]
    scraps, interactions = get_scraps_for_solution(solution, benchmark)

    genome_size = benchmark.genome_size

    assert isinstance(scraps, np.ndarray)
    assert isinstance(interactions, np.ndarray)
    assert scraps.shape == (genome_size, genome_size - 1)
    assert interactions.shape == (genome_size, genome_size - 1)
