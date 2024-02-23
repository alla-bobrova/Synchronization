import streamlit as st

st.set_page_config(page_title="Phase reduction", page_icon=("app/icons/phase_reduction.png"))

st.sidebar.title("Phase reduction")
 
st.title("Phase reduction")

st.markdown(r'''

Обобщенное уравнение Гинзбурга-Ландау:

$$
\dot{z}_j= \Big(\sum^N_{k=1}{(z_k-z_j)}\Big)(\beta-i\alpha)  +z_j(1+i\Omega_j-|z_j|^2) 
$$

После разделения на действительную и мнимую части:

$$
\dot{R}_j=\frac{\mu}{2} \Big[R_j\Big(1-\frac{1}{4}R_j^2-\beta N\Big) + \displaystyle\sum^N_{k=1}{R_k(\beta\cos{(\phi_k-\phi_j)}} + \alpha\sin{(\phi_k-\phi_j))} \Big]
$$

$$
\dot{\phi}_j =\frac{\mu}{2} \Big[ \Omega_j + \alpha N + \displaystyle\frac{1}{R_j}\sum_{k=1}^N{R_k(\beta\sin(\phi_k-\phi_j)-\alpha\cos(\phi_k-\phi_j))} \Big] 
$$

Вынесем $\beta$ из-под знака суммы, введем обозначение $c_1=\displaystyle\frac{\alpha}{\beta}, \beta=\epsilon$ и перейдем к новому времени $\tau=\displaystyle\frac{\mu}{2}t$.

$$
R_j^\prime=R_j\Big(1-\frac{1}{4}R_j^2-\epsilon N\Big) + \epsilon\displaystyle\sum^N_{k=1}{R_k(\cos{(\phi_k-\phi_j)}} + c_1\sin{(\phi_k-\phi_j))},
$$

$$
\phi^\prime_j = \Omega_j + \epsilon c_1 N + \epsilon\displaystyle\frac{1}{R_j}\sum_{k=1}^N{R_k(\sin(\phi_k-\phi_j)-c_1\cos(\phi_k-\phi_j))}.
$$

$$
\dot{R}_j=f(R_j)+\epsilon g_j(R,\theta)  
$$

$$
\dot{\phi}_j= \Omega_j +\epsilon h_j(R,\theta)
$$

$$
g_j (R,\phi) = -R_j N + \sum^N_{k=1}{R_k(\cos{(\phi_k-\phi_j)}} + c_1\sin{(\phi_k-\phi_j))}
$$

$$
h_j(R,\phi) = c_1N + \displaystyle\frac{1}{R_j}\sum_{k=1}^N{R_k(\sin(\phi_k-\phi_j))-c_1\cos(\phi_k-\phi_j)}
$$

Будем искать решение $R_j^\prime=0$ в виде ряда $R_j=R_j^{(0)}+\epsilon R_j^{(1)} + \dots$

Для первого порядка $\epsilon$:

$$\dot{R}_j^{(0)}=f(R_j^{(0)}), \quad f(R_j^{(0)})=R_j^{(0)}(1-\displaystyle\frac{1}{4}(R_j^{(0)})^2), \text{откуда } R_j^{(0)}=2.$$

Для первого порядка $\epsilon$:

$$
0 = (R_j^{(0)}+\epsilon R_j^{(1)}) (1-\displaystyle\frac{1}{4}(R_j^{(0)}+\epsilon R_j^{(1)})^2-\epsilon N ) +\epsilon \sum^N_{k=1}R_k^{(1)}[\cos{(\phi_k-\phi_j)}+c_1\sin{(\phi_k-\phi_j)}]
$$

$$
0 = R_j^{(0)} - \displaystyle\frac{1}{4} (R_j^{(0)})^3 -\frac{1}{2}\epsilon (R_j^{(0)})^2R_j^{(1)} -\frac{1}{4}\epsilon^2 R_j^{(0)}(R_j^{(1)})^2 - \epsilon N R_j^{(0)} + \epsilon R_j^{(1)} - \frac{1}{4}\epsilon(R_j^{(0)})^2R_j^{(1)} - \\ - \frac{1}{2}\epsilon^2R_j^{(0)}(R_j^{(1)})^2 - \frac{1}{4}\epsilon^3(R_j^{(1)})^3 - \epsilon^2 R_j^{(1)}N  +\epsilon \sum^N_{k=1}R_k^{(1)}[\cos{(\phi_k-\phi_j)}+c_1\sin{(\phi_k-\phi_j)}]
$$

$$
 R_j^{(1)} (1-\displaystyle\frac{3}{4}(R_j^{(0)})^2) -  NR_j^{(0)} + \sum^N_{k=1}R_k^{(1)}[\cos{(\phi_k-\phi_j)}+c_1\sin{(\phi_k-\phi_j)}]=0
$$

$$
 R_j^{(1)} = \displaystyle\frac{NR_j^{(0)} - \sum^N_{k=1}R_k^{(1)}[\cos{(\phi_k-\phi_j)}+c_1\sin{(\phi_k-\phi_j)}]} {(1-\displaystyle \frac{3}{4}(R_j^{(0)})^2)}
$$

$$
 R_j^{(1)} =  \displaystyle\frac{-g_j(R^{(0)},\phi)} {f^\prime(R_j^{(0)}) } = \frac{g_j(R^{(0)},\phi)}{2}
$$

$$
R_j = 2 + \epsilon \Big[-N + \frac{1}{2} \displaystyle\sum^N_{k=1}R_k^{(1)} \Big( \cos{(\phi_k-\phi_j)} +c_1\sin{(\phi_k-\phi_j)}  \Big)  \Big]
$$

Используем полученное разложение:

$$
 \phi^\prime_j=\Omega_j+\epsilon c_1N + \epsilon\sum_{k=1}^N\Big[  1+\displaystyle\frac{\epsilon}{2} (R_k^{(1)}-R_j^{(1)}) \Big] [\sin{(\phi_k-\phi_j)}-c_1\cos{(\phi_k-\phi_j)}]
$$

После некоторых преобразований:

$$
 \phi^\prime_j=\Omega_j+\epsilon c_1N + \epsilon\sum_{k=1}^N\Big[  1+\displaystyle\frac{\epsilon}{2} (R_k^{(1)}-R_j^{(1)}) \Big] d_1\sin{(\phi_k-\phi_j-\gamma)},
$$

где $d_1=\sqrt{1+c_1^2}$.

Подставляя $R_j^{(1)}$ в выражение для $\phi^\prime_j$, после некоторых преобразований получаем:

$$
 \phi^\prime_j=\Omega_j+\epsilon N \Big( c_1 + d_1 Im \big[e^{-i\gamma}Z_1e^{-i\phi_j}\big]  \Big) + \displaystyle \frac{d_1\epsilon^2 N^2}{4} \Big( Im \big[ (1+c_1)e^{-i\gamma}Z_1^*Z_2e^{-i\phi_j} \big] + \\ + Im \big[ (1-ic_1)e^{-i\gamma}Z_1e^{-i\phi_j} \big] -  Im \big[ (1-ic_1)e^{-i\gamma}Z_1^2e^{-2i\phi_j} \big]   \Big),
$$

где

$Z_1=Pe^{i\Psi}=\displaystyle\frac{1}{N}\sum_{k=1}^N e^{i\phi_k},$

$Z_2=Qe^{i\Phi}=\displaystyle\frac{1}{N}\sum_{k=1}^N e^{2i\phi_k}.$

Тогда:

$$
\phi^\prime_j = (\Omega_j+\epsilon c_1N) + \epsilon d_1NP\sin{(\Psi-\phi_j-\gamma)} + \displaystyle\frac{d_1\epsilon^2 N^2}{4} \Big( sgn(\beta)PQ\sin{(\Phi-\Psi-\phi_j)} - \\ - P\sin{(\Psi-\phi_j + \vartheta)} + P^2\sin{(2(\Psi-\phi_j)+\vartheta)} \Big),
$$

где

$\vartheta = \arg\Big(  \displaystyle\frac{(\alpha+i\beta)^2}{\beta\sqrt{\alpha^2+\beta^2}}  \Big)$.
''')



