from flask import Blueprint

# 建立各個模組的 Blueprint 物件
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
fortune_bp = Blueprint('fortune', __name__, url_prefix='/fortune')
donation_bp = Blueprint('donation', __name__, url_prefix='/donation')

# 歷史紀錄可以獨立一個 Blueprint 或是掛在 fortune 下，這裡依據路由表設計獨立的 prefix 或者放在根目錄
history_bp = Blueprint('history', __name__, url_prefix='/history')

# 主頁 Blueprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    處理首頁請求。
    回傳 index.html 模板。
    """
    pass
