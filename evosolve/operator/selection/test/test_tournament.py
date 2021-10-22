import numpy as np
from evobench import Benchmark, Population
from pytest import fixture

from ..tournament import Tournament


@fixture(scope="module")
def tournament(benchmark: Benchmark) -> Tournament:
    return Tournament(benchmark, pop_size=10, tournament_size=2)


def test_apply(tournament: Tournament, population: Population):
    new_population = tournament(population)

    assert isinstance(new_population, Population)

    assert len(new_population.solutions) == tournament.POP_SIZE
    assert np.mean(new_population.fitness) > np.mean(population.fitness)
