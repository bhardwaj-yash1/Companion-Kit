import streamlit as st

st.title("Companion Kit")
st.header("predict disease as early as possible !!")
st.text("Plain text")
st.markdown("**Bold text** and _italic_")
st.latex(r"E = mc^2")  # Math

import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.dataframe(df)     # Interactive
st.table(df)         # Static
st.json({"key": "value"})

name = st.text_input("Enter your name")
age = st.number_input("Age", 0, 120)
option = st.selectbox("Choose", ["A", "B", "C"])
options = st.multiselect("Pick some", ["A", "B", "C"])
agree = st.checkbox("I agree")
value = st.slider("Range", 0, 100, 50)
file = st.file_uploader("Upload file")
clicked = st.button("Click me")


st.sidebar.title("Sidebar Menu")
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 content")
with col2:
    st.write("Column 2 content")

with st.expander("More info"):
    st.write("Hidden details here")


st.line_chart(df)
st.bar_chart(df)
st.map(df)  # For lat/lon data

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)


@st.cache_data
def load_data():
    # Expensive operation
    return df

if "count" not in st.session_state:
    st.session_state.count = 0
st.session_state.count += 1
st.write(st.session_state.count)


[theme]
primaryColor="#FF4B4B"
backgroundColor="#FFFFFF"
textColor="#262730"
