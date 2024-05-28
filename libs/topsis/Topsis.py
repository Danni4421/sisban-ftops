from typing import Any
import numpy as np


class Topsis:
    dataset: list[list[int]]
    weight: list[float]
    criterion_type: list[int]
    total_alternative: int
    total_criteria: int
    matrix: np.ndarray[Any, np.dtype] = []
    score: list

    def __init__(self, dataset, weight, criterion_type) -> None:
        self.dataset = dataset
        self.weight = weight
        self.criterion_type = criterion_type
        self.total_alternative = len(dataset)
        self.total_criteria = len(dataset[0])

    def exec(self) -> (list, list):
        # Initialize the matrix that will be used in this method
        self.matrix = self.float_dataset()

        # Start to normalize the dataset and store to the matrix
        self.normalize()

        # After normalize, then weighting all the dataset for each criterion
        self.weighting_product()

        # Getting the ideal best and worst for each criterion
        res_ideal_worst, res_ideal_best = self.calc_ideal_best_worst()

        # Result from calculating ideal best and worst,then use for calculate Euclidean Distance
        distance_worst, distance_best = self.euclidean_distance(
            ideal_worst=res_ideal_worst,
            ideal_best=res_ideal_best
        )

        # After calculating the Euclidean distance, The final step is calculating score for each
        # alternative from distance that we are got it before
        self.performance_score(distance_best, distance_worst)

        # Getting the rank from final score
        ranks = np.argsort(np.argsort(-self.score)) + 1

        return self.score, ranks

    def float_dataset(self) -> np.ndarray[Any, np.dtype]:
        b = []

        for i in self.dataset:
            try:
                ix = []
                for j in i:
                    ix.append(float(j))
            except:
                ix = float(i)
                pass
            b.append(ix)

        b = np.array(b)

        return b

    def normalize(self) -> None:
        for j in range(self.total_criteria):
            sq = np.sqrt(sum(self.matrix[:, j] ** 2))
            sq = 1 if sq == 0 else sq

            for i in range(self.total_alternative):
                self.matrix[i, j] = self.matrix[i, j] / sq

    def weighting_product(self) -> None:
        self.matrix = self.matrix * self.weight

    def calc_ideal_best_worst(self):
        ideal_worst = []
        ideal_best = []

        for i in range(self.total_criteria):
            if self.criterion_type[i] == 1:
                ideal_worst.append(min(self.matrix[:, i]))
                ideal_best.append(max(self.matrix[:, i]))
            else:
                ideal_worst.append(max(self.matrix[:, i]))
                ideal_best.append(min(self.matrix[:, i]))

        return ideal_worst, ideal_best

    def euclidean_distance(self, ideal_worst, ideal_best):
        diw = (self.matrix - ideal_worst) ** 2
        dib = (self.matrix - ideal_best) ** 2

        distance_worst = []
        distance_best = []

        for i in range(self.total_alternative):
            distance_worst.append(sum(diw[i, :]) ** 0.5)
            distance_best.append(sum(dib[i, :]) ** 0.5)

        distance_worst = np.array(distance_worst)
        distance_best = np.array(distance_best)

        return distance_worst, distance_best

    def performance_score(self, distance_best, distance_worst):
        self.score = distance_worst / (distance_best + distance_worst)
