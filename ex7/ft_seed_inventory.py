def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    prefix = seed_type + " seeds:"
    if unit == "area":
        prefix = seed_type + " seeds: covers"
    suffix = "packets available"
    if unit == "grams":
        suffix = "grams total"
    elif unit == "area":
        suffix = "square meters"
    print(prefix, quantity, suffix)
