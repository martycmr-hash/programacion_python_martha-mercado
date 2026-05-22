# fase 5- problema 2

#matriz del menú: [nombre del producto, categoria, precio base]

menu = [
    ["pechuga", "asado", 20000],
    ["costillas BBQ", "asado", 25000],
    ["hamburguesa", "comida rapida", 15000],
    ["pizza", "comida rapida", 20000],
    ["limonada de cereza", "bebida", 7000],
    ["limonada de maracuya", "bebida", 7000]
]

#funcion para calcular el precio final del producto
def calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral):

# aplicar el descuento del 15% si el producto esta en la categoria objetivo y su precio base es yaor al umbral
   if categoria == categoria_objetivo and precio_base > umbral:
    descuento = precio_base * 0.15
    precio_final = precio_base - descuento

   else:
    precio_final = precio_base

   return precio_final

#categoria objetivo y umbral de descuento
categoria_objetivo = "comida rapida"
umbral = 14000

#calcular el precio final de cada producto en el menu
print("PROMOCIONES DEL MENU:")

for producto in menu:
    nombre, categoria, precio_base = producto
    precio_final = calcular_precio_final(categoria, precio_base, categoria_objetivo, umbral)

    if precio_final < precio_base:
        print(nombre, "-", categoria, "- precio base $", precio_base, "- precio final $", precio_final)
    else:
       print(nombre, "-", categoria, "- precio base $", precio_base)
