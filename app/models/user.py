from app.models import get_db_connection

class User:
    @staticmethod
    def create(username, password_hash):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, password_hash) VALUES (?, ?)',
                (username, password_hash)
            )
            conn.commit()
            user_id = cursor.lastrowid
            return user_id
        except sqlite3.IntegrityError:
            return None # 帳號已存在
        finally:
            conn.close()

    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE username = ?', (username,)
        ).fetchone()
        conn.close()
        return user

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        user = conn.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()
        conn.close()
        return user


class Donation:
    @staticmethod
    def create(user_id, amount, message):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO donations (user_id, amount, message) VALUES (?, ?, ?)',
            (user_id, amount, message)
        )
        conn.commit()
        donation_id = cursor.lastrowid
        conn.close()
        return donation_id

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        donations = conn.execute(
            'SELECT * FROM donations WHERE user_id = ? ORDER BY created_at DESC', 
            (user_id,)
        ).fetchall()
        conn.close()
        return donations

    @staticmethod
    def get_all_donations():
        conn = get_db_connection()
        donations = conn.execute(
            '''
            SELECT d.*, u.username 
            FROM donations d 
            JOIN users u ON d.user_id = u.id 
            ORDER BY d.created_at DESC
            '''
        ).fetchall()
        conn.close()
        return donations
