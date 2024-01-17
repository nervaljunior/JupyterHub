import mysql.connector as con 


def create_conection(host,name,senha,banco):
    return con.connect(host=host,user=name,password=senha,database=banco)


def destroy_connection(c):
    return c.close()