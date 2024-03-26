def validate_generation_number(generation: str) -> int:
    try:
        generation_number = int(generation)
    except ValueError:
        raise Exception('generation_number_not_an_integer_value', generation)
    
    available_generations = [1, 2, 3, 4, 5, 6, 7]

    if generation_number not in available_generations:
        raise Exception('invalid_generation_number_value', generation_number)
    
    return generation_number
