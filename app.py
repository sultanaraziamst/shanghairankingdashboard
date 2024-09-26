import pip

import streamlit as st 
import pandas as pd
import datetime
import altair as alt
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go 
import plotly.figure_factory as ff

#reading data data from excel 

df = pd.read_csv("shanghai_ranking_2024.csv")
st.set_page_config(layout="wide")
initial_sidebar_state="expanded"

st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html = True)

Image = Image.open('ranking_logo.png')
col1, col2 = st.columns([0.1, 0.9])
with col1:
    st.image(Image,width=100)

html_title = """
    <style>
    .title-test {
    font-weight:5px;
    border-radius:6px
    }
    </style><h1 class="title-test">University ranking dashboard</h1></center>
    </style><p>This Dashboard provides detailed information about the methodology used in the 2024 Academic Ranking of World Universities (ARWU), commonly known as the ShanghaiRanking. The ARWU evaluates and ranks universities worldwide based on academic and research performance indicators. In 2024, more than 2,500 universities were considered, with the top 1,000 being published.</p>"""

    

with col2: 
    st.markdown(html_title, unsafe_allow_html=True)

col3, col4, col5 = st.columns([0.1, 0.45, 0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last Updated by:\n {box_date}")

with col4:
    top_100_universities = df.nlargest(100, 'Alumni')
    fig = px.bar(top_100_universities, x = "University_Name", y="Alumni",color="Alumni" , labels={"Award": "University Name{}"},
                title="Shanghai University Ranking", hover_data=["Award"],
                template="gridon", height=1000)
st.plotly_chart(fig,use_container_width=True)

with col5:
    fig = px.bar(df, x = "National/Regional Rank", y="Rank", labels={"Publication by National": "University Name{}"},
                title="The rank of the university within its respective country or region", hover_data=["PUB"],
                template="gridon", height=500)
st.plotly_chart(fig,use_container_width=True)


with col5:
    fig = px.histogram(df, x = "Hici", y="PCP", color="Hici", labels={"Highly cited data": "PCP{}"},
                title="The score based on the number of Highly Cited Researchers affiliated with the university", hover_data=["Hici"],
                template="gridon", height=500)
st.plotly_chart(fig,use_container_width=True)


with col5:
    top_100_universities = df.nlargest(100, 'N&S')
    fig = px.scatter(df, x = "N&S", y="PCP", color="N&S", labels={"Not significant": "PCP{}"},
                title="The score representing the number of research articles published in Nature and Science between 2019 and 2023..", hover_data=["Alumni"],
                template="gridon", height=500)
st.plotly_chart(fig,use_container_width=True)


