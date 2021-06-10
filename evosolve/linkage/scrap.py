import numpy as np


class LinkageScrap:

    """
    Parameters
    ----------
    target_index : int
        Base index. Scrap denotes interactions targeted at that gene.
    ranking : np.ndarray[genome_size - 1]
        Genes ranking.
    interactions : np.ndarray
        Specific interaction values of each particular gene from the ranking.
    """

    def __init__(self, target_index: int, interactions: np.ndarray):
        """
        Parameters
        ----------
        target_index : int
            Base index. Scrap denotes interactions targeted at that gene.
        interactions : np.ndarray[genome_size]
            Specific interaction values of each particular gene in the benchmark.
        """

        mask = np.ones(interactions.size, dtype=bool)
        mask[target_index] = False
        interactions = interactions[mask]

        ranking = np.argsort(interactions)
        ranking = np.flip(ranking)
        interactions = interactions[ranking]
        ranking[ranking >= target_index] += 1

        self.target_index = target_index
        self.ranking = ranking
        self.interactions = interactions
