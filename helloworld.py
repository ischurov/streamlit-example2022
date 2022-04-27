import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def print_hello(name="World"):
    st.write(f"## Hello, {name}!")

name = st.text_input("Your name", key="name", value='Anonymous')
print_hello(name)

"""
Let's play with functions
"""

a = st.slider("a")
x = np.linspace(-6, 6, 500)
df = pd.DataFrame(dict(x=x, y=np.sin(a * x)))
fig, ax = plt.subplots()
sns.lineplot(data=df, x='x', y='y', ax=ax)
st.pyplot(fig)

# print("Module helloworld is loaded")

# if __name__ == "__main__":
#     name = input("Enter your name: ")
#     print_hello(name)