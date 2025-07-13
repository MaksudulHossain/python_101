def print_models(unprinted_designs, completed_models):
    # modify list in function
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been printed")
    for completed_model in completed_models:
        print(completed_model)
