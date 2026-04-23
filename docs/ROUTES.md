# 路由與頁面設計 - 線上算命系統

本文件根據產品需求與流程圖，定義系統的 Flask 路由 (Routes)、對應的 HTTP 方法與 Jinja2 模板。

## 1. 路由總覽表格

| 功能區塊 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
|---|---|---|---|---|
| **首頁** | `GET` | `/` | `index.html` | 顯示網站首頁與服務介紹 |
| **會員系統** | `GET` | `/auth/login` | `login.html` | 顯示登入與註冊表單 |
| | `POST` | `/auth/login` | — | 接收表單並處理會員登入或註冊，成功後重導向首頁或歷史紀錄 |
| | `GET` | `/auth/logout` | — | 處理會員登出，清除 Session 並重導向首頁 |
| **線上抽籤** | `GET` | `/fortune/draw` | `draw.html` | 顯示求問事項表單與擲筊介面 |
| | `POST` | `/fortune/draw/result` | — | 接收求問內容與確認擲筊成功，隨機抽取籤詩，重導向至結果頁面 |
| | `GET` | `/fortune/result/<int:poem_id>` | `result.html` | 顯示對應籤號的籤詩原文與白話文解析 |
| **歷史紀錄** | `GET` | `/history` | `history.html` | 列出目前登入會員的所有過往抽籤紀錄 |
| | `POST` | `/history/add` | — | 將當次抽籤結果存入資料庫，並重導向至歷史紀錄頁面 |
| **香油錢** | `GET` | `/donation/donate` | `donate.html` | 顯示香油錢捐贈表單 |
| | `POST` | `/donation/donate` | — | 處理捐款邏輯（模擬），成功後重導向至感謝頁面 |
| | `GET` | `/donation/thanks` | `thanks.html` | 顯示捐款成功的感謝訊息 |

## 2. 每個路由的詳細說明

### 首頁 (`/`)
- **輸入**: 無
- **處理邏輯**: 直接渲染首頁。
- **輸出**: `index.html`

### 會員登入/註冊 (`/auth/login`)
- **輸入**: `username`, `password`, `action` (login 或 register)
- **處理邏輯**: 
  - GET: 顯示表單。
  - POST: 若 `action == login`，驗證密碼；若 `action == register`，建立新帳號。成功則將 `user_id` 存入 Flask Session。
- **輸出**: 成功則重導向 `/` 或 `/history`，失敗則在 `login.html` 顯示錯誤訊息。

### 會員登出 (`/auth/logout`)
- **處理邏輯**: 清除 Flask Session 內的 `user_id`。
- **輸出**: 重導向至 `/`。

### 抽籤頁面 (`/fortune/draw`)
- **輸入**: 無
- **處理邏輯**: 顯示使用者求籤介面，前端負責擲筊動畫。
- **輸出**: `draw.html`

### 抽籤執行 (`/fortune/draw/result`)
- **輸入**: `question` (求問事項，選填)
- **處理邏輯**: 呼叫 `Poem.get_random()` 隨機取得一首籤詩，並將 `question` 存放在 Session 暫存，以便存檔時使用。
- **輸出**: 重導向至 `/fortune/result/<poem_id>`。

### 籤詩結果 (`/fortune/result/<poem_id>`)
- **輸入**: URL 參數 `poem_id`
- **處理邏輯**: 呼叫 `Poem.get_by_id(poem_id)` 取得資料。
- **輸出**: `result.html`，並在頁面上提供「儲存此籤」的按鈕。

### 歷史紀錄列表 (`/history`)
- **輸入**: 需先登入 (從 Session 取得 `user_id`)
- **處理邏輯**: 呼叫 `History.get_by_user(user_id)`。
- **輸出**: `history.html`。若未登入則重導向至 `/auth/login`。

### 儲存歷史紀錄 (`/history/add`)
- **輸入**: `poem_id` (從表單送出)
- **處理邏輯**: 從 Session 取得 `user_id` 與暫存的 `question`，呼叫 `History.create(...)` 寫入資料庫。
- **輸出**: 重導向至 `/history`。

### 捐贈香油錢 (`/donation/donate`)
- **輸入**: `amount`, `message`
- **處理邏輯**: 
  - GET: 顯示表單。
  - POST: 呼叫 `Donation.create(user_id, amount, message)`，若未登入仍可視為匿名捐款(或強迫登入)。
- **輸出**: POST 成功後重導向至 `/donation/thanks`。

### 感謝頁面 (`/donation/thanks`)
- **輸出**: `thanks.html`

## 3. Jinja2 模板清單

所有的模板將放在 `app/templates/` 目錄下：

1. `base.html`: 全站共用基礎佈局（包含 Header 選單與 Footer），其他頁面皆繼承此模板。
2. `index.html`: 繼承 `base.html`，首頁介紹。
3. `login.html`: 繼承 `base.html`，登入與註冊表單。
4. `draw.html`: 繼承 `base.html`，求籤與擲筊互動區。
5. `result.html`: 繼承 `base.html`，顯示籤文結果。
6. `history.html`: 繼承 `base.html`，歷史紀錄清單。
7. `donate.html`: 繼承 `base.html`，香油錢表單。
8. `thanks.html`: 繼承 `base.html`，感謝捐款頁面。
