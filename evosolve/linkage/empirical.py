from abc import ABC, abstractmethod
from typing import List

from evobench import Benchmark, Solution

from evosolve.linkage.scrap import LinkageScrap


class BaseEmpiricalLinkage(ABC):

    def __init__(self, benchmark: Benchmark):
        super(BaseEmpiricalLinkage, self).__init__()
        self.benchmark = benchmark

    @abstractmethod
    def get_scrap(self, base: Solution, target_index: int) -> LinkageScrap:
        """
        Extracts empirical linkage scrap for targeted gene and a given solution.

        Parameters
        ----------
        base : Solution
            Base solution for which scrap will be extracted.
        target_index : int
            Denotes the gene which will be perturbed.

        Returns
        -------
        LinkageScrap
            Genes ranking and their interactions.
        """
        pass

    def get_scraps(
        self,
        bases: List[Solution],
        target_index: int
    ) -> List[LinkageScrap]:
        """
        Exracts empirical linkage scraps for targeted gene and a given solutions.

        Parameters
        ----------
        bases : List[Solution]
            Base solutions for which scraps will be extracted.
        target_index : int
            Denotes the gene which will be perturbed.

        Returns
        -------
        List[LinkageScrap]
            Genes ranking and their interactions.
        """

        scraps: List[LinkageScrap] = []

        for base in bases:
            scrap = self.get_scrap(base, target_index)
            scraps.append(scrap)

        return scraps

    def get_all_scraps(self, base: Solution) -> List[LinkageScrap]:
        """
        Extracts empirical linkage scraps for all genes and a given solution.

        Parameters
        ----------
        base : Solution
            Base solution for which scraps will be extracted.

        Returns
        -------
        List[LinkageScrap]
            Genes ranking and their interactions for each of the solution's genes.
        """

        scraps: List[LinkageScrap] = []

        for target_index in range(base.genome.size):
            scrap = self.get_scrap(base, target_index)
            scraps.append(scrap)

        return scraps
