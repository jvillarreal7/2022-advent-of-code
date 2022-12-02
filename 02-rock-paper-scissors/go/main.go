package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

var matchups = map[string]string{
	"A": "Z",
	"B": "X",
	"C": "Y",
}

var equivalent_plays = map[string]string{
	"A": "X",
	"B": "Y",
	"C": "Z",
}

var play_values = map[string]int{
	"Z": 3,
	"Y": 2,
	"X": 1,
}

var outcome_values = map[string]int{
	"win":  6,
	"draw": 3,
	"lose": 0,
}

func get_match_outcome(play_against, own_play string) string {
	if own_play == equivalent_plays[play_against] {
		return "draw"
	}
	if matchups[play_against] == own_play {
		return "lose"
	}
	return "win"
}

func get_total_score() int {
	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	total_score := 0

	for scanner.Scan() {
		clean_line := strings.Trim(scanner.Text(), "\n")
		match_split := strings.Split(clean_line, " ")
		outcome := get_match_outcome(match_split[0], match_split[1])
		total_score += play_values[match_split[1]] + outcome_values[outcome]
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return total_score
}

func main() {
	fmt.Println(get_total_score())
}
