from evobench import Benchmark
from pytest import fixture

from .linkage import EmpiricalLinkage


@fixture(scope="module")
def empirical_linkage(benchmark: Benchmark) -> EmpiricalLinkage:
    return EmpiricalLinkage(benchmark)
