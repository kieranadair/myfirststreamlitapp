import streamlit as st
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('My First App')

# Button
st.subheader("This is a button")
if st.button("Say Hello"):
    st.write("HELLO THERE")
else:
    st.write("Click the button to make me say hello")

# Example 1
st.subheader('Display text')
st.write('Hello, *World!* :sunglasses:')

# Example 2
st.subheader('Display numbers')
st.write(1234)

# Example 3
st.subheader('Display DataFrame')
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4
st.subheader('Accept multiple arguments')
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5
st.subheader('Display charts')
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


