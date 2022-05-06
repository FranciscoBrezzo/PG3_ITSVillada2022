import pymysql



while True:
    connection = pymysql.connect( host='localhost', user= 'bdi', passwd='pepe1234', db='Ej_Exceptions')
    cur = connection.cursor()
    code = input("Ingrese el comando que desees: ")
    try:
        cur.execute(code)
    except pymysql.err.ProgrammingError as a:
        print(a,"Por favor utilice la sintaxis correcta")
    except pymysql.err.OperationalError as b:
        print(b,"Por favor utilice la sintaxis correcta")