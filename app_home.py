import streamlit as st

def run_home_app():
    st.text('환영합니다!')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('데이터분석 및 고객 정보를 넣으면, 얼마정도의 차를 구매할지를 예측해 줍니다.')
    img_url = 'https://search.pstatic.net/sunny/?src=https%3A%2F%2Fcdn.ppomppu.co.kr%2Fzboard%2Fdata3%2F2014%2F0805%2F1407200822_20140805_%25B1%25B9%25BB%25EA%25C2%25F7_2.jpg&type=a340'
    st.image(img_url)