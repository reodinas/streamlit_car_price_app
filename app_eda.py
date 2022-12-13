import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda_app():
    df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    st.subheader('데이터 프레임 확인')
    st.dataframe(df.head(3))

    st.subheader('기본 통계 데이터')
    st.dataframe(df.describe())

    # 컬럼을 선택할 수 있게 한다. 하나의 컬럼을 선택하면,
    # 해당 컬럼의 최대값, 최소값 데이터를 화면에 보여준다.
    st.subheader('최대/최소 데이터 확인하기')
    columns_list = df.columns[4:]

    selected_col = st.selectbox('컬럼을 선택하세요.', columns_list)

    df_min = df.loc[df[selected_col] == df[selected_col].min(), ]
    df_max = df.loc[df[selected_col] == df[selected_col].max(), ]
    
    st.text('최대 데이터')
    st.dataframe(df_max)
    st.text('최소 데이터')
    st.dataframe(df_min)

    # 컬럼을 선택하면 그 컬럼의 히스토그램을 보여준다.
    st.subheader('컬럼 별 히스토그램')
    histogram_col = st.selectbox('히스토그램 확인할 컬럼을 선택하세요.', columns_list)
    my_bins = st.number_input('빈의 갯수를 입력하세요', 10, 30, value=10, step=1)
    
    fig1 = plt.figure()
    plt.hist(data=df, x=histogram_col, rwidth=0.8, bins=my_bins)
    plt.title(histogram_col + ' Histogram')
    plt.xlabel(histogram_col)
    plt.ylabel('Count')
    st.pyplot(fig1)


    st.subheader('상관 관계 분석')
    
    selected_list = st.multiselect('상관분석을 하고 싶은 컬럼을 선택하세요.', columns_list)

    if len(selected_list) >= 2:

        df_corr = df[selected_list].corr()

        fig2 = plt.figure()
        sb.heatmap(data=df_corr, annot=True, fmt='.2f', cmap='coolwarm',
            vmin=-1, vmax=1, linewidth=0.5)
        st.pyplot(fig2)

