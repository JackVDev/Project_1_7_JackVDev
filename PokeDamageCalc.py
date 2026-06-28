"""_summary_
    PokeDamageCalc.py
    Jack Verdin
    The main file for my Project 1 program. The program acts as a simplified Pokemon damage calculator.
    6/23/2026
"""

import typechart

# Function: While loop input validation in one function
def valid_input(message, allowed):
    given_value = ""
    while len(given_value) < 1:
        given_value = input(message)
        if given_value not in allowed:
            given_value = ""
            print("Invalid input.")
    return given_value

# Function needed: Damage Calculator
def damage_calc(basepower=100, total_atk=100, total_def=100, type_mult=1, stab=1, rand_adjust=1):
    if type_mult == 0: return 0 # If the type mult is 0, don't bother calculating the damage
    if basepower < 1: basepower = 1 # 1 Is the minimum for power
    if total_atk < 1: total_atk = 1 # 1 Is the minimum for attack
    if total_def < 1: total_def = 1 # 1 Is the minimum for defence, also avoids divide by zero error
    final_damage = (((22 * basepower * (total_atk / total_def)) / 50) + 2) * type_mult * stab * rand_adjust
    final_damage = round(final_damage)
    if final_damage < 1: final_damage = 1 # 1 Is the minimum for damage dealt
    return final_damage

# Function needed? Type effectiveness to message
def type_message(type_mult):
    match type_mult:
        case 0:
            return "It had no effect!"
        case 0.25:
            return "It's barely effective!"
        case 0.5:
            return "It's not very effective."
        case 1:
            return "It's regularly effective"
        case 2:
            return "It's supereffective!"
        case 4:
            return "It's extremely effective!"
        case _:
            return "Unexpected Value"

# Function: Stage Multiplier
def stage_mult(value=10, stage=0):
    """Multiplies a value using pokemon's stage system

    Args:
        value (int, optional): the input value of the function. Defaults to 10.
        stage (int, optional): the stage multiplier, an int between -6 and 6. Defaults to 0.

    Returns:
        int: the output value, given as a rounded int
    """
    # Stages must be an integer
    stage = round(stage)
    # A stage of 0 results in no change to value, so it's skipped early
    if stage == 0:
        return value
    # Stages must be between -6 and 6
    if abs(stage) > 6:
        if stage > 0:
            stage = 6
        else:
            stage = -6
    # Stages begin with a fraction of 2/2
    stage_num = 2
    stage_den = 2
    # Positive stages add to numerator, negative stages add to denomenator
    if stage > 0:
        stage_num += stage
    else:
        stage_den += abs(stage)
    # Multiplier is calculated by the fraction
    mult = stage_num / stage_den
    return round(value * mult)

# Code needed: User input
print("- Pokemon Damage Calculator -\n")
given_atk = int(input("Please input the attacking Pokemon's Attack stat: "))
given_atkst = int(input("Please input the attacking Pokemon's Attack stage: "))
given_def = int(input("Please input the defending Pokemon's Defence stat: "))
given_defst = int(input("Please input the defending Pokemon's Defence stage: "))
given_hp = int(input("Please input the defending Pokemon's max HP: "))
given_power = int(input("Please input the base power of the move used: "))
given_typeatk = valid_input("Please input the type of the move used: ", typechart.type_list)
given_typeatk = typechart.type_list.index(given_typeatk)
given_typedef1 = valid_input("Please input the first type of the defending Pokemon: ", typechart.type_list)
given_typedef1 = typechart.type_list.index(given_typedef1)
given_typedef2 = valid_input("Please input the second type of the defending Pokemon: ", typechart.type_list)
given_typedef2 = typechart.type_list.index(given_typedef2)
given_stab = valid_input("Does the move used benefit from the Same Type Attack Bonus?(Y/N) ", ["Y", "N"])
if given_stab == "Y": given_stab = 1.5
else: given_stab = 1
given_typemult = given_typedef1 * given_typedef2
# Code needed: Do the math
total_atk = stage_mult(given_atk, given_atkst)
print(f"With an Attack stat of {given_atk} at stage {given_atkst},\nthe attacking Pokemon has an effective Attack stat of {total_atk}")
total_def = stage_mult(given_def, given_defst)
print(f"With an Defence stat of {given_def} at stage {given_defst},\nthe defending Pokemon has an effective Defence stat of {total_def}")
# Code needed: Output message to terminal