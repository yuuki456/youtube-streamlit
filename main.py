import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iterration = st.empty()
bar = st.progress(0)


for i in range(100):
    latest_iterration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)






left_column, right_column = st.columns(2)

button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここが右カラム')
expander1 = st.expander('お問い合わせ1')
expander1.write('お問い合わせ1の回答')
expander2 = st.expander('お問い合わせ2')
expander2.write('お問い合わせ2の回答')
expander3 = st.expander('お問い合わせ3')
expander3.write('お問い合わせ3の回答')
expander4 = st.expander('お問い合わせ4')
expander4.write('お問い合わせ4の回答')

#'あなたの趣味：',text
#'コンディション：', condition
