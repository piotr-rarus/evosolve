from typing import List

import numpy as np
from pytest import fixture

from evosolve.linkage import LinkageScrap


class LinkageHelpers:

    @staticmethod
    def check_empirical_scraps(
        scraps: List[LinkageScrap],
        genome_size: int
    ):
        assert isinstance(scraps, list)
        assert all(isinstance(scrap, LinkageScrap) for scrap in scraps)

        expected_scrap_size = genome_size - 1

        assert all(isinstance(scrap.ranking, np.ndarray) for scrap in scraps)
        assert all(isinstance(scrap.interactions, np.ndarray) for scrap in scraps)
        assert all(scrap.ranking.size == expected_scrap_size for scrap in scraps)
        assert all(scrap.interactions.size == expected_scrap_size for scrap in scraps)


@fixture(scope="session")
def linkage_helpers() -> LinkageHelpers:
    return LinkageHelpers
