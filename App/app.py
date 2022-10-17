import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
from pathlib import Path

# Title
st.set_page_config(page_title='WHE Distribution')

# Import markdown files
def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

# The body of the document
README = read_markdown_file('README.md')
st.markdown(README, unsafe_allow_html=False)

# Load dataframe
f = 'CWUR_Rank_Meta_19.csv'
df1 = pd.read_csv(f)
f = 'CWUR_Rank_Meta_22.csv'
df2 = pd.read_csv(f)

# Sort top 100 data
df1.sort_values(['top_100'], axis=0, ascending=[False], inplace=True)
df2.sort_values(['top_100'], axis=0, ascending=[False], inplace=True)

# Keep only non-zero values
df1_100 = pd.DataFrame(columns = ['country', 'top_100'])
for i, r in df1.iterrows():
    if r['top_100'] != 0:
        df1_100 = df1_100.append({'country':r['country'], 'top_100':r['top_100']}, ignore_index = True)
    else:
        break
df2_100 = pd.DataFrame(columns = ['country', 'top_100'])
for i, r in df2.iterrows():
    if r['top_100'] != 0:
        df2_100 = df2_100.append({'country':r['country'], 'top_100':r['top_100']}, ignore_index = True)
    else:
        break

# Sort top 300 data
df1.sort_values(['top_300'], axis=0, ascending=[False], inplace=True)
df2.sort_values(['top_300'], axis=0, ascending=[False], inplace=True)

# Keep only non-zero values
df1_300 = pd.DataFrame(columns = ['country', 'top_300'])
for i, r in df1.iterrows():
    if r['top_300'] != 0:
        df1_300 = df1_300.append({'country':r['country'], 'top_300':r['top_300']}, ignore_index = True)
    else:
        break
df2_300 = pd.DataFrame(columns = ['country', 'top_300'])
for i, r in df2.iterrows():
    if r['top_300'] != 0:
        df2_300 = df2_300.append({'country':r['country'], 'top_300':r['top_300']}, ignore_index = True)
    else:
        break


col1, col2, col3, col4 = st.columns([1,1,1,1])
with col1:
    # Category 1_2: Top 100 <- 2019-20
    c12 = st.button("Top 100 (2019-20)", key="1")
with col2:
    # Category 1_3: Top 300 <- 2019-20
    c13 = st.button("Top 300 (2019-20)", key="2")
with col3:
    # Category 2_2: Top 100 <- 2022-23
    c22 = st.button("Top 100 (2022-23)", key="3")
with col4:
    # Category 2_3: Top 300 <- 2022-23
    c23 = st.button("Top 300 (2022-23)", key="4")

# On-click
if c12:
    # Bar chart 1_1
    bc11 = px.bar(df1_100,
                    x='country',
                    y='top_100',
                    text='top_100',
                    color_discrete_sequence = ['#F63366']*len(df1_100),
                    template= 'plotly_white')
    st.plotly_chart(bc11)
if c13:
    # Bar chart 1_2
    bc12 = px.bar(df1_300,
                    x='country',
                    y='top_300',
                    text='top_300',
                    color_discrete_sequence = ['#F63366']*len(df1_300),
                    template= 'plotly_white')
    st.plotly_chart(bc12)


# On-click
if c22:
    bc21 = px.bar(df2_100,
                    x='country',
                    y='top_100',
                    text='top_100',
                    color_discrete_sequence = ['#F63366']*len(df2_100),
                    template= 'plotly_white')
    # Plot right away
    st.plotly_chart(bc21)
if c23:
    # Bar chart 2_2
    bc22 = px.bar(df2_300,
                    x='country',
                    y='top_300',
                    text='top_300',
                    color_discrete_sequence = ['#F63366']*len(df2_300),
                    template= 'plotly_white')
    st.plotly_chart(bc22)

# Geographic distribution
IMAGE = read_markdown_file('IMAGE.md')
st.markdown(IMAGE, unsafe_allow_html=False)
img = Image.open('Images/WHED_2019-22.png')
st.image(img)

# The latter part of the doc
LATTER = read_markdown_file('LATTER.md')
st.markdown(LATTER, unsafe_allow_html=False)
