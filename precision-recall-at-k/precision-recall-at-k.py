def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    recommended_k = recommended[:k]
    match = sum(1 for item in recommended_k if item in relevant)
    precision = match/k
    recall = match/len(relevant)
    return [precision, recall]