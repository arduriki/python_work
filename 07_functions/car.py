def make_car(manufacturer, model_name, **features):
    features['brand'] = manufacturer
    features['model'] = model_name
    return features


car = make_car('subaru', 'outback',
               color='blue',
               tow_package=True)

print(car)