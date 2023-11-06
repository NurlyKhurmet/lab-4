try:
    cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

    car_data = {}

    for manufacturer, model in cars_list:
        if manufacturer in car_data:
            car_data[manufacturer].append(model)
        else:
            car_data[manufacturer] = [model]

    for manufacturer, models in car_data.items():
        print(f"{manufacturer} {len(models)}")
        for model in models:
            print(f"- {model}")

except ValueError:
    print("Bad Input")
