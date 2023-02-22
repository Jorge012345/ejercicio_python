class Programa():
    productos = {1:'Pantalones', 2:'Camisas', 3:'Corbatas', 4:'Casacas'}
    precios = {1:200.00, 2:120.00, 3:50.00, 4:350.00}
    stock = {1:50, 2:45, 3:30, 4:15}
    count = len(productos)
    def __init__(self):
        pass
    
    def get_key(self, val, dic):
        for key, value in dic.items():
            if val == value:
                return key
        return None

    def agregar(self):
        try:
            self.count += 1
            nombre_producto = input("Ingrese el nombre: ")
            precio = float(input("Ingrese el precio: "))
            stock = int(input("Ingrese el stock: "))
            self.productos[self.count] = nombre_producto
            self.precios[self.count] = precio
            self.stock[self.count] = stock
            print("Agregado con exito.")
        except Exception as e:
            print("Error: ",e)

    def eliminar(self):
        print("Eliminando por nombre de producto")
        try:
            
            nombre_producto = input("Ingrese el nombre: ")
            key = self.get_key(nombre_producto, self.productos)
            if key:
                del self.productos[key]
                del self.precios[key]
                del self.stock[key]
                self.count -= 1
                print("Eliminado con exito.")
            else:
                print("No existe el nombre ingresado.")

        except Exception as e:
            print("Error: ",e)

    def actualizar(self):
        print("Actualizando por nombre de producto")
        try:
            nombre_producto = input("Ingrese el nombre: ")
            key = self.get_key(nombre_producto, self.productos)
            if key:
                nombre_producto = input("Ingrese el nuevo nombre: ")
                precio = float(input("Ingrese el nuevo precio: "))
                stock = int(input("Ingrese el nuevo stock: "))
                self.productos[key] = nombre_producto
                self.precios[key] = precio
                self.stock[key] = stock
                print("Actualizado con exito.")
            else:
                print("No existe el nombre ingresado.")

        except Exception as e:
            print("Error: ",e)

    def mostrar(self):
        for clave, valor in self.productos.items():
            cadena = "{:<10}{:<15}{:<10}{:<10}".format(clave, valor, self.precios[clave], self.stock[clave])
            print(cadena)

    def menu(self):
        while True:
            
            print("========================================")
            print("Lista de Productos:")
            print("========================================")
            self.mostrar()
            print("========================================")
            opc = int(input("\n[1] Agregar, [2] Eliminar, [3] Actualizar, [4] Salir. Elija opción: "))
            if opc == 1:
                self.agregar()
            elif opc == 2:
                self.eliminar()
            elif opc == 3:
                self.actualizar()
            elif opc == 4:
                break

if __name__ == '__main__':
    obj = Programa()
    obj.menu()