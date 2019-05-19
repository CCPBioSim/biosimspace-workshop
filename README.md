# Introduction to BioSimSpace

## Aimed at
Anyone interested in learning how to use the new CCP-BioSim
[BioSimSpace](https://github.com/michellab/BioSimSpace) Python environment for easy setup, running, management and analysis of biomolecular simulations.

## Requirements
Knowledge of Python, e.g. as gained from the
<a href="https://ccpbiosim.github.io/python_and_data" target="_blank">Python for Biomolecular Modellers</a> workshop.

## Abstract

BioSimSpace is the new flagship software being produced in partnership with CCP-BioSim/HEC-BioSim. The software provides an easy-to-use Python environment for manipulating biomolecules, running simulations, and analysing / visualising outputs. BioSimSpace hides the details of using individual simulation and analysis packages behind a common, simple Python interface. This enables you to setup, run and analyse simulations using, e.g. Amber, NAMD or Gromacs, all from the same Python script or Jupyter Python interface.

## Training Material

The workshop consists of a series of Jupyter notebooks. These are available on the
<a href="https://notebook.biosimspace.org" target="_blank">workshop jupyter server</a>
and can be downloaded from the <a href="https://github.com/ccpbiosim/biosimspace_workshop" target="_blank">GitHub repository</a>.

Once you have started the server, navigate to the `biosimspace_workshop` directory and you will find the
notebooks there. These training materials will teach you more about BioSimSpace, including how to write your own BioSimSpace code. The material is split into two parts.

### Part 1: Molecular Dynamics

* [01_introduction.ipynb](html/01_introduction.html) : This notebook introduces the goals of BioSimSpace and shows you how to easily configure and run molecular-dynamics simulations and interact with them in real time.
* [02_writing_nodes.ipynb](html/02_writing_nodes.html) : This notebook shows you how to use BioSimSpace to write an interoperable workflow component, called a node. This node is independent of the underlying software packages.
* [03_running_nodes.ipynb](html/03_running_nodes.html) : This notebook shows you the various ways of running BioSimSpace nodes.
* Excercises 

### Part 2: Molecular Setup

* [04_molecular_setup.ipynb](html/04_molecular_setup.html) : This notebook shows you how to use BioSimSpace to parameterise and solvate molecules.
* Excercise
