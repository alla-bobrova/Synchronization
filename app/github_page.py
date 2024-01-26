import streamlit as st

def main():
    st.title("Synchronization")

    st.markdown("## R - one-dimensional array.ipynb")
    st.write("Моделирование уравнения фаз глобально связанных осцилляторов Ван дер Поля. Связи между осцилляторами заданы одномерным массивом.")

    st.markdown("## R - matrix.ipynb")
    st.write("Моделирование уравнения фаз глобально связанных осцилляторов Ван дер Поля. Связи между осцилляторами заданы матрицей $N\\times N$, где $R_{ij}=0$ при $i=j$.")

    st.markdown("### Results")
    st.write("В данных файлах содержатся результаты моделирования для:")
    st.write("- $\\gamma=\\displaystyle\\frac{\\pi}{4}$: `piDiv4.ipynb`")
    st.write("- $\\gamma=\\displaystyle\\frac{\\pi}{2}$: `piDiv2.ipynb`")
    st.write("- $\\gamma=\\displaystyle\\frac{3\\pi}{4}$: `3piDiv4.ipynb`")
    st.write("- $\\gamma=\\pi$: `pi.ipynb`")
    st.write("Результаты для `R - matrix.ipynb` при единичных связях и значениях собственных частот совпадают с `R - one-dimensional array.ipynb`.")

if __name__ == "__main__":
    main()


