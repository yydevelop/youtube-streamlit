import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

left_column,right_column=st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせの内容を書く')

# text=st.slider('あなたの趣味を教えてください',0,100,50)
# condition=st.slider('あなたの趣味を教えてください',0,100,50)

# 'あなたの趣味は、',text,'です'
# 'コンディション',condition

# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img=Image.open('sample.jpg')
#     st.image(img,caption='sample',use_column_width=True)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
# )
# st.map(df)

#st.table(df.style.highlight_max(axis=0))
