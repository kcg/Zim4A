# Zim4A
Zim Desktop Wiki for Android via SL4A

**Description**
Zim4A is an Android application which is written in Python and uses
[SL4A](http://code.google.com/p/android-scripting/ "SL4A") to make a
[Zim Desktop Wiki](http://zim-wiki.org/ "Zim Desktop Wiki") available
for mobile devices running Android OS.
The approach I am using relies on Dropsync to synchronize my Zim wiki
(which lives inside my Dropbox) onto my Android system.

**Features**
So far, the following functionalities are implemented:
* Make the index of a Zim Desktop Wiki browsable
* Show formatted pages
* Edit (existing) pages

The applications was only tested on a Sony Compact Z3 running Android 4.4.4
and might be buggy.

**Screenshots**
![Screenshots](http://karl-goedel.de/modx/assets/img/zim4a.png)

**Installation:**
After installing Dropsync and choosing a folder for your Notebook,
copy all Zim4A files into the same folder in which the Notebook folder
(default name: "Notes") is located.
Then, copy the Zim4Astarter.py script to the script folder of Sl4A and
change the "fullpath" variable to the location of your Notebook.
That's it.
