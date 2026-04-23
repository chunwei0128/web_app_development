from flask import render_template, request, redirect, url_for, session
from app.routes import auth_bp

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    處理會員登入與註冊邏輯。
    GET: 回傳 login.html 顯示表單。
    POST: 驗證帳號密碼或建立新帳號，成功後將 user_id 寫入 session，並重導向。
    """
    pass

@auth_bp.route('/logout', methods=['GET'])
def logout():
    """
    處理會員登出。
    清除 session 中的 user_id，並重導向至首頁。
    """
    pass
