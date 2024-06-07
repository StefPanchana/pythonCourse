import pandas as pd

# Funcion de leer inventario
def leer_inventario(archivo_inventario):
    # Lee los datos de un archivo excel
    return pd.read_excel(archivo_inventario)

# Funcion de leer Venta
def leer_ventas(archivo_ventas):
    # Lee los datos de un archivo excel
    return pd.read_excel(archivo_ventas)

def actualizar_inventario(df_inventario, df_ventas):
    # Actualizar inventario en base a las ventas
    for index, row in df_ventas.iterrows():
        producto_id = row['ID Producto']
        cantidad_vendida = row['Cantidad']

        if producto_id in df_inventario["ID Producto"].values:
            # Buscar el producto en el inventario
             df_inventario.loc[df_inventario["ID Producto"] == producto_id, "Cantidad de Stock"]-= cantidad_vendida
    return df_inventario

def generar_alertas(df_inventario):
    # Generar alertas para productos con stock por debajo del minimo
    alertas = df_inventario[df_inventario["Cantidad de Stock"] < df_inventario["Cantidad Minima"]]
    return alertas

def guardar_inventario_actualizado(df_inventario, archivo_salida):
    # Guardar el inventario actualizado en un archivo excel
    df_inventario.to_excel(archivo_salida, index=False)

def guardar_alertas(df_alertas, archivo_alertas):
    # Guardar las alertas en un archivo excel
    if not df_alertas.empty:
        df_alertas.to_excel(archivo_alertas, index=False)
    else:
        with pd.ExcelWriter(archivo_alertas) as writer:
            df_alertas.to_excel(writer, index=False)

def gestionar_inventario(archivo_inventario, archivo_ventas, archivo_inventario_actualizado, archivo_alertas):
    # Leer inventario y ventas
    df_inventario = leer_inventario(archivo_inventario)
    df_ventas = leer_ventas(archivo_ventas)

    #Actualizar inventario en base a las ventas
    df_inventario_actualizado = actualizar_inventario(df_inventario, df_ventas)

    #Generar alertas
    df_alertas = generar_alertas(df_inventario_actualizado)

    #Guardar inventario actualizado y alertas
    guardar_inventario_actualizado(df_inventario_actualizado, archivo_inventario_actualizado)
    guardar_alertas(df_alertas, archivo_alertas)

gestionar_inventario("","","","")

