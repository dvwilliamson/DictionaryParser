Dictionary Creator
===============
Written by Joshua Monson for the ARCLITE Lab, Brigham Young University.

Requirements
------------
sbt (http://www.scala-sbt.org/)

Compiling
---------
This is an sbt project so all you'll need to do is run sbt from the project directory, then run the command:

    compile
    
Running
-------
Run the sbt command:

    run
    
This will show you the usage:

    ARCLITE Dictionary Tool
    Usage: create [dictionarySet]
    Usage: test   [dictionarySet] [dictionary] [entries ...]
    
    The following are the available dictionary sets:
       giovanni  -- The dictionaries provided by Giovanni

So to create the Giovanni dictionaries you would execute the following sbt command:

    run create giovanni

Dictionary Files
----------------
It is expected that the dictionary text files will be placed under the following directory:

    src/main/resources

They are not included for space reasons. It looks for the following Giovanni dictionary text files in that folder:
* GEN-EF-pos.txt
* GEN-EG-pos.txt
* GEN-EI-pos.txt

The generated dictionaries will be saved to files in this folder.