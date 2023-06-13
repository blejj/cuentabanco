saldo_actual = 2000
numero_cuenta = 100300
opcion = 0

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def depositar(self,saldo_depositar):
        self.balance += saldo_depositar #self.balance = self.balance + saldo_depositar

    def datos(self):
        print(f"Bienvenido {nombre} {apellido}, su numero de cuenta es: {numero_cuenta} y tiene un saldo de ${balance}")

    def retirar(self,saldo_retirar):
        self.balance -= saldo_retirar #self.balance = self.balance - saldo_retirar

    def consultar_saldo(self):
        print("Su saldo actual es de: ",self.balance)

usuario = Cliente("Franco","Bleile",numero_cuenta,saldo_actual)

while opcion != 4:
    print("\n----------------Bienvenido al cajero automatico-----------------")
    print("\nOperaciones que puedes realizar:")
    print("\n1- Consultar saldo.")
    print("2- Depositar.")
    print("3- Retirar.")
    print("4- Salir.")

    opcion = int(input("\nQue opcion deseas realizar?"))

    if opcion <= 4 and opcion > 0:
        if opcion == 1:
            usuario.consultar_saldo()
            continue

        elif opcion == 2:
            saldo_depositar = float(input("\nCuando deseas depositar?"))
            if saldo_depositar > 0:
                usuario.depositar(saldo_depositar)
                print("\nDeposito exitoso. Su saldo actual es de: ",usuario.balance)
                continue
            else:
                print("\nNo podes depositar esa cantidad. Vuelve a intentarlo")
                continue
        else:
            saldo_retirar = float(input("Cuando deseas retirar?"))
            if saldo_retirar <= usuario.balance:
                usuario.retirar(saldo_retirar)
                print("Retiro exitoso. Su saldo ahora es de: ",usuario.balance)
                continue

    else:
        print("No elegiste una opcion correcta.")

print("Muchas gracias por seguir confiando en nosotros. Vuelva pronto!")