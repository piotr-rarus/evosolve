import itertools
import math
import sys
from typing import List, Tuple

import numpy as np
from evobench import Benchmark, Solution


def get_scraps_for_solution(
    solution: Solution,
    benchmark: Benchmark
) -> Tuple[np.ndarray, np.ndarray]:

    assert hasattr(benchmark, "lower_bound")
    assert hasattr(benchmark, "upper_bound")

    scraps: List[np.ndarray] = []
    interactions: List[np.ndarray] = []

    for gene_index in range(solution.genome.size):
        gene_scrap, gene_interactions = get_scrap(
            gene_index, solution, benchmark
        )
        scraps.append(gene_scrap)
        interactions.append(gene_interactions)

    scraps = np.vstack(scraps)
    interactions = np.vstack(interactions)
    return scraps, interactions


# def get_scraps_for_gene(
#     gene_index: int,
#     solutions: List[Solution],
# ) -> Tuple[np.ndarray, np.ndarray]:

#     scraps: List[np.ndarray] = []
#     interactions: List[np.ndarray] = []

#     for solution in solutions:
#         gene_scrap, gene_interactions = get_scrap(solution, gene_index, fihc)
#         scraps.append(gene_scrap)
#         interactions.append(gene_interactions)

#     scraps = np.vstack(scraps)
#     interactions = np.vstack(interactions)
#     return scraps, interactions


def get_scrap(
    gene_index: int,
    solution: Solution,
    benchmark: Benchmark,
) -> Tuple[np.ndarray, np.ndarray]:

    float_eps = sys.float_info.epsilon
    context = (benchmark.lower_bound + benchmark.upper_bound) / 2
    gene_idx = set(range(benchmark.genome_size))
    gene_idx.remove(gene_index)
    pairs = itertools.product([gene_index], gene_idx)

    mask = np.ones(benchmark.genome_size, dtype=bool)
    mask[gene_index] = False

    interactions = np.zeros(benchmark.genome_size, dtype=bool)

    for base, target in pairs:
        a1 = solution.genome.copy()
        a1[base] = context[base]
        a1 = Solution(a1)

        a2 = solution.genome.copy()
        a2[target] = context[target]
        a2 = Solution(a2)

        a3 = solution.genome.copy()
        a3[[base, target]] = context[[base, target]]
        a3 = Solution(a3)

        # ! TODO: single interface for evaluate?
        a1.fitness = benchmark.evaluate_solution(a1)
        a2.fitness = benchmark.evaluate_solution(a2)
        a3.fitness = benchmark.evaluate_solution(a3)

        d1 = a1.fitness - solution.fitness
        d2 = a3.fitness - a2.fitness

        f_sum = np.array([solution.fitness, a1.fitness, a2.fitness, a3.fitness])
        f_sum = np.abs(f_sum).sum()

        eps = _gamma(float_eps / 2, math.sqrt(benchmark.genome_size) + 2) * f_sum
        diff = abs(d1 - d2)

        interactions[target] = diff > eps

    interactions = interactions[mask]
    scrap = np.argsort(interactions)
    scrap = np.flip(scrap)
    interactions = interactions[scrap]
    scrap[scrap >= gene_index] += 1
    interactions = interactions.astype(float)

    return scrap, interactions


def _gamma(shape: float, scale: float) -> float:
    return (shape * scale) / (1.0 - shape * scale)
