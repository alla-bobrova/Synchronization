import streamlit as st

st.set_page_config(page_title="Models", page_icon=("app/icons/phase_reduction.png"))

st.sidebar.title("Models")
 
st.title("Models")

st.subheader("Первый вид связи")
st.markdown(r'''
$$
 \begin{cases}
   \dot{x}_j=y_j+\mu\alpha \displaystyle \sum^N_{k=1} {(x_k-x_j)}\\
   \dot{y}_j=\mu (1-x_j^2)y_j - (1+\mu\Omega_j)x_j + \mu\beta\displaystyle \sum^N_{k=1} {(y_k-y_j)}
 \end{cases}
$$
''')


st.subheader("Второй вид связи")
st.markdown(r'''
$$
 \begin{cases}
   \dot{x}_j=y_j\\
   \dot{y}_j=\mu (1-x_j^2)y_j - (1+\mu\Omega_j)x_j +\mu\alpha \displaystyle \sum^N_{k=1} {(x_k-x_j)} + \mu\beta\displaystyle \sum^N_{k=1} {(y_k-y_j)}
 \end{cases}
$$
''')