from random import choice

class RandomWalk:
    """ a class to generate random walks."""
    def __init__(self,num_points=5000):
        self.num_points=num_points
        #All walks starts from (0,0)

        self.x_values=[0]
        self.y_values=[0]
        self.walk()
    def get_step(self):
        #decide which direction to go and how far to go in that direction.

        x_direction= choice([1,-1])
        x_distance=choice([0,1,2,3,4,5,6,7,8])
        x_step= x_direction * x_distance
        y_direction=choice([1,-1])
        y_distance=choice([0,1,2,3,4,5,6,7,8])
        y_step=y_direction * y_distance
        return x_step,y_step

    def walk(self):
        """calculate all the points in the walk"""
        """keep taking steps until the walk reaches the desired length."""
        while len (self.x_values)< self.num_points:

            x_step,y_step=self.get_step()
            #Reject moves that gonowhere.
            if x_step==0 and y_step==0:
                continue

            #Calculate the new position.
            x=self.x_values[-1] + x_step
            y=self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
