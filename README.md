# Newtownian-Physics-Engine
Copying the human brain is a wide ranging field that stretches from intuitively coding thought all the way to literally dissecting and rebuilding the physical makeup of the brain. Many believe this is what will kickstart the Technological Singularity. The dark horse candidate to kickstart the singularity is universe simulation,  which, if videogames are any indication, will be the only algorithmic, comprehensive, exhaustive search for lifelike intelligence available. Below is the code for a simple simulation  and animation of neutrons in spacetime, an incomplete snapshot of our own universe in its very early stages.

In this project i reduced the universe and physics down to what i consider the fun stuff - ballistics. What you're seeing here is an accurate ballistic simulation of 10 neutrons in space - accurate except for the timescale and nuclear forces. 

It was one of my first projects and i made it primarily for one reason - i believe universe simulation is the dark horse candidate to kickstart the singularity. Anyway, here's an extended video on this animation:

The code features:

- databases
- animation scripting, including creating new meshes, addimg materials and applying particle systems (for the trails) to each of them
- accurate physical modelling using timesteps

The code is broke up into two files. Run the simulation script and you'll be left with the location data of the particles. The animation script animates the scene. 

My idea with that position data is that i could auto label a universe simulation. Inspired by Stephen Wolfram's cellular automata, i would be looking for what i call a set of injection vectors
