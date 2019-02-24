# PyOpenGLobe
A 3D OpenGL rendered Sphere with an applied texture in a PyGame window. A personal project to get acquainted with basics of OpenGL and PyGame. I opted to use PyGame to display the sphere, instead of PyOpenGL itself, since this allowed me to take user input to rotate the sphere and zoom in and out.

## Usage
Run the globe.py in whichever way you usually run python files.

## Features
* Displays OpenGL rendered sphere in PyGame window
* Sphere has a spherically-mapped Earth texture
* Rotate sphere with arrow keys or by clicking and dragging with mouse
* Zoom in and out with the mouse wheel

## Screenshots
<img width="300" alt="screenshot" src="https://user-images.githubusercontent.com/40459599/53302550-80756c00-3857-11e9-9474-9cee0f51d19c.png">

## Requirements
* Python 3
* PyGame
* PyOpenGL
* PIL or Pillow
* Numpy

## Some Notes on What I Learned
I learned a lot about how to render 3D objects in OpenGL. Creating the sphere and displaying it in a PyGame window was relatively straightforward. The challenge was applying a texture to it. I also struggled with the click and drag code that allows the user to rotate the sphere using the mouse. Some very useful StackOverflow answers helped me to implement these features.

I learned how PyGame intercepts user input as 'events' and how to use these to control the way the sphere is rendered. Initially, this program ran very slowly on my computer as I had not properly optimised the code and it was necessarily rerendering the sphere each frame. After some optimisations, the program now runs properly and the sphere can be interacted with smoothly.

I am now confident with rendering 3D object with PyOpenGL. This code could be extended into a full 3D World Map, or to display planet maps in 3D, useful in Astronomy, my undergraduate degree subject.

## License
This project is licensed under the terms of the MIT license. Do whatever you want with it!

## Acknowledgements
* A great tutorial that I used to get started with PyOpenGL: https://www.youtube.com/watch?v=R4n4NyDG2hI
* Texturing a sphere from: https://stackoverflow.com/questions/42986754/pyopengl-sphere-with-texture?answertab=oldest#tab-top 
* Click and drag from: http://goldsequence.blogspot.com/2017/04/using-mouse-for-object-zoom-inzoom.html
* Texture image from: http://planetpixelemporium.com/earth.html
