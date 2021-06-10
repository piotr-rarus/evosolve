from evobench import Population, Solution

from evosolve.conftest import LinkageHelpers

from ..linkage import EmpiricalLinkage


def test_get_scrap(
    empirical_linkage: EmpiricalLinkage,
    solution: Solution,
    linkage_helpers: LinkageHelpers
):
    scrap = empirical_linkage.get_scrap(solution, target_index=0)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps([scrap], genome_size)


def test_get_scraps(
    empirical_linkage: EmpiricalLinkage,
    population: Population,
    linkage_helpers: LinkageHelpers
):
    scraps = empirical_linkage.get_scraps(population.solutions, target_index=0)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps(scraps, genome_size)


def test_get_all_scraps(
    empirical_linkage: EmpiricalLinkage,
    solution: Solution,
    linkage_helpers: LinkageHelpers
):
    scraps = empirical_linkage.get_all_scraps(solution)
    genome_size = empirical_linkage.benchmark.genome_size

    linkage_helpers.check_empirical_scraps(scraps, genome_size)
