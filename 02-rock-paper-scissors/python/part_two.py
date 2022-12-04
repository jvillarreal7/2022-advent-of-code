# Opposing rock beats scissors
# Opposing paper beats rock
# Opposing scissors beats paper
WINNING_MATCHUPS = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

# Opposing rock loses to paper
# Opposing paper loses to scissors
# Opposing scissors loses to rock
LOSING_MATCHUPS = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

# Rock, paper, scissors
EQUIVALENT_PLAYS = {"A": "X", "B": "Y", "C": "Z"}

PLAY_VALUES = {"Z": 3, "Y": 2, "X": 1}

OUTCOME_VALUES = {"Z": 6, "Y": 3, "X": 0}


def get_own_play(play_against: str, desired_outcome: str) -> str:
    if desired_outcome == "Y":
        return EQUIVALENT_PLAYS[play_against]
    if desired_outcome == "Z":
        return LOSING_MATCHUPS[play_against]
    return WINNING_MATCHUPS[play_against]


def get_total_score() -> int:
    with open("../input.txt", "r") as f:
        total_score = 0
        for line in f:
            play_against, desired_outcome = line.strip("\n").split(" ")
            own_play = get_own_play(play_against, desired_outcome)
            total_score += PLAY_VALUES[own_play] + OUTCOME_VALUES[desired_outcome]
    return total_score


print(get_total_score())
