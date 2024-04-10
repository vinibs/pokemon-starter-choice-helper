import sys
from base.enums import AdvantageCondition
from services import data_processing, validation

def startup(arguments = sys.argv):
    if len(arguments) < 2:
        raise Exception('Please provide the generation number as the first argument.')

    try:
        generation_number = validation.validate_generation_number(arguments[1])
        starters_data = data_processing.process_starters_advantages(generation_number)

        print(f'\n# STARTERS ADVANTAGE CONDITION COUNTERS FOR GENERATION {generation_number} #\n')

        for starter_name, advantage_conditions in starters_data.items():
            starter_data_output = f'- {starter_name}:\n'
            starter_data_output += ''.join(
                f'\t- {condition.value} = {len(advantage_conditions[condition])} species\n'
                for condition in AdvantageCondition
            )
            
            print(starter_data_output)

    except Exception as err:
        raise Exception(f"It wasn't possible to calculate the starters' conditions for the provided arguments. Error details: {err}")


if __name__ == '__main__':
    startup()
