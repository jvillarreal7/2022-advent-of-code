const fs = require("fs");

const matchups = {
  A: "Z",
  B: "X",
  C: "Y",
};

const equivalentPlays = { A: "X", B: "Y", C: "Z" };

const playValues = { Z: 3, Y: 2, X: 1 };

const outcomeValues = { win: 6, draw: 3, lose: 0 };

const getMatchOutcome = (playAgainst, ownPlay) => {
  if (ownPlay === equivalentPlays[playAgainst]) {
    return "draw";
  }
  if (matchups[playAgainst] === ownPlay) {
    return "lose";
  }
  return "win";
};

const getTotalScore = () => {
  let totalScore = 0;
  try {
    const fileContent = fs.readFileSync("../input.txt", "utf-8");
    fileContent.split(/\r?\n/).forEach((line) => {
      matchSplit = line.split(" ");
      outcome = getMatchOutcome(matchSplit[0], matchSplit[1]);
      totalScore += playValues[matchSplit[1]] + outcomeValues[outcome];
    });

    return totalScore;
  } catch (err) {
    console.error(err);
  }
};

console.log(getTotalScore());
