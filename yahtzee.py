"""
Project: Creating a 2 player Yahtzee game.

Name: Sam Khademolhosseini
Student #: A01233111
Class: Comp 1510
Starting Date: December 3, 2020
Due Date: December 11, 2020

"""
import random


def STILL_NO_SCORE() -> int:
    """
    In the score sheet keys that have no score yet have a value of -1. So, -1 is the constant value for rows
    without score.
    """
    return -1


def IS_FULL_HOUSE() -> int:
    """
    Score of a full house is always 25 in yahtzee.
    """
    return 25


def IS_SMALL_STRAIGHT() -> int:
    """
    Score of a small straight is always 30 in yahtzee.
    """
    return 30


def IS_LARGE_STRAIGHT() -> int:
    """
    Score of a large straight is always 40 in yahtzee.
    """
    return 40


def IS_FIRST_YAHTZEE() -> int:
    """
    Score of the first yahtzee is always 50.
    """
    return 50


def IS_YAHTZEE_BONUS() -> int:
    """
    Score of yahtzee bonus is always 100.
    """
    return 100


def WORTH_NOTHING() -> int:
    """
    If current dice doesn't match the selected row, the score would always be 0.
    """
    return 0


def UPPER_SECTION_BONUS() -> int:
    """
    Bonus for upper section is always 35.
    """
    return 35


def UPPER_SECTION_BONUS_REQUIREMENT() -> int:
    """
    To get the upper bonus total of upper must be greater than 63.
    """
    return 63


def NUMBER_OF_DICE_IN_YAHTZEE() -> int:
    """
    There are always 5 dice in yahtzee
    """
    return 5


def create_score_sheet() -> dict:
    """
    Create the Yahtzee score sheet for one player.

    >>> create_score_sheet()
    {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}
    """
    score_sheet = {'Aces': -1, 'Twos': -1, 'Threes': -1, 'Fours': -1, 'Fives': -1, 'Sixes': -1, 'Upper Score': 0, '\
Upper Bonus': 0, 'Total Upper Score': 0, '3 of a kind': -1, '4 of a kind': -1, 'Full House': -1, '\
Small Straight': -1, 'Large Straight': -1, 'YAHTZEE': -1, 'Chance': -1, 'Yahtzee Bonus Count': 0, '\
Yahtzee Bonus Score': 0, 'Total Lower Score': 0, 'Grand Total': 0}
    return score_sheet


def roll_dice(number_of_dice_to_roll: int) -> list:
    """
    Roll some dice and store the result in a list.

    :param number_of_dice_to_roll: Number of dice the user wants to roll as an integer.
    :precondition: parameter must be a positive integer.
    :postcondition: Will role dice and return their face value in a list.
    :return: A list containing random numbers between 1 and 6.
    """
    dice_list = [random.randint(1, 6) for _ in range(number_of_dice_to_roll)]
    return sorted(dice_list)


def print_dice(dice_list: list) -> None:
    """
    Print current dice that the user has.

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Parameter must be a list containing numbers.
    :postcondition: Will print each die in the dice in the dice_list in a new line.

    >>> print_dice([1, 2, 4, 4, 6])
    Current dice:
    Die 1: 1
    Die 2: 2
    Die 3: 4
    Die 4: 4
    Die 5: 6
    >>> print_dice([1, 5, 5])
    Current dice:
    Die 1: 1
    Die 2: 5
    Die 3: 5
    """
    print("Current dice:")
    for count, die in enumerate(dice_list, 1):
        print(f"Die {count}: {die}")


def re_roll_handler(dice_list: list) -> None:
    """
    Initiate re-rolling if user wants to re-roll.

    :param dice_list: A list containing the face value of current dice.
    :precondition: Dice list must contain integers.
    :postcondition: Will call re_roll_selected_dice function up to 2 times based on user input.
    """
    first_re_roll = input("Enter 'yes' if you want to re-roll, anything else if you don't: ").lower().strip()

    if first_re_roll == "yes":
        dice_to_re_roll = get_valid_dice()
        re_roll_selected_dice(dice_list, dice_to_re_roll)
        print_dice(dice_list)

        second_re_roll = input("Enter 'yes' if you want to re-roll, anything else if you don't: ").lower().strip()

        if second_re_roll == "yes":
            dice_to_re_roll = get_valid_dice()
            re_roll_selected_dice(dice_list, dice_to_re_roll)
            print_dice(dice_list)


