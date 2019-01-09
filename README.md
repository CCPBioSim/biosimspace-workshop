# Introduction to BioSimSpace

## Aimed at:
Anyone interested in learning how to use the new CCP-BioSim
[BioSimSpace](https://github.com/michellab/BioSimSpace) Python environment for easy setup, running, management and analysis of biomolecular simulations.

## Requirements:
Knowledge of Python, e.g. as gained from the
<a href="https://ccpbiosim.github.io/python_and_data" target="_blank">Python for Biomolecular Modellers</a> workshop.

## Abstract:
BioSimSpace is the new flagship software being produced in partnership with CCP-BioSim/HEC-BioSim. The software provides an easy-to-use Python environment for manipulating biomolecules, running simulations, and analysing / visualising outputs. BioSimSpace hides the details of using individual simulation and analysis packages behind a common, simple Python interface. This enables you to setup, run and analyse simulations using, e.g. Amber, NAMD or Gromacs, all from the same Python script or Jupyter Python interface.

## Demonstration

We will start with a set of demonstrations of what you can do with BioSimSpace. These are a set of Jupyter notebooks. These are available on the 
<a href="https://ccpbiosim.github.io/workshop/events/leeds2019/server.html" target="_blank">workshop jupyter server</a>
and can be downloaded from the <a href="https://github.com/ccpbiosim/biosimspace_workshop" target="_blank">GitHub repository</a>.

Once you have started the server, navigate to the `biosimspace_demo` directory and you will find the following notebooks there:

1. interactive_md.ipynb : This notebook demonstrates how BioSimSpace can be used to run an interactive molecular dynamics simulation on the cloud
2. input_files.ipynb : This notebook demonstrates how BioSimSpace can be used to generate the input files to run molecular dynamics or minimisation using a range of different packages. You can download these input files to run the simulations on your own computer or HPC cluster.
3. conversion.ipynb : This notebook demonstrates how BioSimSpace can be used to convert molecule input files from one format to another.
4. interactive_setup.ipynb : This notebook demonstrates how BioSimSpace can be used to automate the parameterisation and solvation of ligands and proteins using a range of forcefields and water models, producing input files for different MD packages.

## Training Material

The workshop consists of a series of Jupyter notebooks. These are available on the 
<a href="https://ccpbiosim.github.io/workshop/events/leeds2019/server.html" target="_blank">workshop jupyter server</a>
and can be downloaded from the <a href="https://github.com/ccpbiosim/biosimspace_workshop" target="_blank">GitHub repository</a>.

Once you have started the server, navigate to the `biosimspace_workshop` directory and you will find the
notebooks there. These training materials will teach you more about BioSimSpace, including how to write your own BioSimSpace code. These include:

1. 01_introduction.ipynb : This notebook introduces you to the goals of BioSimSpace and how to run BioSimSpace Python scripts on your own computer from the command line.
2. 02_writing_nodes.ipynb : This notebook introduces you to the concept of a workflow node, and how to use BioSimSpace to write the Python scripts that you ran in 01_introduction.ipynb. This includes learning how to add interactive features to your Python script using a Jupyter notebook.
3. 03_interactive_md.ipynb : This notebook shows you how to write a BioSimSpace node that can be used to run molecular dynamics simulations, including the interactive simulations of the type shown in the demo.
4. 04_molecular_setup.ipynb : This notebook shows you how to write a BioSimSpace node that parameterises and solvate different molecules, including how to add interactive features. This will show you how to write notebooks of the type shown in the demo.
