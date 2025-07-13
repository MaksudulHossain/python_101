def make_car(manufacterer, modelname,**kwargs):
    kwargs['manufacturer'] = manufacterer
    kwargs['model name'] = modelname
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)


# method -2 
def make_car(manufacturer, model, **features):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(features)
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)