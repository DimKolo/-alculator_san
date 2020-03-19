from tkinter import *
from tkinter.ttk import Radiobutton
import math

""" Создание окна программы с указанием настроек. """
window = Tk()
window.title("Калькулятор площади геометрических фигур.")
window.geometry('960x540') # ширина=960, высота=540
window.resizable(False, False) # запрещает разворот экрана

""" Вывод рамки для левого и правого меню, с запросом выбора фигуры. """
left_label_frame = LabelFrame(window, text = 'Меню выбора фигуры для расчёта площади', width=270, height=500)
left_label_frame.place(x=10, y=10)
right_label_frame = LabelFrame(window, text = 'Брутальный калькулятор', width=600, height=500)
right_label_frame.place(x=320, y=10)
supplication = Label(right_label_frame, text="Выберите фигуру", font=("Arial Bold", 50))
supplication.place(x=20, y=100)

def circle_GO():
    """ Функция, реагирующая на нажатие кнопки выбора фигуры(Круга) и запускающая необходимые запросы для расчёта. """

    # Обновление правой части калькулятора (ничего лучше не сработало).
    right_label_frame = LabelFrame(window, text='Брутальный калькулятор', width=600, height=500)
    right_label_frame.place(x=320, y=10)

    # Первый запрос (выбор способа расчёта).
    first_question_circle = Label(right_label_frame, text="1) Выберите каким способом будет получен расчёт:")
    first_question_circle.place(x=20, y=30)

    def conclusion():
        """ Вывод расчёта пользователю когда тот введёт необходимые данные. """
        data_output = Label(right_label_frame, text="3) Получен результат:")
        data_output.place(x=20, y=300)

    # Вывод трёх переключателей для выбора пользователем, от которых зависит метод расчёта.
    selected = IntVar()
    rad1 = Radiobutton(right_label_frame, text='Известен радиус', value=1, variable=selected)
    rad2 = Radiobutton(right_label_frame, text='Известен диаметр', value=2, variable=selected)
    rad3 = Radiobutton(right_label_frame, text='Известна длина окружности', value=3, variable=selected)
    rad1.place(x=25, y=60)
    rad2.place(x=25, y=90)
    rad3.place(x=25, y=120)

    def data_request():
        """ Функция вывода второго вопроса с запросом известной величины и самой калькуляцией. """

        # Вывод поля для заполнения известной величиной.
        message = DoubleVar()
        entry = Entry(right_label_frame, width=10, textvariable=message)
        entry.place(x=25, y=233)

        def calculation_for():
            """ Калькуляция(расчёт площади круга по формулам). """

            if selected.get() == 1:
                # Расчёт площади круга по радиусу.
                r = message.get()
                S = math.pi * (r ** 2)
                # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)
            elif selected.get() == 2:
                # Расчёт площади круга по диаметру.
                d = message.get()
                S = 0.25 * math.pi * (d ** 2)
               # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)
            elif selected.get() == 3:
                # Расчёт площади круга по длине окружности.
                L = message.get()
                S = (L ** 2) / (4 * math.pi)
                # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)

        # Кнопка подтверждения ввода известных величин. Требование рассчитать при нажатии.
        btn_calculation = Button(right_label_frame, text="Рассчитать!", command=calculation_for)
        btn_calculation.place(x=100, y=230)

        # Вывод второго вопроса.
        second_question_circle = Label(right_label_frame, text="2) Введите известную величину в появившемся окне и нажмите на кнопку рассчёта.")
        second_question_circle.place(x=20, y=200)

    # Кнопка подтверждения выбора метода расчёта.
    button_right_menu1 = Button(right_label_frame, text="Выбрать!", command=data_request)
    button_right_menu1.place(x=25, y=150)

