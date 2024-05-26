import numpy as np


def map_alternative_after_fuzzied(alternatives):
    result = []

    for alternative in alternatives:
        result.append([
            alternative.get('kondisi_ekonomi'),
            alternative.get('tanggungan'),
            alternative.get('hutang'),
            alternative.get('aset'),
            alternative.get('biaya_listrik'),
            alternative.get('biaya_air')
        ])

    return result


def map_topsis_rank(alternatives, topsis_results, topsis_ranks):
    new_result = []

    for i in range(len(topsis_results)):
        new_result.append({
            'alternative': alternatives[i]['alternatif'],
            'value': topsis_results[i],
            'rank': topsis_ranks[i]
        })

    return new_result


def convert_to_serializable(data):
    if isinstance(data, np.int64):
        return int(data)
    elif isinstance(data, list):
        return [convert_to_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {key: convert_to_serializable(value) for key, value in data.items()}
    return data
