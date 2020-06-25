# Twitch TV
A Python Programm that allow you to make a h24 VLC / Twitch TV

Made by `<Discursif/>` (@Cypooos) for `<Discursif/>` and `<Disrupt/>`

## Creating your TV

### What can you do ?

This python program allow you to stream non-stop content (both videos and direct) to a streaming service like a big TV corporation you are probably not !

**Ways to plan your videos:**
 - Create a google calendar of your videos to play.
 - Interrupt the TV with a live direct from another computer / the same using OBS *still in construction*
 - Playing special videos on top / making transition *still in construction and will  probably not be ready for a big time.*

**What streaming encoder is supported (you'll need to download them):**
 - VLC
 - FFMPEG

**What streaming services is supported:**
For now, the only true way to stream this is to record using OBS the VLC windows. This is temporary, as I'm working also on a way to stream from OBS to youtube / twitch. The FFMPEG way exist already, but it is very buggy (buffer overflow).

### how to add a program ?

Go to the `/program` folder. In it you'll see 2 exemple of how to configure programs. For every program you want to add, you should create a folder in this `/program` folder.

Every programs consist of a list of videos files that can be both in the folder and as a link to it (*the link one is not yet implemented*).

Every Program must also have a file called `program.conf` that told how to play the program. After first play can also see a `played.txt`, this is a file that i use to keep the played videos.

Here's the differents parameters of `program.conf`:
 - `PlayingOrder = Random or RandomMixed or Order`: If you choose random, it will pick a random file everytime the emission is played (can pick 2 time the same one !). If you choose the randomMix, it would mix the files randomely and create a "watchlist" (saved in `played.txt`). If you choose order it will played the files in alphabetical order. This way you can choose it by renomming them '000 - old name.mp4'.
 - `OnFileEnd = Next or Again or Goto:<TIME> or Hole`: If the file have been finish before the end that the planning system plan, should the program start the next file (Next), play the same over (Again), go to a specific time (Goto:XX, XX is the time in seconds), or make a Hole (and the planning system we'll play the `ShowOnEmpty` program)
 - `OnPlanEnd = Continue or Save`: If the planning system finish the program, should the program remember the place in second where he is (Save) so he can continue at the same place next time or close this one and pass to next one (Continue) 
 - `ProgramName = <NAME>`: The name of your program.


Both very useful configuration is :
 - `OnFileEnd = Next` and `OnPlanEnd = Save` or
 - `OnFileEnd = Hole` and `OnPlanEnd = Continue`

## Configurating the application

To configure the application, you'll need to open the "config.conf" file using any text editor you want (notepad, Sublim Text etc..).Every section is told int this file using brackets like `[this]`.

In the `[General]` section you'll want to selcet the different modules you want to use:
 - `PlanningSystem = Google_calendar`: The script to use to get the planning of videos to play.
 - `EmissionsPath = /programs`: The script to use to get the planning of videos to play.
 - `DirectSystem = None`: The script to use to stop the current playlist with a direct from another computer. *(not yet implemented)*
 - `playerss = VLC or FFMPEG`: The software to use to stream the videos.
 - `OnTrouble = None`: How to alert if the program crash / have some trouble. *(not yet implemented)*

Once thoses basic choice made, you'll need to configure eatch module individually. This should not take long.

### The Planning System

If you choose the Planning system to be `GoogleCalendar` (only current option), you'll need to configure the `[GoogleCalendar]` section:
 - `ReloadAccount = true/false`: If "true" (or "yes"), the google calendar will remove the previously made save session. This mean that the program will ask you everytime the Google Popup.  
 - `BufferSize = 10`: How many event the Calendar will keep in memory before reloading.
 - `ShowOnEmpty = PROGRAM_NAME or None`: What to show if nothing was declare in the google calendar. Set `None` to show a black screen.
 - *`Client_secret_file`: Do not touch. The path to the JSON Client Google Auth API token.*
 - *`Client_flow_pickle_file`: Do not touch. The path to the saved Google calandar flow object.*

### The Direct System

Still in devellopement.

### The Streaming Service

If you choose the Player to be `VLC`, you'll need to configure the `[VLC]` section:
 - `HideVLC = true or false`: If "true" (or "yes"), this will hide the VLC window. If "false" (or "no"), this will show it, and this way you can record it using OBS.

If you choose the Player to be `FFMPEG`, you'll need to configure the `[FFMPEG]` section:
 - There is nothing yet. 

### Others

This is some configuration you can change. This is in the `[Other]` section.
Here's the options:
 - `LogFile = core/output/log.txt`: The log file used to log data in case of error.
 - `ReloadPrograms = day or program`: Reload all the programs every days or every programs.

## Running the programm

To run the program the first time you'll need to do the installation process.

### Installation

This is a python application. to run it, you would need python.

Download python [here](https://www.python.org/ftp/python/3.8.3/python-3.8.3.exe).
During the installation process, please check that "add python to path" option is checked. That way the installation program will work !

Once python is installed, you we'll need to type the following command into a terminal. To start a terminal, search for "CMD" in the app searcher.

 - `python -m pip install virtualenv`: this command is gonna download a module called "virtualenv" that we are using to setup a envrionnement to protect the program.
 - `python -m virtualenv venv --python=python3`: This command will create the virtual environnement.
 - `\venv\Script\activate.bat`: Start the environnement
 - `python -m pip -r requirement.txt`: Download the dependency needed

### Running

To run the program you just need to execute the `start.bat` file.

If you failed the installation, and the start.bat program don't start the program, contact @Cypooos#9514 on discord ^w^

To know what this bat file is doing :
 - `call \venv\Script\activate.bat`: Start the environnement
 - `python src/main.py`: Start the program
He also have security about whatever you installed virtualenv. :+1:

### Troubles ?

In case of troubles, you can message @Cypooos#9514 on discord or @Cypooos on Twitter.

## Liscence

This code is made without any garanty. It may not work depending on your platform (Mac, MSDOS, etc..). I don't know. Don't ask me if you are not using a windows machine -_-