# Este programa permite crear datos aleatorios y los guarda en un archivo con extension
# .sql para que sea cargado a la base de datos.
import inspect, os
import random

cantidad_registros = int(input("Cuantos registros desea?  "))
nombre_archivo = 'personas'
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

ruta = os.path.dirname(__file__)
archivo_sql = open(ruta + '/' + nombre_archivo + '.sql', 'w+')

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

for numero in range(0, cantidad_registros):
    nombre_aleatorio =  random.choice(nombres)
    fecha_aleatorio = generar_fecha_aleatoria(1995, 2000)
    apellido_paterno_aleatorio =  random.choice(apellidos)
    apellido_materno_aleatorio =  random.choice(apellidos)
    socio_aleatorio = random.choice(['si', 'no'])
    sql = """INSERT INTO `%s`
            (`nombre`, `apellido_paterno`, `apellido_materno`, `fecha_nac`, `tel`, `socio`)
            VALUES ('%s', '%s', '%s', '%s', 'TELEFONO', '%s');
            """ %(nombre_tabla, nombre_aleatorio, apellido_paterno_aleatorio, apellido_materno_aleatorio,
            fecha_aleatorio, socio_aleatorio)
    archivo_sql.write(sql + '\n')
