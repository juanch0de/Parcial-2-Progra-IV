from modelo.Cliente import Cliente

clientes = []

def crear_cliente(nombre: str, ID: int) -> Cliente:
    cliente = Cliente(nombre, ID)
    clientes.append(cliente)
    return cliente

def actualizar_cliente(ID: int, nombre: str) -> bool:
    for cliente in clientes:
        if cliente.ID == ID:
            cliente.nombre = nombre
            return True
    return False

def eliminar_cliente(ID: int) -> bool:
    global clientes
    original_len = len(clientes)

    clientes = [cliente for cliente in clientes if cliente.ID != ID]

    if len(clientes) < original_len:
        return True
    else:
        return False

def mostrar_clientes() -> list:
    return clientes
