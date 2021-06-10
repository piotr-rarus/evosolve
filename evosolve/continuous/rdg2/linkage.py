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

    gene_idx = list(range(benchmark.genome_size))
    base = [gene_idx[0]]
    target = gene_idx[1:]

    scrap: List[int] = []
    scraps: List[List[int]] = []

    while target:
        scrap = get_scrap(base, target, solution, benchmark)

        if scrap:
            base += scrap
            target = [
                gene_index
                for gene_index in target
                if gene_index not in scrap
            ]

        else:
            scraps.append(base)
            base = [target[0]]

            if len(target) > 1:
                target = target[1:]
            else:
                target = []

    scraps.append(base)

    return None


def get_scrap(
    base: List[int],
    target: List[int],
    solution: Solution,
    benchmark: Benchmark,
) -> Tuple[np.ndarray, np.ndarray]:

    float_eps = sys.float_info.epsilon
    context = (benchmark.lower_bound + benchmark.upper_bound) / 2

    a1 = solution.genome.copy()
    a1[base] = context[base]
    a1 = Solution(a1)

    a2 = solution.genome.copy()
    a2[target] = context[target]
    a2 = Solution(a2)

    a3 = solution.genome.copy()
    a3[base + target] = context[base + target]
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

    if diff > eps:
        if len(target) == 1:
            return target
        else:
            target_middle = len(target) // 2
            target_1 = target[:target_middle]
            target_2 = target[target_middle:]

            scrap1 = get_scrap(base, target_1, solution, benchmark)
            scrap2 = get_scrap(base, target_2, solution, benchmark)

            return scrap1 + scrap2
    else:
        return []


def _gamma(shape: float, scale: float) -> float:
    return (shape * scale) / (1.0 - shape * scale)

    # [1, 2, 3, 4]
    # 1 -> [2, 3, 4]
    # [2] -> [1, 3, 4]

    # _scraps = []
    # _interactions = []

    # for scrap in scraps:

    # for gene_index in range(solution.genome.size):
    #     gene_scrap, gene_interactions = get_scrap(
    #         gene_index, solution, benchmark
    #     )
    #     scraps.append(gene_scrap)
    #     interactions.append(gene_interactions)

    # scraps = np.vstack(scraps)
    # interactions = np.vstack(interactions)
    # return scraps, interactions


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
