# Streamlitを使うときはこのようにimport
import streamlit as st

def make_message(name:str, country:str):
    data = {
        "日本": f"メリークリスマス、{name}さん！このクリスマスが{name}さんにとって愛と喜びに満ちたものになりますように。",
        "アメリカ": f"Ho Ho Ho! Merry Christmas, {name}! May your heart be warm, your home be bright, and your days be merry and full of happiness.",
        "中国": f"亲爱的{name}、圣诞快乐！愿你的每一天都充满笑容和祝福！",
        "オーストラリア": f"Ho Ho Ho! Merry Christmas, {name}! May your heart be warm, your home be bright, and your days be merry and full of happiness.",
    }
    return data[country]

def make_image(country:str):
    image = {
        "日本": "https://i.gyazo.com/7f7fa9985d27a49f7b65f2b6faf7bde5.jpg",
        "アメリカ": "https://i.gyazo.com/0ed3c1555f8c474a81a5ec77ecb657ff.jpg",
        "中国": "https://i.gyazo.com/721cc5acf919c27c9a57005af8b78ea2.jpg",
        "オーストラリア": "https://i.gyazo.com/566a5129252ac459c3493b07e0bb0683.jpg"
    }
    return image[country]

# st.title＝タイトル表示
st.title(f"Streamlitクリスマスカード 🎅")

# st.button=ボタンを作成。押すとTrueが返ってくる。括弧内はボタンに表示する文字
button_pushed = st.button(f"雪を降らせる")
# もしbutton_pushedの結果がTrueだったら、st.snowを実行する
if button_pushed:
    st.snow()

card_number = st.slider(f'送る枚数を選択してください', 1, 5)

st.write(f'送る枚数', card_number)

# card_numberに合わせて入力フォームを表示
# rangeは指定範囲を繰り返すときに使う
# テキストを表示するときは冒頭にfが必要
# iの定義は不要らしい
for i in range(card_number):
    name = st.text_input(
    label = f'{i+1}人目の名前を入力してください',
    placeholder = f'山田花子')

    country = st.selectbox(
    f'{i+1}人目の国を選んでください',
    ['','日本', 'アメリカ', '中国', 'オーストラリア'],
    )

    # テキストが全く同じ表示だとバグる？
    show_image = st.checkbox(f'{i+1}人目のカードに画像を表示しますか？')
    
    if name and country:
        st.divider()
        st.caption(f'💌 {name}にサンタさんからのクリスマスカードが届いたよ！')
        message = make_message(name, country)
        st.write(message)
        image = make_image(country)
        # 画像を表示するときはst.image
        if show_image:
            st.image(image)
        st.divider()


