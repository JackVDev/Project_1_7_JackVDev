"""_summary_
    PokeDamageCalc.py
    Jack Verdin
    The main file for my Project 1 program. The program acts as a simplified Pokemon damage calculator.
    6/23/2026
"""

# Function needed: Damage Calculator
def damage_calc():
    #Unfinished
    return 1

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
# Code needed: Do the math
# Code needed: Output message to terminal