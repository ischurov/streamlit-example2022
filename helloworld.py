import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import altair as alt

with st.echo(code_location='below'):
    """
    ## Hello, World!
    """


    def print_hello(name="World"):
        st.write(f"### Hello, {name}!")


    name = st.text_input("Your name", key="name", value="Anonymous")
    print_hello(name)

    """
    ## Добавим графики
    Чтобы заработали библиотеки seaborn и altair, нужно добавить в проект файл 
    `requirements.txt` с такими строчками:
    
        seaborn
        altair
    """


    a = st.slider("a")
    x = np.linspace(-6, 6, 500)
    df = pd.DataFrame(dict(x=x, y=np.sin(a * x)))
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="x", y="y", ax=ax)
    st.pyplot(fig)

    """
    ## Немного анализа данных
    """


    @st.cache
    def get_data():
        data_url = (
            "https://github.com/Godoy/imdb-5000-movie-dataset/raw/"
            "master/data/movie_metadata.csv"
        )
        return (
            pd.read_csv(data_url)
            .dropna(subset=["title_year"])
            .assign(
                title_year=lambda x: pd.to_datetime(
                    x["title_year"], format="%Y"
                )
            )
        )


    df = get_data()

    director = st.selectbox(
        "Director", df["director_name"].value_counts().iloc[:10].index
    )

    df_selection = df[lambda x: x["director_name"] == director]
    df_selection

    chart = (
        alt.Chart(df_selection)
        .mark_circle()
        .encode(x=alt.X("title_year:T"), y="imdb_score", tooltip="movie_title")
    )

    st.altair_chart(
        (
            chart
            + chart.transform_loess("title_year", "imdb_score").mark_line()
        ).interactive()
        # .transform_loess добавляет сглаживающую кривую
    )
