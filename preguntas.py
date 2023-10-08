"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    cantidad_de_filas = tbl0.shape[0]
    #return cantidad_de_filas
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    return cantidad_de_filas


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    return tbl0.shape[1]


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra en la columna `_c1` de tbl0.tsv?
    """
    # Utiliza value_counts() para contar los valores únicos en la columna _c1
    cantidad_por_letra = tbl0['_c1'].value_counts().sort_index()
    return cantidad_por_letra



def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    return tbl0.groupby('_c1')['_c2'].mean()


def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    return tbl0.groupby('_c1')['_c2'].max()


def pregunta_06():
    """
    Retorne una lista con los valores únicos de la columna _c4 en mayúsculas
    y ordenados alfabéticamente.
    """
    # Obtener valores únicos en la columna _c4
    valores_unicos = tbl1['_c4'].unique()
    
    # Convertir los valores a mayúsculas y ordenar alfabéticamente
    valores_unicos_mayusculas = sorted([valor.upper() for valor in valores_unicos])
    
    return valores_unicos_mayusculas


def pregunta_07():
    """
    Calcule la suma de _c2 por cada letra en la columna _c1 en tbl0.tsv.
    """
    # Agrupar por la columna _c1 y calcular la suma de _c2 para cada grupo
    suma_por_letra = tbl0.groupby('_c1')['_c2'].sum()
    return suma_por_letra



def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44
    """
    # Cargamos el archivo tbl0.tsv
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

    # Calculamos la suma de las columnas _c0 y _c2 y la almacenamos en una nueva columna 'suma'
    tbl0['suma'] = tbl0['_c0'] + tbl0['_c2']

    # Devolvemos el DataFrame con la columna 'suma' agregada
    return tbl0


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998
    """
    # Cargamos el archivo tbl0.tsv
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")

    # Intentamos convertir la columna _c3 al formato de fecha y extraer el año,
    # pero manejamos las fechas inválidas asignando un valor nulo (None)
    tbl0['year'] = tbl0['_c3'].apply(lambda x: x.split("-")[0])

    # Devolvemos el DataFrame con la columna 'year' agregada
    return tbl0


def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    return tbl0.sort_values(by=['_c2']).groupby('_c1').apply(lambda x: ":".join(x['_c2'].astype(str))).to_frame('_c2')


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    

    # Definimos una función personalizada para concatenar los valores en una lista separada 
    def concatenate_values(series):
        return ','.join(sorted(series.unique()))

    resultado = tbl1.groupby('_c0')['_c4'].apply(concatenate_values).reset_index()

    return resultado


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
   
    # Concatenamos los valores de _c5a y _c5b en un formato "clave:valor"
    tbl2['_c5'] = tbl2.apply(lambda x: f"{x['_c5a']}:{x['_c5b']}", axis=1)

    # Agrupamos y concatenamos los valores por _c0 respetando el orden original
    resultado = tbl2.groupby('_c0', sort=False)['_c5'].apply(lambda x: ','.join(x)).reset_index()

    # Ordenamos alfabéticamente la columna _c5
    resultado['_c5'] = resultado['_c5'].apply(lambda x: ','.join(sorted(x.split(','))))

    return resultado




def pregunta_13():
 # Realizar un merge entre tbl10 y tbl12 utilizando _c0 como clave
    merged = pd.merge(tbl0, tbl2, left_on='_c0', right_on='_c0')
    
    # Calcular la suma de _c5b por cada valor en _c1 y ordenar el resultado
    result = merged.groupby('_c1')['_c5b'].sum()
    
    return result
