import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


def visualize():
    unis = {'Moscow': 27, 'Saint-Petersburg': 17}
    unis['other'] = 352 - sum(unis.values())
    plt.title('Distribution of technical unis in Russia')
    plt.pie(list(unis.values()), explode=[0.1]*len(unis), labels=list(unis.keys()),
            autopct=lambda pct: f'{round(pct * 352 / 100)}', shadow=True)
    plt.axis('equal')

    plt.show()


if __name__ == '__main__':
    visualize()
