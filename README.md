# Newtownian-Physics-Engine

There are some dependencies for this project. On Ubuntu 21.04, I did:

```
pip3 install pandas
```

You'll also need Blender3D, which you can get from here: https://www.blender.org/

In this project I reduced the universe and physics down to what i consider the fun stuff - ballistics. What you're seeing here is an accurate ballistic simulation of 10 neutrons in space - accurate except for the timescale and nuclear forces. It was one of my first projects and i made it primarily for one reason - i believe universe simulation is the dark horse candidate to kickstart the singularity. Anyway, here's an extended video on this animation:

The code features:

- databases
- animation scripting, including creating new meshes, adding materials, keyframing motion, and applying particle systems (for the trails) to each of them
- accurate physical modelling using timesteps

The code is broke up into two files. Run the simulation script and you'll be left with the location data of the particles. The animation script animates the scene. 

My idea with the position data is that I could auto label a universe simulation. Inspired by Stephen Wolfram's cellular automata, i would be looking for an initialization vector (velocity, acceleration, position, universal constants, etc.) that produces interesting phenomenon. For example, because all the particles just have gravity acting on them, the particles will eventually all occupy the same position. So I might auto label reward for initialization vectors that result in a longer lasting universe simulation. I go more in depth in this video: https://www.youtube.com/watch?v=DVxFjD7zNac&t=7s

Side Note: I plan on giving this repo a major update, including a GUI and the capability to algorithmically select initialization vectors based on a variety of parameters. So if you're interested, leave a star and watch for an update.
