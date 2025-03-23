from flask import Flask, render_template, request
from pyquery import PyQuery
import requests

app = Flask(__name__)

def get_currency_rate(name):
    url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"
    res = requests.get(url)
    html = PyQuery(res.text)

    # 擷取中文與英文幣別名稱
    chinese_list = html("div.hidden-phone.print_show").text().split()[::2]
    english_list = html("div.hidden-phone.print_show").text().split()[1::2]

    # 擷取本行現金賣出的匯率
    sell_list = html("td[data-table=本行現金賣出]").text().split()[::2]

    # 建立中文對英文的字典，以及英文對匯率的字典
    ch_to_en = dict(zip(chinese_list, english_list))
    en_to_rate = dict(zip(english_list, sell_list))

    # 判斷輸入的幣別是中文還是英文
    if name in ch_to_en:
        en_name = ch_to_en[name]
    elif name in en_to_rate:
        en_name = name
    else:
        return None

    # 取得該英文幣別對應的匯率
    rate = en_to_rate.get(en_name)
    return rate

@app.route("/", methods=["GET", "POST"])
def index():
    rate = None
    currency_name = ""
    message = ""
    
    if request.method == "POST":
        # 從表單中取得使用者輸入的幣別名稱
        currency_name = request.form.get("currency")
        rate = get_currency_rate(currency_name)
        if rate:
            message = f"{currency_name} 現金匯率/本行賣出為: {rate}"
        else:
            message = f"找不到 {currency_name} 的匯率資料"
    
    return render_template("indexnew.html", message=message, currency_name=currency_name)
if __name__ == "__main__":
    app.run(debug=True)