def get_valid_dice() -> list:
    """
    Ask user to type in the dice number of dice that he/she wants to re-roll.

    :precondition: No precondition.
    :postcondition: Will keep asking for user input if the input isn't valid.
    :return: A list containing selected dice.
    """
    dice_to_re_roll = []
    is_valid = False
    while not is_valid:
        dice_to_re_roll = sorted(input("Enter the dice number(s) that you want to re-roll with a space between them."
                                       "(ex. '2 3 5' re-rolls the second, third, and the fifth die): ").strip().split())
        if dice_to_re_roll[0] in ["1", "2", "3", "4", "5"] and \
                dice_to_re_roll[-1] in ["1", "2", "3", "4", "5"]:
            is_valid = True

    return dice_to_re_roll


def re_roll_selected_dice(dice_list: list, list_of_dice_to_re_roll: list) -> None:
    """
    Re-roll the selected dice from the dice list.

    :param dice_list: A list containing the face value of 5 dice.
    :param list_of_dice_to_re_roll: A list containing the dice number of the dice that user wants to re-roll.
    :precondition: The numbers in the second list must be between 1 to length of dice_list.
    :postcondition: Will replace the value of the selected dice with new random numbers.
    """
    for dice_num in list_of_dice_to_re_roll:
        dice_index = int(dice_num) - 1
        dice_list[dice_index] = random.randint(1, 6)

    dice_list.sort()


def print_yahtzee_score_sheet(score_sheet: dict) -> None:
    """
    Print the Yahtzee score sheet.

    :param score_sheet: A dictionary representing the Yahtzee score sheet
    :precondition: The parameter must be a dictionary.
    :postcondition: Will print each key value pair in a new line leading by number of the row.

    >>> print_yahtzee_score_sheet({'Aces': -1, 'Twos': 6, 'Threes': 0, 'Full House': 25, 'Total': 31})
    Current state of your score sheet (not used rows are displayed as -1):
    1. Aces: -1
    2. Twos: 6
    3. Threes: 0
    4. Full House: 25
    5. Total: 31
    """
    print("Current state of your score sheet (not used rows are displayed as -1):")
    for count, (key, value) in enumerate(score_sheet.items(), 1):
        print(f"{count}. {key}: {value}")


def available_rows(score_sheet: dict) -> list:
    """
    Find all available rows.

    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: Available rows in the dict must have value of -1 to count.
    :postcondition: Will print all available rows and return a list containing the row number of the available rows.
    :return: A list containing the row number of the available rows.
    >>> available_rows({"Aces": -1, "Twos": 4, "Full House": -1, "Small Straight": 30, "YAHTZEE": 50})
    Following rows are currently available in you score sheet.
    1: Aces
    3: Full House
    5: YAHTZEE
    ['1', '3', '5']
    """
    all_available_rows = []
    print("Following rows are currently available in you score sheet.")
    for count, (key, value) in enumerate(score_sheet.items(), 1):
        if score_sheet[key] == -1:
            print(f"{count}: {key}")
            all_available_rows.append(str(count))
        elif key == "YAHTZEE" and score_sheet["YAHTZEE"] == 50:
            print(f"{count}: {key}")
            all_available_rows.append(str(count))

    return all_available_rows


def ask_for_valid_row(row_that_are_available: list) -> str:
    """
    Ask for user input until it's a valid row.

    :param row_that_are_available: A list containing the row number of the availabe rows.
    :precondition: No precondition.
    :postcondition: Will validate the input. If the input is not valid, it keeps asking for input.
    :return: A valid numeric string.
    """
    selected_row = input("Select the row number of the row you want to use this time: ")

    while selected_row not in row_that_are_available:
        selected_row = input("Select the row number of the row you want to use this time: ")

    return selected_row


