"""Print out all the melons in our inventory."""


from melons import melons
 

def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melon_name, attributes in melons.items():
        print(melon_name.title())

        for attribute, value in attributes.items():
            print(f'{attribute}: {value}')

print_melon(melons)

    
