from app.models import get_db_connection

class Poem:
    @staticmethod
    def get_random():
        conn = get_db_connection()
        poem = conn.execute(
            'SELECT * FROM poems ORDER BY RANDOM() LIMIT 1'
        ).fetchone()
        conn.close()
        return poem

    @staticmethod
    def get_by_id(poem_id):
        conn = get_db_connection()
        poem = conn.execute(
            'SELECT * FROM poems WHERE id = ?', (poem_id,)
        ).fetchone()
        conn.close()
        return poem

    @staticmethod
    def get_all():
        conn = get_db_connection()
        poems = conn.execute('SELECT * FROM poems ORDER BY poem_number ASC').fetchall()
        conn.close()
        return poems


class History:
    @staticmethod
    def create(user_id, poem_id, question):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO history (user_id, poem_id, question) VALUES (?, ?, ?)',
            (user_id, poem_id, question)
        )
        conn.commit()
        history_id = cursor.lastrowid
        conn.close()
        return history_id

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        histories = conn.execute(
            '''
            SELECT h.id, h.question, h.created_at, p.poem_number, p.poem_text, p.explanation 
            FROM history h
            JOIN poems p ON h.poem_id = p.id
            WHERE h.user_id = ?
            ORDER BY h.created_at DESC
            ''', 
            (user_id,)
        ).fetchall()
        conn.close()
        return histories
