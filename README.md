3D Cube Simulation with Pygame and OpenGL
Overview
This project is a 3D cube simulation built using Python, Pygame, and OpenGL. It generates a series of cubes that move through a 3D space. The camera's movement is controlled by the arrow keys and mouse, allowing you to explore the generated environment.

Features
3D Cube Rendering: Displays multiple cubes in a 3D space using OpenGL.
Camera Control: Navigate the environment using the arrow keys and zoom in/out with the mouse scroll wheel.
Randomized Cube Positions: Cubes are randomly placed within the scene to create a dynamic visual effect.
Controls
Arrow Keys: Move the camera around the scene.
Mouse Scroll Wheel: Zoom in/out of the scene.
Dependencies
To run this project, you need to have the following Python packages installed:

pygame
PyOpenGL
You can install the dependencies using pip:

bash
Copy code
pip install pygame PyOpenGL
How to Run
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/3d-cube-simulation.git
Navigate to the project directory:
bash
Copy code
cd 3d-cube-simulation
Run the script:
bash
Copy code
python main.py
Code Structure
main.py: The main script that initializes the Pygame window, sets up the 3D perspective, and handles user input to control the camera and interact with the cubes.
cube(): Renders a cube using vertices, edges, and surfaces.
set_vertices(): Randomly generates the positions of the cubes in the scene.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contribution
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

