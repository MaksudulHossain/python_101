# style -1 
def make_car(manufacterer, modelname='corolla',**kwargs):
    kwargs['manufacturer'] = manufacterer
    kwargs['model name'] = modelname
    return kwargs

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)