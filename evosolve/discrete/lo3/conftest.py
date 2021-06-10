from evobench import Benchmark
from pytest import fixture

from evosolve.discrete.hc import FIHC

from .linkage import EmpiricalLinkage


@fixture(scope="module")
def fihc(benchmark: Benchmark) -> FIHC:
    return FIHC(benchmark)


@fixture(scope="module")
def empirical_linkage(fihc: FIHC) -> EmpiricalLinkage:
    return EmpiricalLinkage(fihc)
