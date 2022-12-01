package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	max_calories := 0
	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	current_calories := 0
	for scanner.Scan() {
		if scanner.Text() != "" {
			cal, err := strconv.Atoi(scanner.Text())
			if err != nil {
				log.Fatal(err)
			}
			current_calories += cal
		} else {
			if max_calories < current_calories {
				max_calories = current_calories
			}
			current_calories = 0
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	fmt.Println(max_calories)
}
