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

1. Install the [SL4A apk](http://android-scripting.googlecode.com/files/sl4a_r6.apk "SL4A") on your Android device. Note: You need to allow unknown sources first (Settings --> Security).

2. Add the python interpreter within Sl4A (also see [here](http://www.pythoncentral.io/python-for-android-the-scripting-layer-sl4a/ ""))

3. *Optional:* If you want a synced notebook via Dropbox, install the free app [Dropsync](play.google.com/store/apps/details?id=com.ttxapps.dropsync) and choose to sync the folder where your Notebook is located. In my case, I synced this folder to **/sdcard/sl4a/Dropbox/**, but feel free to choose whatever you like as a path (this is the *fullpath* variable in **Zim4Astarter.py**).

4. Copy all the [Zim4A files](github.com/kcg/Zim4A) to the parent folder of the Notebook (e.g. **/sdcard/sl4a/Dropbox**)

5. Copy the starter script **Zim4Astarter.py** to the script directory of Sl4A (**/sdcard/sl4a/scripts**).

6. Change the variable *fullpath* to the synced folder and change the variable *notebook* to the name of your Zim wiki. In the default case that is simply **Notes** (The notebook folder should be in the *fullpath* folder, i.e. **/sdcard/sl4a/Dropbox/Notes** in my case).

7. Start the script by opening SL4A and choosing **Zim4Astarter.py**.

8. *Optional:* Create a script shortcut on your homescreen for easy accessibility. (also see [here](groups.google.com/forum/#!topic/android-scripting/MVkn3aVXYrI))
