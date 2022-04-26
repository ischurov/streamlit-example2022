import streamlit as st
import pandas as pd
import numpy as np

def print_hello(name="World"):
    st.write(f"## Hello, {name}!")

name = st.text_input("Your name", key="name", value='Anonymous')
print_hello(name)

"""
Let's play with functions
"""

a = st.slider("a")
x = np.linspace(-6, 6, 500)
df = pd.DataFrame(dict(y=np.sin(a * x)))
st.line_chart(df)

# print("Module helloworld is loaded")

# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     print_hello(name)