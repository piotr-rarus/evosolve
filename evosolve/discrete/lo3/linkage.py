from typing import List, Tuple

import numpy as np
from evobench import Solution

from evosolve.discrete.hc.fihc import FIHC


def get_scraps_for_solution(
    solution: Solution,
    fihc: FIHC
) -> Tuple[np.ndarray, np.ndarray]:

    scraps: List[np.ndarray] = []
    interactions: List[np.ndarray] = []

    for gene_index in range(solution.genome.size):
        gene_scrap, gene_interactions = get_scrap(solution, gene_index, fihc)
        scraps.append(gene_scrap)
        interactions.append(gene_interactions)

    scraps = np.vstack(scraps)
    interactions = np.vstack(interactions)
    return scraps, interactions


def get_scraps_for_gene(
    gene_index: int,
    solutions: List[Solution],
    fihc: FIHC
) -> Tuple[np.ndarray, np.ndarray]:
    scraps: List[np.ndarray] = []
    interactions: List[np.ndarray] = []

    for solution in solutions:
        gene_scrap, gene_interactions = get_scrap(solution, gene_index, fihc)
        scraps.append(gene_scrap)
        interactions.append(gene_interactions)

    scraps = np.vstack(scraps)
    interactions = np.vstack(interactions)
    return scraps, interactions


def get_scrap(
    solution: Solution,
    gene_index: int,
    fihc: FIHC
) -> Tuple[np.ndarray, np.ndarray]:

    loci_order = fihc.get_loci_order()
    fihc_solution = fihc(solution, loci_order)

    modified = solution.genome.copy()
    modified[gene_index] = not modified[gene_index]
    modified = Solution(modified)
    fihc_modified = fihc(modified, loci_order)

    interactions = np.abs(fihc_solution.genome - fihc_modified.genome)
    mask = np.ones(fihc.benchmark.genome_size, dtype=bool)
    mask[gene_index] = False
    interactions = interactions[mask]
    scrap = np.argsort(interactions)
    scrap = np.flip(scrap)
    interactions = interactions[scrap]
    scrap[scrap >= gene_index] += 1

    return scrap, interactions
