from conexao_direta import create_conection, destroy_connection


#aqui é conexão direta sem ORM, dessa forma temos 
 
def insert(con,nome,email,senha):
    cursor=con.cursor()
    sql="INSERT INTO usuario(nome,email,senha) values (%s,%s,%s)"
    valores=(nome, email, senha)
    cursor.execute(sql,valores)
    cursor.close()
    con.commit()
    
def select_tudo(con):
    cursor=con.cursor()
    sql= "SELECT id,nome,email FROM usuario"
    cursor.execute(sql)
    
    
def main():
    con=create_conection("localhost","root","","treinopython")

    insert(con,"nerval","nerval@email","123456")
    select_tudo(con)

    destroy_connection(con)    
    
    
    
    
if __name__== "__main__":
    main()