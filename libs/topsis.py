import numpy as np
import topsispy as tp


def topsis_method(dataset, weights, criterion_type):
    dt = np.array(dataset)
    result = tp.topsis(dt, weights, criterion_type)
    listed_result = list(result)

    # Calculating ranks
    ranks = np.argsort(np.argsort(-listed_result[1])) + 1

    return listed_result[1], ranks
