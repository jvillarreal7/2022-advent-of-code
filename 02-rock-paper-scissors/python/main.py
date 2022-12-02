# Opposing rock beats scissors
# Opposing paper beats rock
# Opposing scissors beats paper
MATCHUPS = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

# Rock, paper, scissors
EQUIVALENT_PLAYS = {"A": "X", "B": "Y", "C": "Z"}

PLAY_VALUES = {"Z": 3, "Y": 2, "X": 1}

OUTCOME_VALUES = {"win": 6, "draw": 3, "lose": 0}


def get_match_outcome(play_against, own_play) -> str:
    if own_play == EQUIVALENT_PLAYS[play_against]:
        return "draw"
    if MATCHUPS[play_against] == own_play:
        return "lose"
    return "win"


def get_total_score() -> int:
    with open("../input.txt", "r") as f:
        total_score = 0
        for line in f:
            play_against, own_play = line.strip("\n").split(" ")
            outcome = get_match_outcome(play_against, own_play)
            total_score += PLAY_VALUES[own_play] + OUTCOME_VALUES[outcome]
    return total_score


print(get_total_score())