def lower_section_score_calculator(dice_list: list, valid_row: str) -> int:
    """
    Calculate the score for lower section.

    Calls the right functions to calculate the score based on the valid_row.

    :param dice_list: A list containing the face value of 5 dice.
    :param valid_row: A valid numeric string representing the selected row.
    :precondition: Valid_row must be a string.
    :postcondition: Will call the right function to calculate the score.
    :return: The score as an integer.

    >>> lower_section_score_calculator([1, 2, 3, 4, 5], "14")
    40
    >>> lower_section_score_calculator([1, 1, 3, 3, 3], "12")
    25
    >>> lower_section_score_calculator([1, 2, 3, 4, 5], "12")
    0
    """
    score = 0
    if valid_row == "10":
        score = three_of_a_kind_score_calculator(dice_list)
    elif valid_row == "11":
        score = four_of_a_kind_score_calculator(dice_list)
    elif valid_row == "12":
        score = full_house_score_calculator(dice_list)
    elif valid_row == "13":
        score = small_straight_score_calculator(dice_list)
    elif valid_row == "14":
        score = large_straight_score_calculator(dice_list)
    elif valid_row == "16":
        score = chance_score_calculator(dice_list)

    return score


def upper_section_score_calculator(dice_list: list, valid_row: str) -> int:
    """
    Calculate the score for Aces, Twos, Threes, Fours, Fives, Sixes rows.

    :param dice_list: A list containing the face value of 5 dice.
    :param valid_row: A valid numeric string representing the selected row.
    :precondition: Dice list must contain integers and must be a sorted list. Chosen row must be a valid numeric string.
    :postcondition: Will calculate the score based on the dice that the user has.
    :return: The score as an integer.

    >>> upper_section_score_calculator([1, 1, 3, 5, 5], "5")
    10
    >>> upper_section_score_calculator([2, 2, 2, 2, 6], "2")
    8
    >>> upper_section_score_calculator([1, 2, 3, 4, 5], "6")
    0
    """
    count = dice_list.count(int(valid_row))
    score = count * int(valid_row)
    return score


def three_of_a_kind_score_calculator(dice_list: list) -> int:
    """
    Calculate the score for three of a kind.

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will calculate the score based on the dice that the user has.
    :return: The score as an integer.

    >>> three_of_a_kind_score_calculator([2, 3, 3, 3, 3])
    14
    >>> three_of_a_kind_score_calculator([1, 1, 1, 1, 1])
    5
    >>> three_of_a_kind_score_calculator([2, 2, 2, 5, 6])
    17
    >>> three_of_a_kind_score_calculator([1, 2, 2, 4, 5])
    0
    """
    possible_score = 0
    for num in dice_list:
        possible_score += num

    for die in dice_list:
        if dice_list.count(die) >= 3:
            return possible_score

    return WORTH_NOTHING()


def four_of_a_kind_score_calculator(dice_list: list) -> int:
    """
    Calculate the score for four of a kind.

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will calculate the score based on the dice that the user has.
    :return: The score as an integer.

    >>> four_of_a_kind_score_calculator([2, 3, 3, 3, 3])
    14
    >>> four_of_a_kind_score_calculator([1, 1, 1, 1, 1])
    5
    >>> four_of_a_kind_score_calculator([3, 3, 3, 3, 6])
    18
    >>> four_of_a_kind_score_calculator([3, 3, 4, 5, 6])
    0
    """
    possible_score = 0
    for num in dice_list:
        possible_score += num

    for die in dice_list:
        if dice_list.count(die) >= 4:
            return possible_score

    return WORTH_NOTHING()


def full_house_score_calculator(dice_list: list) -> int:
    """
    Calculate the score for a full house.

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will return 25 if it's a valid full house, else 0.
    :return: The score as an integer.

    >>> full_house_score_calculator([2, 2, 4, 4, 4])
    25
    >>> full_house_score_calculator([2, 2, 3, 3, 3])
    25
    >>> full_house_score_calculator([1, 1, 2, 2, 3])
    0
    """
    for die_1 in dice_list:
        for die_2 in dice_list:
            if dice_list.count(die_1) == 2 and dice_list.count(die_2) == 3:
                return IS_FULL_HOUSE()

    return WORTH_NOTHING()


