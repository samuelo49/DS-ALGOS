def weighted_vote_counter(votes, num_winners):
    points = {}

    for vote in votes:
        for i, candidate in enumerate(vote):
            points[candidate] = points.get(candidate, 0) + (len(vote) - i)
    print(f"points_data_struct: {points}")
    winners = sorted(points, key=points.get, reverse=True)[:num_winners]

    return winners

# Example usage
votes = [
    ["A", "B", "C"],
    ["A", "C", "B"],
    ["B", "A", "C"],
    ["C", "B", "A"],
    ["C", "A", "B"]
]

num_winners = 2

winners = weighted_vote_counter(votes, num_winners)
print(f"The top {num_winners} winners are: {winners}")
