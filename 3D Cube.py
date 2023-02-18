from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
x = [0, 1, 1, 0, 0, 1, 1, 0]
y = [0, 0, 1, 1, 0, 0, 1, 1]
z = [0, 0, 0, 0, 1, 1, 1, 1]

# Plot the vertices
ax.scatter(x, y, z)

# Connect the vertices to create the faces of the cube
for i in range(4):
    ax.plot([x[i], x[i+4]], [y[i], y[i+4]], [z[i], z[i+4]])
for i in range(0, 8, 2):
    ax.plot([x[i], x[i+1]], [y[i], y[i+1]], [z[i], z[i+1]])
for i in range(0, 8, 4):
    ax.plot([x[i], x[i+2]], [y[i], y[i+2]], [z[i], z[i+2]])

plt.show()
