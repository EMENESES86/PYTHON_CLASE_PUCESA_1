# # Estoy definiendo la variable1 num1 = 5
# num1 = 5
# # Estoy definiendo la variable2 num2 = 3
# num2 = 3
# # Estoy imprimiendo la suma de num1 + num2
# print(num1 + num2)

num1 = float(input("Ingrese el primer número: ")) # Se solicita al usuario que ingrese un número
num2 = float(input("Ingrese el segundo número: ")) # Se solicita al usuario que ingrese un número

def suma(num1, num2): # Se define la función suma
    # return num1 + num2 # Se retorna la suma de los dos números
    print("la suma de ",num1,"+",num2,"=",num1 + num2) # Se imprime la suma de los dos números
suma(num1, num2) # Se llama a la función suma

# print("la suma de ",num1,"+",num2,"=",num1 + num2) # Se imprime la suma de los dos números
# print("la resta de ",num1,"-",num2,"=",num1 - num2) # Se imprime la resta de los dos números
# print("la multiplicación de ",num1,"*",num2,"=",num1 * num2) # Se imprime la multiplicación de los dos números
# if num2 == 0: # Si el segundo número es igual a 0
#     print("No se puede dividir por 0") # Se imprime que no se puede dividir por 0
# else:
#     print("la división de ",num1,"/",num2,"=",num1 / num2) # Se imprime la división de los dos números
# print("la potencia de ",num1,"**",num2,"=",num1 ** num2) # Se imprime la potencia de los dos números
# print("la división entera de ",num1,"//",num2,"=",num1 // num2) # Se imprime la división entera de los dos números
# print("el módulo de ",num1,"%",num2,"=",num1 % num2) # Se imprime el módulo de los dos números
# print("la raíz cuadrada de ",num1,"=",num1 ** 0.5) # Se imprime la raíz cuadrada del primer número