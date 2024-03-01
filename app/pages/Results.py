import streamlit as st
from PIL import Image
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from numba import jit
import numba


st.set_page_config(page_title="Results", page_icon=("app/icons/results.png"))

st.sidebar.title("Resuls")
 
st.title("Results")

st.markdown('[Результаты эксперимента](https://github.com/alla-bobrova/Synchronization/tree/main/exp1)')


@jit(nopython=True, parallel=True)
def system(phi, t, N, mu, omega, gamma, d, R):
    result = np.zeros_like(phi)

    for j in numba.prange(N):
        sum_term = 0.0
        for k in range(N):
            if j != k:
                sum_term += R[k] * np.sin(phi[k] - phi[j] - gamma)

        result[j] = mu / 2 * (omega[j] + d / R[j] * sum_term)

    return result

def plot():
    st.subheader("Dynamic Visualization")

    # Parameters
    N = st.slider("Number of oscillators", min_value=1, max_value=256, value=128, step=1)
    mu = st.slider(r"$\mu$", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    d = st.slider(r"$d$", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    gamma = st.slider(r"$\gamma$", min_value=0.0, max_value=np.pi, value=3*np.pi/4, step=np.pi/100)
    
    omega = np.ones(N)
    R = np.ones(N)

    phi0 = 2 * np.pi * np.random.rand(N)
    time_span = st.slider("Time span:", min_value=100, max_value=3000, value=1000, step=100)
    t_span = np.linspace(0, time_span, 1000)
    solution = odeint(system, phi0, t_span, args=(N, mu, omega, gamma, d, R))

    # приведение к [0, 2пи]
    solution = np.fmod(solution, 2*np.pi)
    # 0 и 2пи на окружности одна точка
    solution[solution == 2*np.pi] -= 2*np.pi
    # отрицательные привели к [0, 2пи]
    solution[solution < 0] += 2*np.pi


    st.subheader("Финальные значения фаз осцилляторов")
    # Распределение осцилляторов на плоскости
    plt.plot(range(N), solution[-1,:], marker='o')
    plt.xlabel('$j$')
    plt.ylabel('$\phi_j$')
    plt.grid(True)
    st.pyplot(plt)
    plt.show()

    # Распределение осцилляторов на окружности
    theta = solution[-1, :]
    x = np.cos(theta)
    y = np.sin(theta)

    fig, ax = plt.subplots(figsize=(6, 6))
    sc = ax.scatter(x, y, c=range(1, N+1), cmap='viridis',
                    s=50, edgecolor='black', linewidth=0.6)
    ax.set_aspect('equal', 'box')

    circle = plt.Circle((0, 0), 1, color='black',
                        fill=False, linewidth=0.5, alpha=0.8)
    ax.add_patch(circle)
    ax.grid()

    cbar = plt.colorbar(sc, shrink=0.8)
    cbar.set_label('Номер осциллятора')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    st.pyplot(fig)
    plt.show()


    st.subheader("Order parameter")
    # Построение графиков параметров порядка
    R1 = np.abs(np.mean(np.exp(1j * solution[:, :]), axis=1))
    R2 = np.abs(np.mean(np.exp(2j * solution[:, :]), axis=1))

    fig, ax = plt.subplots()
    ax.plot(t_span, R1, label='R1')
    ax.plot(t_span, R2, label='R2')
    ax.grid(True)
    ax.set_xlabel('Время')
    ax.set_ylabel('Значение')
    ax.legend()
    st.pyplot(fig)
    st.write("Final values of R1 and R2:")
    st.write(f"R1: {R1[-1]}")
    st.write(f"R2: {R2[-1]}")


    st.subheader("Пространственно-временная диаграмма")
    # Создание цветовой карты
    colors = ['#FFFF00', '#800080']
    n_bins = 100  # Количество оттенков

    # 0 и 2*pi одним цветом
    color_map_values = np.linspace([1, 1, 0], [128/255, 0, 128/255], n_bins)
    color_map_values[0, :] = color_map_values[-1, :] = [1, 1, 0]

    cmap_name = "custom_gradient"
    custom_cmap = ListedColormap(color_map_values)

    # Построение с градиентом цветовой карты
    fig, ax = plt.subplots()
    im = ax.imshow(solution.T, aspect='auto', cmap=custom_cmap, extent=[
                t_span[0], t_span[-1], 0, N], vmin=0, vmax=2*np.pi)
    cb = plt.colorbar(im, ax=ax, label=fr'$\phi_j$', ticks=[0, np.pi, 2*np.pi])
    cb.set_ticklabels(['$0$', '$\pi$', '$2\pi$'])

    plt.xlabel(fr'$t$')
    plt.ylabel(fr'$j$')
    st.pyplot(fig)
    plt.show()


plot()
