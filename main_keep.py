import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Itaration{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)

'Done!!!'

#st.write('DataFrame')   #add text
#st.write('Display Image')   #add text

#st.sidebar.write('Intractive Widgets')
#st.write('Intractive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです。')

exp = st.expander('問い合わせ')
exp.write('問い合わせ内容を記載')

text = st.text_input('あなたの趣味を教えて下さい')
'あなたの趣味：',text, 'です。'

# if st.checkbox('showImage'):
#     # 図の挿入
#     img = Image.open('C:\\Users\\skino\\OneDrive\\画像\\202310リゾナーレ八ヶ岳\\S__477995050_0.jpg')
#     st.image(img,caption='Tsumu',use_column_width=True)


option = st.sidebar.selectbox(
    'あなたな好きな数字を指定下さい',
    list(range(1,11))
)

'あなたの好きな数字は、',option, 'です'


cond = st.slider('あなたの調子は？',0,100,50) # 最小値、最大値、初期値
'コンディション：',cond

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]    
})

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)

#st.write(df)
#st.dataframe(df.style.highlight_max(axis=0),width=1000,height=1000)   #widthなどの引数が用意されている
#st.table(df.style.highlight_max(axis=0))    #staticな表を表示


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,130.79],
    columns=['latitude','longitude']
)

st.map(df)