def small_straight_score_calculator(dice_list: list) -> int:
    """
    Calculate the score for small straight (sequence of 4).

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will return 30 if it's a valid small straight, else 0.
    :return: The score as an integer.

    >>> small_straight_score_calculator([1, 2, 3, 4, 6])
    30
    >>> small_straight_score_calculator([3, 4, 4, 5, 6])
    30
    >>> small_straight_score_calculator([1, 2, 3, 3, 5])
    0
    """
    no_duplicate_dice_list = list(set(dice_list))
    while no_duplicate_dice_list[0] > 1:
        for index in range(len(no_duplicate_dice_list)):
            no_duplicate_dice_list[index] -= 1

    if no_duplicate_dice_list == [1, 2, 3, 4] or no_duplicate_dice_list == [1, 2, 3, 4, 5] or \
            no_duplicate_dice_list == [1, 2, 3, 4, 6] or no_duplicate_dice_list == [1, 3, 4, 5, 6]:
        return IS_SMALL_STRAIGHT()

    else:
        return WORTH_NOTHING()


def large_straight_score_calculator(dice_list: list) -> int:
    """
    Calculate the score for large straight (sequence of 5).

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will return 40 if it's a valid large straight, else 0.
    :return: The score as an integer.

    >>> large_straight_score_calculator([1, 2, 3, 4, 5])
    40
    >>> large_straight_score_calculator([2, 3, 4, 5, 6])
    40
    >>> large_straight_score_calculator([1, 2, 3, 4, 6])
    0
    """
    if dice_list == [1, 2, 3, 4, 5] or dice_list == [2, 3, 4, 5, 6]:
        return IS_LARGE_STRAIGHT()
    else:
        return WORTH_NOTHING()


def chance_score_calculator(dice_list: list) -> int:
    """
    Add the face number of all the dice.

    :param dice_list: A list containing the face value of 5 dice.
    :precondition: Dice list must contain integers and must be a sorted list.
    :postcondition: Will add the value of all the dice.
    :return: The score as an integer.

    >>> chance_score_calculator([1, 2, 3, 4, 5])
    15
    >>> chance_score_calculator([1, 2, 2, 3, 3])
    11
    >>> chance_score_calculator([1, 1, 1, 1, 1])
    5
    """
    score = 0
    for die in dice_list:
        score += die
    return score


def yahtzee_score_handler(dice_list: list, score_sheet: dict) -> None:
    """
    Calculate and submit the score for yahtzee.

    :param dice_list: A list containing the face value of 5 dice.
    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: Dice list must contain integers and must be a sorted list.
    :precondition: Score Sheet dictionary must have YAHTZEE key.
    :postcondition: Will handle yahtzee score and its possible bonuses.
    """
    if dice_list.count(dice_list[0]) == 5:
        if score_sheet["YAHTZEE"] == -1:
            score_sheet["YAHTZEE"] = IS_FIRST_YAHTZEE()
            score_sheet["Total Lower Score"] += IS_FIRST_YAHTZEE()
            score_sheet["Grand Total"] += IS_FIRST_YAHTZEE()

        elif score_sheet["YAHTZEE"] == 50:
            score_sheet["Yahtzee Bonus Count"] += 1
            score_sheet["Yahtzee Bonus Score"] += IS_YAHTZEE_BONUS()
            score_sheet["Total Lower Score"] += IS_YAHTZEE_BONUS()
            score_sheet["Grand Total"] += IS_YAHTZEE_BONUS()

    else:
        if score_sheet["YAHTZEE"] == -1:
            score_sheet["YAHTZEE"] = WORTH_NOTHING()


def submit_upper_section_score(score: int, valid_row: str, score_sheet: dict) -> None:
    """
    Save the score as the value of the selected row.

    :param score: An integer representing the score.
    :param valid_row: A valid numeric string representing the selected row.
    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: Selected row must be valid.
    :postcondition: Will change the value of the selected key in the score sheet to the score.
    """
    if valid_row == "1":
        score_sheet['Aces'] = score
    elif valid_row == "2":
        score_sheet['Twos'] = score
    elif valid_row == "3":
        score_sheet['Threes'] = score
    elif valid_row == "4":
        score_sheet['Fours'] = score
    elif valid_row == "5":
        score_sheet['Fives'] = score
    else:
        score_sheet['Sixes'] = score

    score_sheet['Upper Score'] += score
    score_sheet['Total Upper Score'] += score
    score_sheet['Grand Total'] += score

    if score_sheet['Upper Score'] >= UPPER_SECTION_BONUS_REQUIREMENT():
        score_sheet['Upper Bonus'] = UPPER_SECTION_BONUS()
        score_sheet['Total Upper Score'] += UPPER_SECTION_BONUS()
        score_sheet['Grand Total'] += UPPER_SECTION_BONUS()


