def hide(card_number):
    
    card_str = str(card_number)
    first_part = card_str[:2]
    last_part = card_str[-4:]
    mask = "*" * 10
    
    return first_part + mask + last_part