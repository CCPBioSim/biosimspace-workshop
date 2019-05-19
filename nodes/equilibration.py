#!/usr/bin/env python
# coding: utf-8

# Author: Lester Hedges<br>
# Email:&nbsp;&nbsp; lester.hedges@bristol.ac.uk
# 
# # Equilibration
# 
# A node to perform equilibration of a molecular system.

# In[ ]:


import BioSimSpace as BSS


# In[ ]:


node = BSS.Gateway.Node("A node to perform equilibration and save the equlibrated molecular configuration to file.")
node.addAuthor(name="Lester Hedges", email="lester.hedges@bristol.ac.uk", affiliation="University of Bristol")
node.setLicense("GPLv3")


# Set the input requirements:

# In[ ]:


node.addInput("files", BSS.Gateway.FileSet(help="A set of molecular input files."))

node.addInput("runtime", BSS.Gateway.Time(help="The run time.",
                                          unit="nanoseconds",
                                          minimum=0*BSS.Units.Time.nanosecond,
                                          maximum=10*BSS.Units.Time.nanosecond,
                                          default=0.2*BSS.Units.Time.nanosecond))

node.addInput("temperature_start", BSS.Gateway.Temperature(help="The initial temperature.",
                                                           unit="kelvin",
                                                           minimum=0*BSS.Units.Temperature.kelvin,
                                                           maximum=1000*BSS.Units.Temperature.kelvin,
                                                           default=0*BSS.Units.Temperature.kelvin))

node.addInput("temperature_end", BSS.Gateway.Temperature(help="The final temperature.",
                                                         unit="kelvin",
                                                         minimum=0*BSS.Units.Temperature.kelvin,
                                                         maximum=1000*BSS.Units.Temperature.kelvin,
                                                         default=300*BSS.Units.Temperature.kelvin))

node.addInput("restrain_backbone", BSS.Gateway.Boolean(help="Whether to restrain the backbone.",
                                                       default=False))


# We now need to define the output of the node. In this case we will return a set of files representing the equilibrated molecular system.

# In[ ]:


node.addOutput("equilibrated", BSS.Gateway.FileSet(help="The equilibrated molecular system."))


# If needed, here are some input files again. These can then be re-uploaded using the GUI.
# 
# AMBER files: [ala.crd](../input/ala.crd), [ala.top](../input/ala.top)
# 
# GROMACS: [kigaki.gro](https://raw.githubusercontent.com/michellab/BioSimSpace/devel/demo/gromacs/kigaki/kigaki.gro), [kigaki.top](https://raw.githubusercontent.com/michellab/BioSimSpace/devel/demo/gromacs/kigaki/kigaki.top)
# 
# Now show the GUI.

# In[ ]:


node.showControls()


# Generate the molecular system.

# In[ ]:


system = BSS.IO.readMolecules(node.getInput("files"))


# Set up the equilibration protocol.
# 
# (Note that the keyword arguments happen to have the same name as the input requirements. This need not be the case.)

# In[ ]:


protocol = BSS.Protocol.Equilibration(runtime=node.getInput("runtime"), temperature_start=node.getInput("temperature_start"), temperature_end=node.getInput("temperature_end"), restrain_backbone=node.getInput("restrain_backbone"))


# Start the MD equilibration.

# In[ ]:


process = BSS.MD.run(system, protocol)


# Get the equilibrated molecular system and write to file in the same format as the input.

# In[ ]:


node.setOutput("equilibrated", BSS.IO.saveMolecules("equilibrated", process.getSystem(block=True), system.fileFormat()))


# Validate the node.

# In[ ]:


node.validate()

