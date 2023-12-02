
import re

# aoc_input = ["abcone2threexyz"]

inputs = []
with open("/Users/mills/Coding/Python/advent_of_code2023/day1_input.txt", "r") as file:
    for line in file:
        new_line = ""
        re_match = re.findall(r'((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine))',line)
        if re_match:
            for match in re_match:
                if match[0] == "one":
                    if new_line:
                        new_line = re.sub(match[0], "1", new_line)
                    else:
                        new_line = re.sub(match[0], "1", line)
                elif match[0] == "two":
                    if new_line:
                        new_line = re.sub(match[0], "2", new_line)
                    else:
                        new_line = re.sub(match[0], "2", line)
                elif match[0] == "three":
                    if new_line:
                        new_line = re.sub(match[0], "3", new_line)
                    else:
                        new_line = re.sub(match[0], "3", line)
                elif match[0] == "four":
                    if new_line:
                        new_line = re.sub(match[0], "4", new_line)
                    else:
                        new_line = re.sub(match[0], "4", line)
                elif match[0] == "five":
                    if new_line:
                        new_line = re.sub(match[0], "5", new_line)
                    else:
                        new_line = re.sub(match[0], "5", line)
                elif match[0] == "six":
                    if new_line:
                        new_line = re.sub(match[0], "6", new_line)
                    else:
                        new_line = re.sub(match[0], "6", line)
                elif match[0] == "seven":
                    if new_line:
                        new_line = re.sub(match[0], "7", new_line)
                    else:
                        new_line = re.sub(match[0], "7", line)
                elif match[0] == "eight":
                    if new_line:
                        new_line = re.sub(match[0], "8", new_line)
                    else:
                        new_line = re.sub(match[0], "8", line)
                elif match[0] == "nine":
                    if new_line:
                        new_line = re.sub(match[0], "9", new_line)
                    else:
                        new_line = re.sub(match[0], "9", line)
            # print(new_line)
            inputs.append(new_line.strip("\n"))
        else:
            # print(line)
            inputs.append(line.strip("\n"))

print(inputs)
print(len(inputs))

input_totals = []

for input in inputs:
    if input:
        numbers = []
        for char in input:
            if any(
                [
                char == "1",
                char == "2",
                char == "3",
                char == "4",
                char == "5",
                char == "6",
                char == "7",
                char == "8",
                char == "9",
                ]
            ):
                numbers.append(char)
        if len(numbers) == 1:
            combined_numbers = int(numbers[0])
        else:
            combined_numbers = int(numbers[0] + numbers[-1])
        input_totals.append(combined_numbers)

print(input_totals)

sum = 0

for total in input_totals:
    sum += total

print(sum)
