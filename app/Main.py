import subprocess
import streamlit as st

# Обновление pip
subprocess.run(["pip", "install", "--upgrade", "pip"])

# Установка зависимостей из файла requirements.txt
subprocess.run(["pip", "install", "-r", "requirements.txt"])

st.set_page_config(page_title="Synchronization", page_icon=("app/icons/main_page.png"))

def main():

    st.sidebar.title("Main")

    st.title("Synchronization")

    st.header("Содержание:")

    st.markdown(r''' Модель:
    $$
    \begin{cases}
    \dot{x}_j=y_j\\
    \dot{y}_j=\mu (1-x_j^2)y_j - (1+\mu\Omega_j)x_j +\mu\alpha \displaystyle \sum^N_{k=1} {(x_k-x_j)} + \mu\beta\displaystyle \sum^N_{k=1} {(y_k-y_j)}
    \end{cases}
    $$
    ''')
    st.subheader("R - one-dimensional array.ipynb")
    st.write("Моделирование уравнения фаз глобально связанных осцилляторов Ван дер Поля. Связи между осцилляторами заданы одномерным массивом.")

    st.subheader("R - matrix.ipynb")
    st.write("Моделирование уравнения фаз глобально связанных осцилляторов Ван дер Поля. Связи между осцилляторами заданы матрицей $N\\times N$, где $R_{ij}=0$ при $i=j$.")

    st.subheader("Results")
    st.write("Результаты для `R - matrix.ipynb` при единичных связях и значениях собственных частот совпадают с `R - one-dimensional array.ipynb`.")


if __name__ == "__main__":
    main()