def triangle_GO():
    """ Функция, реагирующая на нажатие кнопки выбора фигуры(Треугольника) и запускающая необходимые запросы для расчёта. """

    # Обновление правой части калькулятора (ничего лучше не сработало).
    right_label_frame = LabelFrame(window, text='Брутальный калькулятор', width=600, height=500)
    right_label_frame.place(x=320, y=10)

    # Первый запрос (выбор способа расчёта).
    first_question_triangle = Label(right_label_frame, text="1) Выберите каким способом будет получен расчёт:")
    first_question_triangle.place(x=20, y=30)

    def conclusion():
        """ Вывод расчёта пользователю когда тот введёт необходимые данные. """
        data_output = Label(right_label_frame, text="3) Получен результат:")
        data_output.place(x=20, y=300)

    # Вывод трёх переключателей для выбора пользователем, от которых зависит метод расчёта.
    selected = IntVar()
    rad1 = Radiobutton(right_label_frame, text='Известна сторона (Значение_1) и высота (Значение_2)', value=1, variable=selected)
    rad2 = Radiobutton(right_label_frame, text='Известны две стороны (Значение_1, Значение_2) и угол между ними (Значение_3 (в градусах))', value=2, variable=selected)
    rad3 = Radiobutton(right_label_frame, text='Известны три стороны (Значение_1, Значение_2, Значение_3)', value=3, variable=selected)
    rad1.place(x=25, y=60)
    rad2.place(x=25, y=90)
    rad3.place(x=25, y=120)

    def data_request():
        """ Функция вывода второго вопроса с запросом известной величины и самой калькуляцией. """

        # Вывод полей для заполнения известными величинами.
        message_01, message_02, message_03 = DoubleVar(), DoubleVar(), DoubleVar()
        entry_01 = Entry(right_label_frame, width=10, textvariable=message_01)
        entry_01.place(x=95, y=233)
        entry_02 = Entry(right_label_frame, width=10, textvariable=message_02)
        entry_02.place(x=245, y=233)
        entry_03 = Entry(right_label_frame, width=10, textvariable=message_03)
        entry_03.place(x=395, y=233)
        entry_01_description = Label(right_label_frame, text="Значение_1:")
        entry_01_description.place(x=20, y=233)
        entry_02_description = Label(right_label_frame, text="Значение_2:")
        entry_02_description.place(x=170, y=233)
        entry_03_description = Label(right_label_frame, text="Значение_3:")
        entry_03_description.place(x=320, y=233)

        # Запрет вывода поля для Значения_3 в случае выбора 1-го способа расчёта.
        if selected.get() == 1:
            entry_03.place_forget()
            entry_03_description.place_forget()

        def calculation_for():
            """ Калькуляция(расчёт площади треугольника по формулам). """

            if selected.get() == 1:
                # Расчёт площади треугольника по стороне и высоте.
                a = message_01.get()
                h = message_02.get()
                S = 0.5 * (a * h)
                # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)
            elif selected.get() == 2:
                # Расчёт площади треугольника через две стороны и угол между ними.
                a = message_01.get()
                b = message_02.get()
                sin_a = int(message_03.get())
                # Конвертирую градусы в радианы для определения синуса угла. С последующим расчётом площади.
                S = 0.5 * a * b * math.sin(math.radians(sin_a))
               # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)
            elif selected.get() == 3:
                # Расчёт площади треугольника по трём сторонам.
                a = message_01.get()
                b = message_02.get()
                c = message_03.get()
                p = (a + b + c) / 2
                S = math.sqrt(p * (p - a) * (p - b) * (p - c))
                # Вывод расчёта пользователю с округлением.
                conclusion()
                data_output_conclusion = Label(right_label_frame, text=round(S, 2), font=("Arial Bold", 50))
                data_output_conclusion.place(x=20, y=350)

        # Кнопка подтверждения ввода известных величин. Требование рассчитать при нажатии.
        btn_calculation = Button(right_label_frame, text="Рассчитать!", command=calculation_for)
        btn_calculation.place(x=500, y=230)

        # Вывод второго вопроса.
        second_question_triangle = Label(right_label_frame, text="2) Введите известную величину в появившемся окне и нажмите на кнопку рассчёта.")
        second_question_triangle.place(x=20, y=200)

    # Кнопка подтверждения выбора метода расчёта.
    button_right_menu1 = Button(right_label_frame, text="Выбрать!", command=data_request)
    button_right_menu1.place(x=25, y=150)

""" Кнопки в левом меню, при нажатии на которые срабатывает функционал в правой рамке Калькулятора. """
button_left_menu1 = Button(left_label_frame, text='1. Круг', width=20, height=1, bg='gray', fg='white', font='arial 14', anchor="w", command=circle_GO)
button_left_menu1.place(x=15, y=100)
button_left_menu2 = Button(left_label_frame, text='2. Треугольник', width=20, height=1, bg='gray', fg='white', font='arial 14', anchor="w", command=triangle_GO)
button_left_menu2.place(x=15, y=150)
button_left_menu_quit = Button(left_label_frame, text='Выход из программы', width=20, height=1, bg='gray', fg='white', font='arial 14', command=window.destroy)
button_left_menu_quit.place(x=15, y=400)

""" Запуск программы. """
window.mainloop()