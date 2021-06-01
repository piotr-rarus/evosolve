from evobench import Benchmark, Population
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