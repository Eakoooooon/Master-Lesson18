"""
自己紹介カードの作成

"""
import datetime


# 生年月日から年齢を計算する関数
def get_age(year, month, day):
    dt_now = datetime.datetime.now()
    birthday = datetime.datetime(
        year=year,
        month=month,
        day=day
    )

    # 経過日数を計算
    elapsed_days = dt_now - birthday
    # 計算した経過日数を365で割ることで何年経過しているか算出する
    age = int((elapsed_days.days) / 365)
    return str(age)


# 取得情報を入れる辞書
my_info = {
    "name": None,
    "birthday_year": None,
    "birthday_month": None,
    "birthday_day": None,
    "age": None,
    "hobby": None,
    "message": None
}

# 　表示するメッセージリスト
msg_list = [
    "自己紹介カードを作成します。\n以下の情報を入力してください。",
    "名前を入力してください",
    "生年月日を入力してください",
]

print(msg_list[0])

# 名前の入力
print("Q1")
my_info["name"] = input(msg_list[1] + "\n")

# 生年月日の入力
print("Q2")
print(msg_list[2])

# 生年月日の入力
# 入力された値はint型に変換して辞書に保存
# intに変換できない者が入力されたときはエラーとなる
try:
    my_info["birthday_year"] = int(input("年(西暦)は？" + "\n"))
    my_info["birthday_month"] = int(input("月は？" + "\n"))
    my_info["birthday_day"] = int(input("日は？" + "\n"))

    # 年齢の計算
    my_info["age"] = get_age(year=my_info["birthday_year"],
                             month=my_info["birthday_month"],
                             day=my_info["birthday_day"])
except ValueError as e:
    print(e)

# 趣味と一言メッセージの入力
my_info['hobby'] = input("趣味を入力してください\n")
my_info['message'] = input("一言メッセージを入力してください\n")

# カードの作成
card = f"名前：{my_info['name']}\n生年月日：{my_info['birthday_year']}/{my_info['birthday_month']}/{my_info['birthday_day']}（{my_info['age']} 歳）\n趣味：{str(my_info['hobby'])}\n一言メッセージ：{str(my_info['message'])}"

# 自己紹介カードの表示
print("===========================================================")
print(card)
print("===========================================================")
