from cs50 import get_string, get_int
from sys import exit, argv
from math import inf

MAX_VOTERS = 100
MAX_CANDIDATES = 9


class Candidate():
    def __init__(self, name, votes, eliminated):
        self.name = name
        self.votes = votes
        self.eliminated = eliminated


candidates = []
preferences = []


def main():

    # Check for invalid usage
    if len(argv) < 2:
        print("Usage: python runoff [candidate ...]")
        exit(1)

    global candidate_count
    candidate_count = len(argv) - 1

    # Populate candidates dictionary
    if candidate_count > MAX_CANDIDATES:
        print(f"Maximum number of candidates is {MAX_CANDIDATES}")
        exit(2)

    for name in argv[1:]:
        candidate = Candidate(name, 0, False)
        candidates.append(candidate)

    global voter_count
    voter_count = get_int("Number of voters: ")
    if voter_count > MAX_VOTERS:
        print(f"Maximum number of voters is {MAX_VOTERS}")
        exit(3)

    # Keep querying for votes
    for i in range(voter_count):

        # Query for each rank
        for j in range(candidate_count):
            name = get_string(f"Rank {j + 1}: ")

            # Record vote, unless it's invalid
            if not vote(i, j, name):
                print("Invalid vote.")
                exit(4)

        print()

    # Keep holding runoffs until winner exists
    while True:
        tabulate()

        # Check if election has been won
        won = print_winner()

        if won:
            break

        # Eliminate last-place candidates
        min_votes = find_min()
        tie = is_tie(min_votes)

        # If tie, everyone wins
        if tie:
            for candidate in candidates:
                if (not candidate.eliminated):
                    print(candidate.name)
            break

        # Eliminate anyone with a minimum number of votes
        eliminate(min_votes)

        # Reset vote counts back to zero
        for candidate in candidates:
            candidate.votes = 0


# Record preference if vote is valid
def vote(voter, rank, name):
    # TODO
    return False


# Tabulate votes for non-eliminated candidates
def tabulate():
    # TODO
    return


def print_winner():
    # TODO
    return False


def find_min():
    # TODO
    return 0


def is_tie(min_votes):
    # TODO
    return False


def eliminate(min_votes):
    # TODO
    return


if __name__ == "__main__":
    main()
