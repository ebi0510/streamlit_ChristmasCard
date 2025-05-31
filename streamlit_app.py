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
st.title("Streamlitクリスマスカード 🎅")

# st.button=ボタンを作成。押すとTrueが返ってくる。括弧内はボタンに表示する文字
button_pushed = st.button("雪を降らせる")
# もしbutton_pushedの結果がTrueだったら、st.snowを実行する
if button_pushed:
    st.snow()

name = st.text_input(
    label = "あなたの名前を入力してください",
    placeholder = "山田花子")

# 空白選んでたらTrue判定だと思ったんだけど、違うらしい
country = st.selectbox(
    'あなたの国',
    ['','日本', 'アメリカ', '中国', 'オーストラリア'],
    )

st.write('名前:', name)
st.write('国：', country)

if name and country:
    st.write('入力が完了しました！')
    message = make_message(name, country)
    st.write(message)
    image = make_image(country)
    # 画像を表示するときはst.image
    st.image(image)


