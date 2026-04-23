from flask import render_template, request, redirect, url_for, session
from app.routes import donation_bp

@donation_bp.route('/donate', methods=['GET', 'POST'])
def donate():
    """
    處理香油錢捐贈。
    GET: 顯示 donate.html 捐款表單。
    POST: 接收捐款金額與祈福語，寫入 donations 資料表，重導向至感謝頁面。
    """
    pass

@donation_bp.route('/thanks', methods=['GET'])
def thanks():
    """
    顯示捐款成功感謝頁面。
    回傳 thanks.html 模板。
    """
    pass
