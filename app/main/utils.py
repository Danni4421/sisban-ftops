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
    for i in range(len(topsis_results)):
        alternatives[i]["value"] = topsis_results[i]
        alternatives[i]["rank"] = topsis_ranks[i]

        # Delete unused variable
        del alternatives[i]["kondisi_ekonomi"]
        del alternatives[i]["tanggungan"]
        del alternatives[i]["hutang"]
        del alternatives[i]["aset"]
        del alternatives[i]["biaya_listrik"]
        del alternatives[i]["biaya_air"]
    
    return alternatives