def submit_lower_section_score(score: int, valid_row: str, score_sheet: dict) -> None:
    """
    Save the score as the value of the selected row.

    :param score: An integer representing the score.
    :param valid_row: A valid numeric string representing the selected row.
    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: Selected row must be valid.
    :postcondition: Will change the value of the selected key in the score sheet to the score.
    """
    if valid_row == "10":
        score_sheet['3 of a kind'] = score
    elif valid_row == "11":
        score_sheet['4 of a kind'] = score
    elif valid_row == "12":
        score_sheet['Full House'] = score
    elif valid_row == "13":
        score_sheet['Small Straight'] = score
    elif valid_row == "14":
        score_sheet['Large Straight'] = score
    else:
        score_sheet['Chance'] = score

    score_sheet['Total Lower Score'] += score
    score_sheet['Grand Total'] += score


def calculate_and_submit_score(dice_list: list, valid_row: str, score_sheet: dict) -> None:
    """
    Call right functions to handle score calculation and submission.

    Invoke all functions needed to calculate score based on the hand and submit the score to the score sheet.

    :param dice_list: A list containing the face value of 5 dice.
    :param valid_row: A valid numeric string representing the selected row.
    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: all parameters must be valid and must be the right type.
    :postcondition: Will calculate score and save changes to the score sheet.
    """
    if valid_row == "15":
        yahtzee_score_handler(dice_list, score_sheet)

    elif valid_row in ["1", "2", "3", "4", "5", "6"]:
        score = upper_section_score_calculator(dice_list, valid_row)
        submit_upper_section_score(score, valid_row, score_sheet)

    else:
        score = lower_section_score_calculator(dice_list, valid_row)
        submit_lower_section_score(score, valid_row, score_sheet)


def one_round_yahtzee(score_sheet) -> None:
    """
    Invoke functions for one round (not game) of Yahtzee.

    :param score_sheet: A dictionary representing the Yahtzee score sheet.
    :precondition: Score sheet must be a valid Yahtzee score sheet in the format of a dictionary.
    :postcondition: Allows user to play one round of Yahtzee.
    """
    current_dice = roll_dice(NUMBER_OF_DICE_IN_YAHTZEE())
    print_dice(current_dice)
    re_roll_handler(current_dice)

    still_available_rows = available_rows(score_sheet)
    valid_selected_row = ask_for_valid_row(still_available_rows)

    calculate_and_submit_score(current_dice, valid_selected_row, score_sheet)
    print_yahtzee_score_sheet(score_sheet)


def identify_winner(score_sheet_1: dict, score_sheet_2: dict) -> None:
    """

    :param score_sheet_1: A dictionary representing the Yahtzee score sheet for player 1.
    :param score_sheet_2: A dictionary representing the Yahtzee score sheet for player 2.
    :precondition: Score sheet must be a valid Yahtzee score sheet in the format of a dictionary.
    :postcondition: Will print the winner.
    """
    print(f"Player 1 Grand total score: {score_sheet_1['Grand Total']}")
    print(f"Player 2 Grand total score: {score_sheet_2['Grand Total']}")
    if score_sheet_1["Grand Total"] > score_sheet_2["Grand Total"]:
        print(f"Player 1 wins by {score_sheet_1['Grand Total'] - score_sheet_2['Grand Total']}")

    elif score_sheet_2["Grand Total"] > score_sheet_1["Grand Total"]:
        print(f"Player 2 wins by {score_sheet_2['Grand Total'] - score_sheet_1['Grand Total']}")

    else:
        print("WOW! It's a draw.")


def yahtzee():
    """
    Call the right functions to play a 2 player Yahtzee game.

    :precondition: No precondition.
    :postcondition: User will start a 2 player Yahtzee game.
    """
    score_sheet_p1 = create_score_sheet()
    score_sheet_p2 = create_score_sheet()
    while -1 in score_sheet_p1.values() or -1 in score_sheet_p2.values():
        if -1 in score_sheet_p1.values():
            print("<< Player 1's turn >>")
            one_round_yahtzee(score_sheet_p1)

        if -1 in score_sheet_p2.values():
            print("<< Player 2's turn >>")
            one_round_yahtzee(score_sheet_p2)

    identify_winner(score_sheet_p1, score_sheet_p2)


def main():
    """
    Drives the program.
    """
    yahtzee()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
