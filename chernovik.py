
st.markdown(r'''
$$
\displaystyle\frac{\pi}{4} \, \text{-- притягивающая связь, синфазная синхронизация}
$$
''')

# Список изображений
images = ['exp1/pi_4/order_parametr/1.png', 'exp1/pi_4/phi(j)/1.png', 'exp1/pi_4/synch_circle/1.png', 'exp1/pi_4/spatiotemporal/1.png']

# Переменная для отслеживания текущего индекса изображения
current_index = st.session_state.get('current_index', 0)

# Функция для обработки нажатия на кнопку "Вперед"
def next_image():
    st.session_state.current_index = (current_index + 1) % len(images)

# Функция для обработки нажатия на кнопку "Назад"
def previous_image():
    st.session_state.current_index = (current_index - 1) % len(images)

# Размещаем изображение в первой строке
st.image(Image.open(images[current_index]), caption=f'Выбранное изображение: {current_index + 1}/{len(images)}')

# Размещаем кнопки "Назад" и "Вперед" в одной строке
button_container = st.container()
with button_container:
    col1, col2, col3 = st.columns([10, 5, 70])
    with col1:
        if st.button('Назад'):
            previous_image()
    with col3:
        if st.button('Вперед'):
            next_image()
