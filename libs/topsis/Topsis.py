from typing import Any
from app.database import db
from app.models import Topsis as TopsisModel, TopsisNormalization, TopsisWeighting, TopsisBestWorst, TopsisEuclideanDistance
import numpy as np


class Topsis:
    alternatives: list
    key: int
    dataset: list[list[int]]
    weight: list[float]
    criterion_type: list[int]
    normalized_matrix: np.ndarray[Any, np.dtype]
    weighted_matrix: np.ndarray[Any, np.dtype]
    ideal_best: list
    ideal_worst: list
    distance_best: list
    distance_worst: list
    total_alternative: int
    total_criteria: int
    score: list
    ranks: list

    def __init__(self, alternatives, key, dataset, weight, criterion_type) -> None:
        self.alternatives = alternatives
        self.key = key
        self.dataset = dataset
        self.weight = weight
        self.criterion_type = criterion_type
        self.total_alternative = len(dataset)
        self.total_criteria = len(dataset[0])

    def exec(self):       
        # Initialize the matrix that will be used in this method
        matrix = self.float_dataset()

        # Start to normalize the dataset and store to the matrix
        self.normalize(matrix)

        # After normalize, then weighting all the dataset for each criterion
        self.weighting_product()

        # Getting the ideal best and worst for each criterion
        self.ideal_worst, self.ideal_best = self.calc_ideal_best_worst()

        # Result from calculating ideal best and worst,then use for calculate Euclidean Distance
        self.distance_worst, self.distance_best = self.euclidean_distance()

        # After calculating the Euclidean distance, The final step is calculating score for each
        # alternative from distance that we are got it before
        self.performance_score()

        # Getting the rank from final score
        self.ranks = np.argsort(np.argsort(-self.score)) + 1

        self.store_into_db()

        return self.score, self.ranks

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

    def normalize(self, matrix) -> None:
        self.normalized_matrix = np.empty((self.total_alternative, self.total_criteria), np.float64)

        for j in range(self.total_criteria):
            sq = np.sqrt(sum(matrix[:, j] ** 2))
            sq = 1 if sq == 0 else sq

            for i in range(self.total_alternative):
                self.normalized_matrix[i, j] = matrix[i, j] / sq

    def weighting_product(self) -> None:
        self.weighted_matrix = self.normalized_matrix * self.weight

    def calc_ideal_best_worst(self):
        ideal_worst = []
        ideal_best = []

        for i in range(self.total_criteria):
            if self.criterion_type[i] == 1:
                ideal_worst.append(min(self.weighted_matrix[:, i]))
                ideal_best.append(max(self.weighted_matrix[:, i]))
            else:
                ideal_worst.append(max(self.weighted_matrix[:, i]))
                ideal_best.append(min(self.weighted_matrix[:, i]))

        return ideal_worst, ideal_best

    def euclidean_distance(self):
        diw = (self.weighted_matrix - self.ideal_worst) ** 2
        dib = (self.weighted_matrix - self.ideal_best) ** 2

        distance_worst = []
        distance_best = []

        for i in range(self.total_alternative):
            distance_worst.append(sum(diw[i, :]) ** 0.5)
            distance_best.append(sum(dib[i, :]) ** 0.5)

        distance_worst = np.array(distance_worst)
        distance_best = np.array(distance_best)

        return distance_worst, distance_best

    def performance_score(self):
        self.score = self.distance_worst / (self.distance_best + self.distance_worst)

    def store_into_db(self):
        for i in range(len(self.alternatives)):
            alternative_id = self.alternatives[i]
            
            # Query untuk mencari entri existing
            topsis_in_db = TopsisModel.query.filter_by(alternative=alternative_id, bansos=self.key).first()
            normalize_alternative = TopsisNormalization.query.filter_by(alternative=alternative_id, bansos=self.key).first()
            weight_alternative = TopsisWeighting.query.filter_by(alternative=alternative_id, bansos=self.key).first()
            euclidean = TopsisEuclideanDistance.query.filter_by(alternative=alternative_id, bansos=self.key).first()
            
            if topsis_in_db is None:
                topsis_in_db = TopsisModel(
                    alternative=alternative_id,
                    bansos=self.key
                )
                db.session.add(topsis_in_db)
            
            topsis_in_db.bansos = self.key
            topsis_in_db.kondisi_ekonomi = float(self.dataset[i][0])
            topsis_in_db.tanggungan = float(self.dataset[i][1])
            topsis_in_db.hutang = float(self.dataset[i][2])
            topsis_in_db.aset = float(self.dataset[i][3])
            topsis_in_db.biaya_listrik = float(self.dataset[i][4])
            topsis_in_db.biaya_air = float(self.dataset[i][5])
            topsis_in_db.preference_value = float(self.score[i])
            topsis_in_db.rank = float(self.ranks[i])

            db.session.commit()
            
            topsis = TopsisModel.query.filter_by(alternative=alternative_id,bansos=self.key).first()

            if normalize_alternative is None:
                normalize_alternative = TopsisNormalization(
                    topsis_id=topsis.id,
                    alternative=alternative_id,
                    bansos=self.key
                )
                db.session.add(normalize_alternative)

            normalize_alternative.bansos = self.key
            normalize_alternative.normalize_kondisi_ekonomi = float(self.normalized_matrix[i][0])
            normalize_alternative.normalize_tanggungan = float(self.normalized_matrix[i][1])
            normalize_alternative.normalize_hutang = float(self.normalized_matrix[i][2])
            normalize_alternative.normalize_aset = float(self.normalized_matrix[i][3])
            normalize_alternative.normalize_biaya_listrik = float(self.normalized_matrix[i][4])
            normalize_alternative.normalize_biaya_air = float(self.normalized_matrix[i][5])

            if weight_alternative is None:
                weight_alternative = TopsisWeighting(
                    topsis_id=topsis.id,
                    alternative=alternative_id,
                    bansos=self.key
                )
                db.session.add(weight_alternative)

            weight_alternative.bansos = self.key
            weight_alternative.weighted_kondisi_ekonomi = float(self.weighted_matrix[i][0])
            weight_alternative.weighted_tanggungan = float(self.weighted_matrix[i][1])
            weight_alternative.weighted_hutang = float(self.weighted_matrix[i][2])
            weight_alternative.weighted_aset = float(self.weighted_matrix[i][3])
            weight_alternative.weighted_biaya_listrik = float(self.weighted_matrix[i][4])
            weight_alternative.weighted_biaya_air = float(self.weighted_matrix[i][5])

            if euclidean is None:
                euclidean = TopsisEuclideanDistance(
                    topsis_id=topsis.id,
                    alternative=alternative_id,
                    bansos=self.key
                )
                db.session.add(euclidean)

            euclidean.bansos = self.key
            euclidean.positive_distance = self.distance_best[i]
            euclidean.negative_distance = self.distance_worst[i]

        # Ideal BEST
        ideal_best = TopsisBestWorst.query.filter_by(status="BEST").first()
        if ideal_best is None:
            ideal_best = TopsisBestWorst(
                status="BEST",
                bansos=self.key
            )
            db.session.add(ideal_best)

        ideal_best.bansos = self.key
        ideal_best.bw_kondisi_ekonomi = float(self.ideal_best[0])
        ideal_best.bw_tanggungan = float(self.ideal_best[1])
        ideal_best.bw_hutang = float(self.ideal_best[2])
        ideal_best.bw_aset = float(self.ideal_best[3])
        ideal_best.bw_biaya_listrik = float(self.ideal_best[4])
        ideal_best.bw_biaya_air = float(self.ideal_best[5])

        # Ideal WORST
        ideal_worst = TopsisBestWorst.query.filter_by(status="WORST").first()
        if ideal_worst is None:
            ideal_worst = TopsisBestWorst(
                status="WORST",
                bansos=self.key
            )
            db.session.add(ideal_worst)

        ideal_worst.bansos = self.key
        ideal_worst.bw_kondisi_ekonomi = float(self.ideal_worst[0])
        ideal_worst.bw_tanggungan = float(self.ideal_worst[1])
        ideal_worst.bw_hutang = float(self.ideal_worst[2])
        ideal_worst.bw_aset = float(self.ideal_worst[3])
        ideal_worst.bw_biaya_listrik = float(self.ideal_worst[4])
        ideal_worst.bw_biaya_air = float(self.ideal_worst[5])

        # Commit semua perubahan sekali saja
        db.session.commit()
