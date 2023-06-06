"""probando para calculadora"""
recetas = {'RODILLA':['atun', 'jamón serrano','salami', 'pavo','queso'], 'KATSU SANDO':['crispy meat','signature ton katsu sauce'], 'TRIPLE SANDWICH':['3 or 4 slices of plain', 'white sandwich bread','mayonnaise','fresh avocados','tomatoes','slices of hard-boiled egg'] }
print (f'****************** THE BIG BREAD SA *****************')
print()
print (f'****************** CALCULADORA DE INSUMOS *****************\n')
receta_necesaria=input(f' Ingrese, por favor, la receta que desea producir: \n').upper()
cantidad_receta=int (input(f' Ingrese, por favor, la cantidad que desea producir: \n'))

if receta_necesaria in recetas:
    insumos_receta_necesaria = recetas[receta_necesaria]
    print(f'Para poder producir {cantidad_receta} {receta_necesaria}, los insumos y cantidades requeridas son: {insumos_receta_necesaria}')
else:
    print(f'La receta {receta_necesaria} no se encuentra en el diccionario.')