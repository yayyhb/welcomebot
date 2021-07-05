import sqlite3

def verlosung_add (group_id, user_id, username, firstname, text_msg):
    con = sqlite3.connect('abb.db')
    cur = con.cursor()

    test_exists = "SELECT count(*) FROM verlosung WHERE user_id = '" + user_id + "' AND group_id = '" + group_id + "'"
    user_exists = cur.execute(test_exists)
    user_exists = cur.fetchone()[0]

    test_exists = "SELECT count(*) FROM verlosung WHERE joy_name = '" + text_msg + "' AND group_id = '" + group_id + "'"
    joy_exists = cur.execute(test_exists)
    joy_exists = cur.fetchone()[0]

    if not user_exists and not joy_exists:
        sql = "INSERT INTO verlosung (group_id, user_id, user_name, joy_name) VALUES (?, ?, ?, ?)"
        cur.execute(sql, (group_id, user_id, username, text_msg))
        message = firstname + ", dein Joy Name '" + text_msg[:2] + "****' wurde unter dem Telegramm Benutzer '@" + username[:2] + "*****' für die Verlosung gespeichert. Viel Glück!"
        con.commit()
        con.close()

    else:
        message = firstname + ", Du kannst Dich nur einmal für die Verlosung registrieren. Bei Problemen wende Dich bitte an die Admins."

    return message

def verlosung_getWinner(chat_id):
    chat_id = str(chat_id)
    con = sqlite3.connect('abb.db')
    cur = con.cursor()

    sql = "SELECT user_name, joy_name FROM verlosung WHERE group_id = '" + chat_id + "' ORDER BY RANDOM() LIMIT 1"
    cur.execute(sql)
    winner = cur.fetchall()
    
    if winner:
        user_name = str(winner[0][0])
        joy_name = str(winner[0][1])
        message = "Und der Gewinner ist @" + user_name + " mit dem Joy Namen '" + joy_name + "'. Herzlichen Glückwunsch!"
        con.close()

    else:
        message = "Es ist aktuell niemand für eine Verlosung angemeldet"

    return message

def verlosung_purge(chat_id):
    chat_id = str(chat_id)
    con = sqlite3.connect('abb.db')
    cur = con.cursor()
    print("Teilnehmer gelöscht:")
    print("Chat ID: " + chat_id)
    cur.execute("DELETE FROM verlosung WHERE group_id = '" + chat_id + "'")
    con.commit()
    con.close()
    message = "Die Teilnehmer der Verlosung in dieser Gruppe wurden gelöscht."
    return message
