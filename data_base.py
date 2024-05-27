import psycopg2

def Checker_User(User, password):
    conn = psycopg2.connect(host = "localhost", dbname = "Proyecto_Kali", user = "postgres", password = "JorgeCerda1401", port = 5432)
    cur = conn.cursor()

    cur.execute("""SELECT name, id_user FROM users""")
    users = cur.fetchall()

    cur.execute("""SELECT password, id_user FROM passwords""")
    passwords = cur.fetchall()

    for user_info, password_info in zip(users, passwords):
        if User == user_info[0] and password == password_info[0]:
            conn.commit()
            cur.close()
            conn.close()
            return True
        
    conn.commit()
    cur.close()
    conn.close()
    return False
    


    


    