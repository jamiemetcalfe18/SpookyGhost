import random
# Random body parts
def generate_spooky_ghost():
    eyes = random.choice(['oo', 'O O', 'XX', 'x x', '@ @', '><'])
    mouth = random.choice(['-', 'o', 'O', '0', '_', 'u', 'w'])
    arms = random.choice(['\\   /', '/   \\', '\\| |/', '/| |\\', '|   |'])
    body_pattern = random.choice(['|||', '///', '###', '==', '|||', '~~~'])
    
    ghost = f"""
        .-.
       ({eyes})
       | {mouth} |  
      _|_ _|_
    /       \\ 
   {arms}
  {body_pattern}{body_pattern}{body_pattern}
  {body_pattern}{body_pattern}{body_pattern}
  ||   ||   ||
  ||   ||   ||
     '""""""'
    """
    
    return ghost

# Generate a spooky ghost
print(generate_spooky_ghost())
