# Function needed: Type effectiveness calc
def type_calc(type_atk, type_def1, type_def2):
    #Unfinished
    return 1

# Function needed: Damage Calculator
def damage_calc():
    #Unfinished
    return 1

# Function needed? Type effectiveness to message
def type_message(type_mult):
    #Unfinished
    return "Unfinished Message"

# Function: Stage Multiplier
def stage_mult(value=10, stage=0):
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
    return (value * mult)

# Code needed: User input
# Code needed: Do the math
# Code needed: Output message to terminal