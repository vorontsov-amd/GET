import numpy as np
import matplotlib.pyplot as plt


with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
dt = tmp[1]

data_array = np.loadtxt("data.txt", dtype=int)
data_array = 3.3 * data_array / 256
time = np.linspace(0, dt * (len(data_array) - 1), len(data_array))

fig, ax = plt.subplots(figsize=(16, 10), dpi=400)
ax.plot(time, data_array, label='V(t)', color='r', linewidth=3) 
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, c")
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.legend(fontsize = 10,
          ncol = 1,    #  количество столбцов
          facecolor = 'oldlace',    #  цвет области
          edgecolor = 'r',    #  цвет крайней линии
          title = 'Данные',    #  заголовок
          title_fontsize = '10'    #  размер шрифта заголовка
         )
ax.grid(which='major',
        color = 'k')

ax.minorticks_on()

ax.grid(which='minor',
        color = 'gray',
        linestyle = ':')


yMax = np.max(data_array)
ax.set_xlim([0, dt * (len(data_array) - 1)])
ax.set_ylim([0, yMax + 1])

vMax = np.argmax(data_array)
t1 = time[vMax]
t2 = time[-1] - t1
ax.text(t1, yMax + 0.33, "Время зарядки " + str(round(t1, 3)))
ax.text(t1, yMax + 0.66, "Время разрядки " + str(round(t2, 3)))


#plt.show()
fig.savefig("save.svg")

#print(data_array)