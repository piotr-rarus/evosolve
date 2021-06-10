import numpy as np
from evobench import Solution

from evosolve.discrete.hc.fihc import FIHC
from evosolve.linkage import BaseEmpiricalLinkage, LinkageScrap


class EmpiricalLinkage(BaseEmpiricalLinkage):

    def __init__(self, fihc: FIHC):
        super(EmpiricalLinkage, self).__init__(fihc.benchmark)
        self.fihc = fihc

    def get_scrap(self, base: Solution, target_index: int) -> LinkageScrap:
        loci_order = self.fihc.get_loci_order()
        base_converged = self.fihc(base, loci_order)

        perturbed = base.genome.copy()
        perturbed[target_index] = not perturbed[target_index]
        modified = Solution(perturbed)
        perturbed_converged = self.fihc(modified, loci_order)

        interactions = np.abs(base_converged.genome - perturbed_converged.genome)
        return LinkageScrap(target_index, interactions)
