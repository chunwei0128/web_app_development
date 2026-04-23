import sqlite3
import os

def get_db_connection():
    """
    建立並回傳與 SQLite 的資料庫連線。
    預設取得 dictionary 格式的回傳值，方便以欄位名稱存取。
    """
    # 確保資料庫路徑是正確的 (相對於專案根目錄)
    db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'instance', 'database.db')
    
    # 若 instance 目錄不存在則自動建立
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn
