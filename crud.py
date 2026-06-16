from database import get_connection

def get_users():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "select * from users"
    )

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def create_user(name, email):
    conn = get_connection()

    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            insert into users
            (name, email)
            values
            (%s,%s)
            """,
            (name, email)
        
        )
        
        conn.commit()
        return True
    except Exception:
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        select *
        from users
        where user_id = %s
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user

def get_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        select * from users
        where name ILIKE %s
        """,
        (f"%{name}%",)
    )

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users

def update_user_email(user_id , new_email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        update users
        set email = %s
        where user_id = %s
        """,
        (new_email , user_id)
    )

    if cursor.rowcount == 0:
        conn.commit()
    
        cursor.close()
        conn.close()
        return False
    else:

        conn.commit()
    
        cursor.close()
        conn.close()
        return True

def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        Delete from users
        where user_id = %s
        """,
        (user_id,)
    )

    if cursor.rowcount == 0:
        conn.commit()

        cursor.close()
        conn.close()
        return False
    else:
        
        conn.commit()

        cursor.close()
        conn.close()
        return True
   
