from evobench import Benchmark, Population, Solution
from pytest import fixture

from evosolve.conftest import LinkageHelpers

from ..empirical_random import RandomEmpiricalLinkage


@fixture(scope="module")
def empirical_linkage(benchmark: Benchmark) -> RandomEmpiricalLinkage:
    return RandomEmpiricalLinkage(benchmark)


def test_get_scrap(
    empirical_linkage: RandomEmpiricalLinkage,
    solution: Solution,
    linkage_helpers: LinkageHelpers
):
    scrap = empirical_linkage.get_scrap(solution, target_index=0)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps([scrap], genome_size)


def test_get_scraps(
    empirical_linkage: RandomEmpiricalLinkage,
    population: Population,
    linkage_helpers: LinkageHelpers
):
    scraps = empirical_linkage.get_scraps(population.solutions, target_index=0)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps(scraps, genome_size)


def test_get_all_scraps(
    empirical_linkage: RandomEmpiricalLinkage,
    solution: Solution,
    linkage_helpers: LinkageHelpers
):
    scraps = empirical_linkage.get_all_scraps(solution)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps(scraps, genome_size)
