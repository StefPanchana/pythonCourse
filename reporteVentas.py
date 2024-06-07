import pandas as pd

def leer_datos_excel(archivo_entrada):
    #leer los datos de un archivo excel
    return pd.read_excel(archivo_entrada)

def procesar_datos_ventas(df:pd.DataFrame):
    #Procesar los datos de las ventas para obtener metricas claves
    resumen_ventas= df.groupby("ID Producto").agg(
        Total_Ventas=("Cantidad", "sum"),
        Total_Ingreso=("Ingreso", "sum"),
        Numero_Transacciones=("ID Producto", "count"),
        Fecha_Ultima_Venta=("Fecha", "max")
    ).reset_index()
    return resumen_ventas

def filtrar_datos(resumen_ventas, umbral_ingreso=1000):
    #Filtrar los productos que sean menores un umbral de ingreso
    return resumen_ventas[resumen_ventas("Total_Ingreso")>= umbral_ingreso]

def guardar_datos_excel(df, archivo_salida):
    #Guardar los datos en un archivo excel
    df.to_excel(archivo_salida, index=False)

def generar_reporte_ventas(archivo_entrada, archivo_salida):
    #Toma los datos de entrada, genera el reporte de ventas y lo guarda en un nuevo archivo excel
    
    #Lee los datos
    df= leer_datos_excel(archivo_entrada)

    #Calcular ingreso total por venta
    df["Ingreso"]= df["Cantidad"] * df["Precio Unitario"]

    #Procesar los datos para crear el resumen de ventas
    resumen_ventas= procesar_datos_ventas(df)

    #Filtra los datos para incluir solo productos con ingresos superios al umbral de ingresos
    resumen_ventas_filtrado= filtrar_datos(resumen_ventas)

    #Guardar el reporte en un archivo excel nuevo
    guardar_datos_excel(resumen_ventas_filtrado, archivo_salida)

generar_reporte_ventas("","")
