# msLWLink
Megascans to Lightwave3D link plugins.

This project is an attept to build a set of scripts to allow the export of Megascans objects, surfaces, atlases and other assets directly into Lightwave3D Modeler or Layout.

Roadmap:

1: Get Bridge and Lightwave talking to each other via the 'export to' option in Bridge.
2: Get Lightwave to accept an exported FBX format 3D Asset and automaticaly set up LW native PBSDF surfaces(1)
2.1: Add Octane surfaces to the options.  
3: Add surfaces to an existing, selected object surface.

Longer range goals:
4: (Modeler) Create a method to bring atlases into Lightwave3D and automatically set up seperate layers with appropriate UV layout to allow instancing and scattering of the Atlas "pieces". 
5: There is no 5.   
6: Other ideas as they percolate up from the deep recesses of my brain or more likely, come in from others using Megascans and Lightwave.


footnotes: 
(1) - Standard (and other) material types are either deprecated or too specific to be reasonably handled by this plugin/script at this time.   Megascans is a PBR based collection of assets and I intend to focus on PBSDF and Octane surfacing for now.  
