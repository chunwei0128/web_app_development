from flask import render_template, request, redirect, url_for, session
from app.routes import fortune_bp, history_bp

# -----------------
# 抽籤相關路由
# -----------------
@fortune_bp.route('/draw', methods=['GET'])
def draw_page():
    """
    顯示求籤與擲筊介面。
    回傳 draw.html 模板。
    """
    pass

@fortune_bp.route('/draw/result', methods=['POST'])
def draw_result():
    """
    處理擲筊完成後的抽籤邏輯。
    隨機取得一首籤詩，並將使用者的問題暫存，最後重導向至籤詩結果頁面。
    """
    pass

@fortune_bp.route('/result/<int:poem_id>', methods=['GET'])
def show_result(poem_id):
    """
    顯示籤詩結果。
    根據 poem_id 從資料庫取得籤詩原文與白話文解釋，回傳 result.html 模板。
    """
    pass

# -----------------
# 歷史紀錄相關路由
# -----------------
@history_bp.route('/', methods=['GET'])
def history_list():
    """
    顯示使用者的歷史抽籤紀錄。
    需驗證登入狀態，回傳 history.html 模板。
    """
    pass

@history_bp.route('/add', methods=['POST'])
def history_add():
    """
    將剛抽完的籤詩存入歷史紀錄。
    需驗證登入狀態，接收 poem_id，寫入 history 資料表，並重導向至歷史紀錄頁面。
    """
    pass
