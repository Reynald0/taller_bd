# Este programa permite crear datos aleatorios y los guarda en un archivo con extension
# .sql para que sea cargado a la base de datos.
import inspect, os
import random

nombre_tabla = "personas"
nombres = [ 'Isabella', 'Daniel', 'Olivia', 'David', 'Alexis', 'Gabriel',
            'Sofia', 'Benjamin', 'Victoria', 'Samuel', 'Amelia', 'Lucas',
            'Alexa', 'Angel', 'Julia', 'Jose', 'Camila', 'Adrian', 'Alexandra',
            'Sebastian', 'Maya', 'Xavier', 'Andrea', 'Juan', 'Ariana', 'Luis',
            'Maria', 'Diego', 'Eva', 'Oliver', 'Angelina', 'Carlos', 'Valeria',
            'Jesus','Natalia', 'Alex', 'Isabel', 'Max', 'Sara', 'Alejandro',
            'Liliana', 'Antonio', 'Adriana', 'Miguel', 'Juliana', 'Victor',
            'Gabriela', 'Joel', 'Daniela', 'Santiago', 'Valentina', 'Elias',
            'Lila',	'Ivan', 'Vivian', 'Oscar', 'Nora', 'Leonardo', 'Angela',
            'Eduardo', 'Elena', 'Alan', 'Clara', 'Nicolas', 'Eliana', 'Jorge',
            'Alana', 'Omar', 'Miranda', 'Paul', 'Amanda', 'Andres', 'Diana',
            'Julian', 'Ana', 'Josue', 'Penelope', 'Roman', 'Aurora', 'Fernando',
            'Alexandria', 'Javier', 'Lola', 'Abraham', 'Alicia', 'Ricardo',
            'Amaya', 'Francisco', 'Alexia', 'Cesar', 'Jazmin', 'Mario', 'Mariana',
            'Manuel', 'Alina', 'Edgar', 'Lucia', 'Alexis', 'Fatima', 'Israel',
            'Ximena', 'Mateo', 'Laura', 'Hector', 'Cecilia', 'Sergio', 'Alejandra',
            'Emiliano', 'Esmeralda', 'Simon', 'Veronica', 'Rafael', 'Daniella',
            'Martin', 'Miriam', 'Marco', 'Carmen', 'Roberto', 'Iris', 'Pedro',
            'Guadalupe', 'Emanuel', 'Selena', 'Abel', 'Fernanda', 'Ruben', 'Angelica',
            'Fabian', 'Emilia', 'Emilio', 'Lia', 'Joaquin', 'Tatiana', 'Marcos',
            'Monica', 'Lorenzo', 'Carolina','Armando', 'Jimena', 'Adan', 'Dulce',
            'Raul', 'Talia', 'Julio', 'Estrella', 'Enrique', 'Brenda', 'Gerardo',
            'Lilian', 'Pablo', 'Paola', 'Jaime', 'Serena', 'Saul', 'Celeste',
            'Esteban', 'Viviana', 'Gustavo', 'Elisa', 'Rodrigo', 'Melina', 'Arturo',
            'Gloria', 'Mauricio', 'Claudia', 'Orlando', 'Sandra', 'Hugo', 'Marisol',
            'Salvador', 'Asia', 'Alfredo', 'Ada', 'Maximiliano', 'Rosa', 'Ramon',
            'Isabela', 'Ernesto', 'Regina', 'Tobias', 'Elsa', 'Abram', 'Perla',
            'Noe', 'Raquel', 'Guillermo', 'Virginia', 'Ezequiel', 'Patricia', 'Lucian',
            'Linda', 'Alonzo', 'Marina', 'Felipe', 'Leila', 'Matias', 'America',
            'Tomas', 'Mercedes', 'Jairo']

apellidos = ['Alirio', 'Suarez', 'Cordero', 'De Dios', 'De La Cruz', 'Alvarez',
            'Jimenez', 'Contreras', 'Sanchez', 'Sixto', 'Herrera', 'Villegas']

destinos = ['Balancan', 'Nacajuca', 'Macuspana', 'Tacotalpa', 'Centro',
            'Emiliano Zapata', 'Teapa', 'Huimanguillo', 'Cardenas', 'Comalcalco']

ruta = os.path.dirname(__file__)

