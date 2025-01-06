# 日本語学習済みモデルをdropboxからダウンロード
from gensim.models import KeyedVectors
import streamlit as st
import requests
import os

dropbox_link = "https://www.dropbox.com/scl/fi/89zfk7npuo5suivpkox97/jawiki.word_vectors.300d.bin?rlkey=4hi0dkpr16plbsdb2w37v3u1r&st=3miejyz1&dl=1"

def download_file(url, destination):
    response = requests.get(url, stream=True)
    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

# gensimでモデルを読み込む（cache化する）
@st.cache(allow_output_mutation=True)
def load_model():
    temp_path = "/tmp/jawiki.word_vectors.300d.bin"
    if not os.path.exists(temp_path):
        download_file(dropbox_link, temp_path)
    model = KeyedVectors.load_word2vec_format(temp_path, binary=True)
    return model

# モデルのロードをローディングインジケーターで包む
with st.spinner('日本語学習済みモデル(800MB)をロード中...しばらくお待ちください。'):
    try:
        model = load_model()
    except Exception as e:
        st.error(f"モデルのロードに失敗しました: {e}")
        st.stop()

if "word_base" not in st.session_state:
    st.session_state.word_base = ""
if "word_sub" not in st.session_state:
    st.session_state.word_sub = ""
if "word_add" not in st.session_state:
    st.session_state.word_add = ""  

# 使用例
st.sidebar.title('Word2Vecアプリ')
st.sidebar.write("")

func = st.sidebar.radio("処理を選択してください。",
                        ("類似語を調べる","単語間の類似度を調べる","単語の足し算","単語の引き算","単語のアナロジー"))

st.sidebar.write("")
st.sidebar.write("東北大学乾研究室の日本語Wikipediaエンティティベクトルを使用しています。")

if func == "類似語を調べる":
    word_base = st.text_input("単語を入力してください。", value="青春")
    if st.button('実行'):
        try:
            results = model.most_similar(word_base, topn=5)
            for word_kouho, similarity in results:
                st.write(f'{word_kouho}: {similarity:.2f}')
        except KeyError:
            st.write('入力した単語は登録されていません。')     

if func == "単語間の類似度を調べる":
    word_a = st.text_input("単語を入力してください。", value="ラーメン")
    word_b = st.text_input("単語を入力してください。", value="パスタ")
    if st.button('実行'):
        try:
            result = model.similarity(word_a, word_b)
            st.write(result)
        except KeyError:
            st.write('入力した単語は登録されていません。')     

if func == "単語の足し算":
    word_base = st.text_input("最初の単語を入力してください。", value="公務員")
    word_add = st.text_input("足し算する単語を入力してください。", value="ピストル")
    if st.button('足し算を実行'):
        try:
            results = model.most_similar(positive=[word_base, word_add], topn=5)
            for word_kouho, similarity in results:
                st.write(f'{word_kouho}: {similarity:.2f}')
        except KeyError:
            st.write('入力した単語は登録されていません。')     

if func == "単語の引き算":
    word_base = st.text_input("最初の単語を入力してください。", value="人生")
    word_sub = st.text_input("引き算する単語を入力してください。", value="お金")
    if st.button('引き算を実行'):
        try:
            results = model.most_similar(positive=[word_base], negative=[word_sub], topn=5)
            for word_kouho, similarity in results:
                st.write(f'{word_kouho}: {similarity:.2f}')
        except KeyError:
            st.write('入力した単語は登録されていません。')     

if func == "単語のアナロジー":
    word_base = st.text_input("最初の単語を入力してください。", value="王")
    st.session_state.word_base = word_base
    word_sub = st.text_input("引き算する単語を入力してください。", value="男")
    st.session_state.word_sub = word_sub
    word_add = st.text_input("足し算する単語を入力してください。", value="女")
    st.session_state.word_add = word_add
    if st.button('アナロジーを実行'):
        try:
            results = model.most_similar(positive=[st.session_state.word_base, 
                                                   st.session_state.word_add], 
                                         negative=[st.session_state.word_sub], topn=5)
            for word_kouho, similarity in results:
                st.write(f'{word_kouho}: {similarity:.2f}')
        except KeyError:
            st.write('入力した単語は登録されていません。')     
