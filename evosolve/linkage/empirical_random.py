from evobench import Benchmark, Solution

from evosolve.linkage import BaseEmpiricalLinkage, LinkageScrap


class RandomEmpiricalLinkage(BaseEmpiricalLinkage):
    """
    """

    def __init__(self, benchmark: Benchmark):
        super(RandomEmpiricalLinkage, self).__init__(benchmark)

    def get_scrap(self, base: Solution, target_index: int) -> LinkageScrap:

        assert base.genome.size == self.benchmark.genome_size

        interactions = self.benchmark.rng.uniform(
            size=self.benchmark.genome_size
        )

        return LinkageScrap(target_index, interactions)