def generar_fecha_aleatoria(anio_inicio, anio_final):
    anio_aleatorio = random.randint(anio_inicio, anio_final)
    mes_aleatorio = random.randint(1, 12)
    dia_aleatorio = random.randint(1, 30)

    if mes_aleatorio == 2 and dia_aleatorio > 28:
        dia_aleatorio = 28

    if mes_aleatorio <= 9 and dia_aleatorio <= 9:
        mes_aleatorio = '0' + str(mes_aleatorio)
        dia_aleatorio = '0' + str(dia_aleatorio)
        fecha_nac_aleatorio = '%d-%s-%s' %(anio_aleatorio, mes_aleatorio, dia_aleatorio)
    elif mes_aleatorio <= 9:
        mes_aleatorio = '0' + str(mes_aleatorio)
        fecha_nac_aleatorio = '%d-%s-%d' %(anio_aleatorio, mes_aleatorio, dia_aleatorio)
    elif dia_aleatorio <= 9:
        dia_aleatorio = '0' + str(dia_aleatorio)
        fecha_nac_aleatorio = '%d-%d-%s' %(anio_aleatorio, mes_aleatorio, dia_aleatorio)
    else:
        fecha_nac_aleatorio = '%d-%d-%d' %(anio_aleatorio, mes_aleatorio, dia_aleatorio)

    return fecha_nac_aleatorio


def generar_telefono_aleatorio():
    numero = '99'
    for number in range(4):
        numero += str(random.randint(10,99))
    return numero

def generar_hora_aleatoria():
    hora = random.randint(1,24)
    minuto = random.randint(1,59)
    segundo = random.randint(1,59)

    return '%d:%d:%d' %(hora,minuto,segundo)


def generar_persona(archivo):
    nombre_aleatorio =  random.choice(nombres)
    fecha_aleatorio = generar_fecha_aleatoria(1995, 2000)
    apellido_paterno_aleatorio =  random.choice(apellidos)
    apellido_materno_aleatorio =  random.choice(apellidos)
    telefono_aleatorio = generar_telefono_aleatorio()
    socio_aleatorio = random.choice(['si', 'no'])
    sql = """INSERT INTO `personas`
            (`nombre`, `apellido_paterno`, `apellido_materno`, `fecha_nac`, `tel`, `socio`)
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s');
            """ %(nombre_aleatorio, apellido_paterno_aleatorio, apellido_materno_aleatorio,
            fecha_aleatorio, telefono_aleatorio, socio_aleatorio)
    archivo.write(sql + '\n')

def generar_barco(archivo):
    nombre_aleatorio =  random.choice(nombres)
    amarre_aleatorio = random.randint(1, 2000)
    cuota_aleatoria = random.uniform(500.0, 8000.0)
    sql = """INSERT INTO `barcos` (`nombre`, `numero_amarre`, `cuota_pago`)
            VALUES ('%s', '%d', '%.2f');
            """ %(nombre_aleatorio, amarre_aleatorio, cuota_aleatoria)
    archivo.write(sql + '\n')

def generar_salidas(archivo):
    #CUIDADO pueden duplicarse
    personas_id_persona_aleatorio = random.randint(1, 20)
    barcos_matricula_aleatorio = random.randint(1, 20)
    #CUIDADO pueden duplicarse
    fecha_aleatorio = generar_fecha_aleatoria(1995, 2020)
    hora_aleatoria = generar_hora_aleatoria()
    destino_aleatorio = random.choice(destinos)
    sql = """INSERT INTO `barcos_salidas` (`personas_id_persona`, `barcos_matricula`, `fecha`, `hora`, `destino`)
            VALUES ('%d', '%d', '%s', '%s', '%s');
            """%(personas_id_persona_aleatorio, barcos_matricula_aleatorio, fecha_aleatorio, hora_aleatoria, destino_aleatorio)
    archivo.write(sql + '\n')

def generar_sql(numero_registros):
    persona_sql = open(ruta + '/personas.sql', 'w+')
    barco_sql = open(ruta + '/barcos.sql', 'w+')
    barco_salida_sql = open(ruta + '/barcos_salidas.sql', 'w+')
    for numero in range(numero_registros):
        generar_persona(persona_sql)
        generar_barco(barco_sql)
        generar_salidas(barco_salida_sql)

cantidad_registros = int(input("Cuantos registros desea?  "))
generar_sql(cantidad_registros)
