package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
	"unicode"

	"github.com/juliangruber/go-intersect/v2"
)

func getItemPriority(item []rune) int {
	if unicode.IsUpper(item[0]) {
		return int(item[0]) - 38
	}
	return int(item[0]) - 96
}

func getRucksacks() [][]string {
	f, err := os.Open("../input.txt")
	if err != nil {
		log.Fatal(err)
	}

	defer f.Close()

	scanner := bufio.NewScanner(f)

	rucksack := [][]string{}
	compartments := []string{}

	for scanner.Scan() {
		cleanLine := strings.Trim(scanner.Text(), "\n")
		halfRucksackLength := len(cleanLine) / 2
		firstCompartment := cleanLine[:halfRucksackLength]
		secondCompartment := cleanLine[halfRucksackLength:]
		compartments = append(compartments, firstCompartment, secondCompartment)
		rucksack = append(rucksack, compartments)
		compartments = []string{}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return rucksack
}

func getCommonItem(rucksack []string) string {
	commonItem := intersect.SimpleGeneric[string](strings.Split(rucksack[0], ""), strings.Split(rucksack[1], ""))
	return commonItem[0]
}

func main() {
	totalItemPriority := 0
	rucksacks := getRucksacks()
	for _, rucksack := range rucksacks {
		commonItem := getCommonItem(rucksack)
		totalItemPriority += getItemPriority([]rune(commonItem))
	}
	fmt.Println(totalItemPriority)
}
