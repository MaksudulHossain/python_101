from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """ A class to generate random walks"""
    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_vals = [0]
        self.y_vals = [0]

    def get_step(self):
        xy_direction = choice([-1,1])
        xy_distance = choice([1,2,3,4])
        xy_step = xy_direction * xy_distance
        return xy_step

    def fill_walk(self):
        while len(self.x_vals) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue
                
            next_x = self.x_vals[-1] + x_step
            next_y = self.y_vals[-1] + y_step

            self.x_vals.append(next_x)
            self.y_vals.append(next_y)

def main():
    while True:
        rw = RandomWalk(5000)
        rw.fill_walk()

        plt.figure(dpi=128, figsize=(10,6))
        point_numbers = list(range(rw.num_points))
        plt.scatter(0,0,c='green',edgecolors='none',s=100)
        plt.scatter(rw.x_vals,rw.y_vals,
                    c=point_numbers,
                    cmap=plt.cm.Blues,
                    edgecolors='none',
                    s=3)
        
        # plt.plot(rw.x_vals,rw.y_vals,
        #             linewidth=2)
        
        # plt.axes().get_xaxis().set_visible(False)
        # plt.axes().get_yaxis().set_visible(False)
        plt.xticks([])
        plt.yticks([])

        plt.show()
        keep_running = input("Make another walk? (y/n): ")
        if keep_running=='n':
            break
if __name__ == '__main__':
    main()

