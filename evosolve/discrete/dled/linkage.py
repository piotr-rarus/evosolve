from typing import List, Tuple

import numpy as np
from evobench import Benchmark, Solution


def get_scraps_for_solution(
    solution: Solution,
    benchmark: Benchmark
) -> Tuple[np.ndarray, np.ndarray]:

    scraps: List[np.ndarray] = []
    interactions: List[np.ndarray] = []

    for gene_index in range(solution.genome.size):
        gene_scrap, gene_interactions = get_scrap(solution, gene_index, benchmark)
        scraps.append(gene_scrap)
        interactions.append(gene_interactions)

    scraps = np.vstack(scraps)
    interactions = np.vstack(interactions)
    return scraps, interactions


def get_scraps_for_gene(
    gene_index: int,
    solutions: List[Solution],
) -> Tuple[np.ndarray, np.ndarray]:
    scraps: List[np.ndarray] = []
    interactions: List[np.ndarray] = []

    for solution in solutions:
        gene_scrap, gene_interactions = get_scrap(solution, gene_index)
        scraps.append(gene_scrap)
        interactions.append(gene_interactions)

    scraps = np.vstack(scraps)
    interactions = np.vstack(interactions)
    return scraps, interactions


def get_scrap(
    base: Solution,
    gene_index: int,
    benchmark: Benchmark
) -> Tuple[np.ndarray, np.ndarray]:

    perturbed = base.genome.copy()
    perturbed[gene_index] = not perturbed[gene_index]
    perturbed = Solution(perturbed)
    perturbed.fitness = benchmark.evaluate_solution(perturbed)

    base_converged = base.genome.copy()
    perturbed_converged = perturbed.genome.copy()

    for i in range(benchmark.genome_size):
        if i == gene_index:
            continue

        base_c = base.genome.copy()
        perturbed_c = perturbed.genome.copy()

        base_c[i] = not base_c[i]
        perturbed_c[i] = not perturbed_c[i]

        base_c = Solution(base_c)
        perturbed_c = Solution(perturbed_c)

        base_c.fitness = benchmark.evaluate_solution(base_c)
        perturbed_c.fitness = benchmark.evaluate_solution(perturbed_c)

        if base_c.fitness > base.fitness:
            base_converged[i] = base_c.genome[i]

        if perturbed_c.fitness > perturbed.fitness:
            perturbed_converged[i] = perturbed_c.genome[i]

    interactions = np.abs(base_converged - perturbed_converged)
    mask = np.ones(benchmark.genome_size, dtype=bool)
    mask[gene_index] = False
    interactions = interactions[mask]
    scrap = np.argsort(interactions)
    scrap = np.flip(scrap)
    interactions = interactions[scrap]
    scrap[scrap >= gene_index] += 1

    return scrap, interactions
