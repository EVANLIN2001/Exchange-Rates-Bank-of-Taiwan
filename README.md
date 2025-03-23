# 貨幣匯率查詢應用程式
這個專案是一個基於 Python 與 Flask 的 Web 應用程式，利用 [台灣銀行匯率網站](https://rate.bot.com.tw/xrt?Lang=zh-TW) 的資料，自動抓取並展示最新的現金賣出匯率。應用程式支援中文與英文輸入貨幣名稱，讓你輕鬆查詢所需的匯率資訊。

<img src="https://example.com/myimage.png" alt="Logo" width="300"/>

## 功能特色
- **自動資料抓取**  
  使用 Requests 與 PyQuery 從台灣銀行獲取最新匯率資料。

- **前端查詢介面**  
  採用 Flask 與 Bootstrap 建構簡潔美觀的網頁介面，方便使用者輸入與查詢。

- **中英文支援**

  使用者可輸入中文或英文貨幣名稱，系統自動轉換並查詢對應的匯率。

## 技術棧
- **後端**：Python, Flask  
- **資料抓取**：Requests, PyQuery  
- **前端**：HTML, CSS, Bootstrap
  
### 此專案結構簡單，適合初學者參考與學習網頁爬蟲、資料解析以及 Web 應用程式開發。
