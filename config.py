def structure_config(choice):
    if choice == 1: 
        layer_configs = [
            {"layer": 0, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 1, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 8, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 9, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 10, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 11, "r": 8, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==2: 
        layer_configs = [
        {"layer": 0, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 1, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 6, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 7, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 8, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 9, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 10, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 11, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==3: 
        layer_configs = [
            {"layer": 0, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 1, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 5, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 8, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 9, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 10, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 11, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==4: 
        layer_configs = [
        {"layer": 0, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 1, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 4, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 5, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 8, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 9, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 10, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
        {"layer": 11, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==5: 
        layer_configs = [
        {"layer": 0, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
        {"layer": 1, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
        {"layer": 2, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
        {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
        {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 8, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
        {"layer": 9, "r": 12, "lora_alpha": 4, "lora_dropout": 0.12, "target": ['query']},
        {"layer": 10, "r": 12, "lora_alpha": 4, "lora_dropout": 0.12, "target": ['query']},
        {"layer": 11, "r": 12, "lora_alpha": 4, "lora_dropout": 0.12, "target": ['query']}]
    elif choice==6: 
        layer_configs = [
            {"layer": 0, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 1, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 2, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 8, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 9, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 10, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 11, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==7: 
        layer_configs = [
            {"layer": 0, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 1, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 5, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 8, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 9, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 10, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 11, "r": 12, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==8: 
        layer_configs = [
            {"layer": 0, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 1, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 5, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 8, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 9, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 10, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']},
            {"layer": 11, "r": 16, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query']}]
    elif choice==9:
        layer_configs = [
            {"layer": 0, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 1, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 2, "r": 2, "lora_alpha": 4, "lora_dropout": 0.03, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 6, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 7, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 8, "r": 8, "lora_alpha": 4, "lora_dropout": 0.075, "target": ['query']},
            {"layer": 9, "r": 10, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query','value']},
            {"layer": 10, "r": 10, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query','value']},
            {"layer": 11, "r": 10, "lora_alpha": 4, "lora_dropout": 0.1, "target": ['query','value']}]
    else:
        layer_configs = [
            {"layer": 0, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 1, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 2, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 3, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 4, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 5, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 6, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 7, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 8, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 9, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 10, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']},
            {"layer": 11, "r": 4, "lora_alpha": 4, "lora_dropout": 0.05, "target": ['query']}]
    
    return layer_configs
    