import numpy as np


class Topsis:
    def __init__(self, dataset, weight, criterion_type):
        self.dataset = dataset
        self.weight = weight
        self.criterion_type = criterion_type
        self.total_alternative = len(dataset)
        self.total_criteria = len(dataset[0])
        self.matrix = []

    def exec(self):
        self.matrix = self.float_dataset()
        normalize_matrix = self.normalize()
        weighted_matrix = self.weight_product(normalize_matrix)
        ideal_worst, ideal_best = self.calc_ideal_best_worst(matrix=weighted_matrix)
        distance_worst, distance_best = self.euclidean_distance(weighted_matrix, ideal_worst, ideal_best)
        score = self.performance_score(distance_best, distance_worst)
        ranks = np.argsort(np.argsort(-score)) + 1

        return score, ranks

    def float_dataset(self):
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

    def normalize(self):
        raw = np.empty(shape=(self.total_alternative, self.total_criteria), dtype=np.float64)

        for j in range(self.total_criteria):
            sq = np.sqrt(sum(self.matrix[:, j] ** 2))
            for i in range(self.total_alternative):
                raw[i, j] = self.matrix[i, j] / sq

        return raw

    def weight_product(self, matrix):
        return matrix * self.weight

    def calc_ideal_best_worst(self, matrix):
        ideal_worst = []
        ideal_best = []
        for i in range(self.total_criteria):
            if self.criterion_type[i] == 1:
                ideal_worst.append(min(matrix[:, i]))
                ideal_best.append(max(matrix[:, i]))
            else:
                ideal_worst.append(max(matrix[:, i]))
                ideal_best.append(min(matrix[:, i]))
        return ideal_worst, ideal_best

    def euclidean_distance(self, matrix, ideal_worst, ideal_best):
        diw = (matrix - ideal_worst) ** 2
        dib = (matrix - ideal_best) ** 2
        distance_worst = []
        distance_best = []
        for i in range(self.total_alternative):
            distance_worst.append(sum(diw[i, :]) ** 0.5)
            distance_best.append(sum(dib[i, :]) ** 0.5)
        distance_worst = np.array(distance_worst)
        distance_best = np.array(distance_best)
        return distance_worst, distance_best

    def performance_score(self, distance_best, distance_worst):
        score = []
        score = distance_worst / (distance_best + distance_worst)
        return score
