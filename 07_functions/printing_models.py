import printing_functions as pf


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# function_name(list_name[:]) -> function works with a copy of the list
# doesn't alter the original list
pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)
print(unprinted_designs)  # Showing that the list is intact.
# It's way better to pass the original list, though
