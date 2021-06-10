from evobench import Benchmark, Population, Solution
from evobench.continuous import Multimodal
from pytest import fixture


@fixture(scope="module")
def benchmark() -> Benchmark:
    return Multimodal(blocks=[4] * 3, overlap_size=1)


@fixture(scope="module")
def population(benchmark: Benchmark) -> Population:
    population = benchmark.initialize_population(10)
    benchmark.evaluate_population(population)
    return population


@fixture(scope="module")
def solution(population: Population) -> Solution:
    return population.solutions[0]
