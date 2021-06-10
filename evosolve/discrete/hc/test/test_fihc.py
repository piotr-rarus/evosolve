import numpy as np
from evobench import Benchmark, Population, Solution
from pytest import fixture

from ..fihc import FIHC


@fixture(scope="module")
def fihc(benchmark: Benchmark) -> FIHC:
    return FIHC(benchmark)


def test_fihc(fihc: FIHC, population: Population):
    next_solutions = fihc.apply(population.solutions)
    next_population = Population(next_solutions)

    assert isinstance(next_solutions, list)
    assert all(isinstance(solution, Solution) for solution in next_solutions)
    assert np.mean(next_population.fitness) > np.mean(population.fitness)

    assert all(
        after.__hash__() != before.__hash__()
        for after, before
        in zip(next_population.solutions, population.solutions)
    )
