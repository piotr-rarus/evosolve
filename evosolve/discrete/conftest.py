from evobench import Benchmark, Population, Solution
from evobench.discrete import Trap
from pytest import fixture


@fixture(scope="module")
def benchmark() -> Benchmark:
    return Trap(blocks=[4] * 3)


@fixture(scope="module")
def population(benchmark: Benchmark) -> Population:
    population = benchmark.initialize_population(10)
    benchmark.evaluate_population(population)
    return population


@fixture(scope="module")
def solution(population: Population) -> Solution:
    return population.solutions[0]
