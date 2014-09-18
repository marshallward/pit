Manifesto
=========

Goal: uniquely identify every experiment. Retain history of changes to input
parameters and files, and executable.

An experiment is defined as a directory, containing all the necessary
components to run the model. This does not necessarily mean all inputs must be
physically located in the experiment directory, but the means to find those
inputs must be defined by an input file located in the directory.

All components that are essential to running the experiment (inputs) must
themselves be uniquely identified. This will probably take the form of a hash
function. The unique ID of each input need not be intimately associated with
the input as we can regenerate that ID at will. For the case of input data the
ID serves as verification. This means the unique ID must be defined in any
configuration file that references an input data file along with the path to
the input file. If the generated ID of the input file does not match that in
the configuration file the control software/script must either locate the input
file, stop execution and raise an error, or modify the configuration file to
include the correct ID. The latter then corresponds to an alteration to the
experiment.

The executable used in the experiment must also have a unique identifier.
Tracking changes to the executable is a separate task, but using the same
principles as are outlined in this document, and considering the compilation of
the executable as an experiment, means the state of the executable can also be
similarly forensically tracked, and it's state identified by reference to it's
unique ID.

The proposal is to use existing distributed revision control (DRC) software for
the task of tracking changes in the experimental directory. These changes
represent a comprehensive history of the experiment, as they capture changes to
all the inputs, the executable and the status of each invocation, i.e. if the
executable ran without error.

Modern DRC systems generates a unique identifier for the state of the text
files they monitor. To be compliant with the principals of forensic experiment
tracking all configuration files necessary for the experiment to run must be
monitored by the DRC system. As all input data that is defined within these
configuration files is associated with a unique ID the state of the input data
files will also be captured by the revision control system.

At it's most basic, starting an experiment can consist of creating a directory
and copying into it the various input and configuration files that are
required. It may be tools can be used to collect the necessary input files, and
create the configuration files, but it is not a necessary requirement. What is
required is that the software (usually a script of some sort) that runs the
experiment performs the following steps:

1. Check input data have correct IDs. If not the input data with the correct ID
   must be found (and used), or the execution must stop and flag an error, or
   the ID in the configuration file must be changed to match the input data.
   Ideally this would be done before the main executable is run. If the input
   files are large and calculating the ID is prohibitively time consuming this
   step can be run in parallel with the main executable but working in this
   mode allows for no pre-checks and sourcing correct input data files in the
   case of an ID mismatch. Thus this mode only allows for the third option,
   which is changing the experimental configuration.

2. Once the experiment has finished the state, that is the success or otherwise
   of the experimental run must be logged in a file that is under the control
   of the DRC system.

3. The DRC system is invoked to save the state of the experiment, that is save
   the state of all the configuration files and history files that are
   "watched".

4. Highly recommended (but optional) another program is invoked to save the
   state of this experiment in a database that contains information about all
   experiments, allowing searches for common experiments, options, inputs. It
   makes it easier to identify which experiments might have erroneous inputs,
   or used versions of source code with bugs. The database is not necessary to
   run experiments, the experimental state is stored in git, but it ties
   experiments together. Potential collaborators could search each others
   database to find what models they are running. They could even fork a
   successful model and start using it themselves. A database can also be used
   to curate data. On entry a use-by date can be automatically generated. This
   does not guarantee deletion at that date, but allows for sequential deletion
   of data when storage becomes limited.

Finally, a unique identifier (DOI?) could be generated at point-of-publish for
the datasets used in the publication (this might require a database to satisfy
the requirements of a DOI, or something DOI-like). We could also generate
unique IDs for the output data as this time consuming step would only need to
be done once. The use-by date could be automatically incremented for important
datasets like this. This could satisfy the ARC requirement to keep data and
make it available. If so it could also satisfy Andy Pittman's request for a one
push publish solution.

This has the potential to be VERY cool.
