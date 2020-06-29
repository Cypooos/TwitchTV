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

### How to add a program ?

Go to the `/program` folder. In it you'll see 2 exemple of how to configure programs. For every program you want to add, you should create a folder in this `/program` folder.

Every programs consist of a list of videos files that can be both in the folder or as a link to it. To add a video just drop it in the folder. To add a link one just drop a .txt file countaining a complete url (like "https://storage.googleapis.com/disruptplus_archives/Nature/Nature_air.mp4").

If you don't want to store the program inside the folder you can add a file referenc to it. Just like the url one but you just have to sepcify "file://PATH/TO/THE/FILE". It only accept absolute paths.

Every Program must also have a file called `program.conf` that told how to play the program. After first play can also see a `played.txt`, this is a file that i use to keep the played videos.

Here's the differents parameters of `program.conf`:
 - `PlayingOrder = Random or RandomMixed or Order`: If you choose random, it will pick a random file everytime the emission is played (can pick 2 time the same one !). If you choose the randomMix, it would mix the files randomely and create a "watchlist" (saved in `played.txt`). If you choose order it will played the files in alphabetical order. This way you can choose it by renomming them '000 - old name.mp4'.
 - `OnFileEnd = Next or Again or Goto:<TIME> or Hole`: If the file have been finish before the end that the planning system plan, should the program start the next file (Next), play the same over (Again), go to a specific time (Goto:XX, XX is the time in seconds), or make a Hole (and the planning system we'll play the `ShowOnEmpty` program)
 - `OnPlanEnd = Continue or Save`: If the planning system finish the program, should the program remember the place in second where he is (Save) so he can continue at the same place next time or close this one and pass to next one (Continue) 
 - `FileStart = 0`: The time to play your files from (cool for skipping intro from a premium service). It acccept floating numbers (like 3.5)
 - `ProgramName = <NAME>`: The name of your program. Use by the google calendar for exemple.


Both very useful configuration is :
 - `OnFileEnd = Next` and `OnPlanEnd = Save` or
 - `OnFileEnd = Hole` and `OnPlanEnd = Continue`

## Configurating the application

To configure the application, you'll need to open the "config.conf" file using any text editor you want (notepad, Sublim Text etc..).Every section is told int this file using brackets like `[this]`.

In the `[General]` section you'll want to selcet the different modules you want to use:
 - `PlanningSystem = GoogleCalendar`: The script to use to get the planning of videos to play.
 - `ProgramLoader = classic`: The script to use to get the differents programs.
 - `Players = VLC`: The software to use to stream the videos. I exept you to use VLC because the other one are not yet implemented. It is very laggy in the switching of videos and very unstable : the project is still in devellopement. We will add the `VLC-server`, `CV2` and `Pyglet` options whitch should be more stable. `FFMPEG` is also a possibilty, but this will not show the media, direclty stream the file to twitch / youtube.
 - `OnTrouble = None`: How to alert if the program crash / have some trouble. *(not yet implemented)*

Once thoses basic choice made, you'll need to configure eatch module individually. This should not take long.

### The Planning System

If you choose the Planning system to be `GoogleCalendar` (only current option), you'll need to configure the `[GoogleCalendar]` section:
 - `ReloadAccount = true/false`: If "true" (or "yes"), the google calendar will remove the previously made save session. This mean that the program will ask you everytime the Google Popup.  
 - `BufferSize = 10`: How many event the Calendar will keep in memory before reloading.
 - `CalendarName = TV`: The name of the Calendar to choose from.
 - `ShowOnEmpty = PROGRAM_NAME or None`: What to show if nothing was declare in the google calendar. Set `None` to show a black screen.
 - *`Client_secret_file`: Do not touch. The path to the JSON Client Google Auth API token.*
 - *`Client_flow_pickle_file`: Do not touch. The path to the saved Google calandar flow object.*

### The Program Loader

This program is responsible to select what to play and when. This will called the planning system to get the differents programs and will play them to the Streaming service.

For now the only option is "Classic" or "Default", but in the future I will add "Live". This will allow you to do both video files and lives.

The program's options are actually above if you choose `classic`, in the "How to add a program ?" section.

### The Streaming Service

Watever Streaming service you choose, you have those options to set :
 - `Hide = true or false`: If "true" (or "yes"), this will hide the VLC window. If "false" (or "no"), this will show it, and this way you can record it using OBS.

If you choose the Player to be `VLC`, you'll need to configure the `[VLC]` section:
 - There is no options to configure.

the only player for now is VLC; It is buggy, but in the future we will add both CV2, VLC-server and pyglet.

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

Once python is installed, you we'll need to install the dependency I used.

For this just open a CMD terminal (shift+click inside of the folder -> open terminal) and type the command `python -m pip install -r requirements.txt`. Once finish you can close the terminal.

To launch the program, you just need to start `start.bat`

### Running

To run the program you just need to execute the `start.bat` file.

If you failed the installation, and the start.bat program don't start the program, contact @Cypooos#9514 on discord ^w^

### Troubles ?

In case of troubles, you can message @Cypooos#9514 on discord or @Cypooos on Twitter.

Read also the "Errors" sections. This will light you way up to the light (maybe)

## Errors

MMmmm, i'm not perfect. But some of the errors don't come from me. So, for eatch message in the console, if the message don't start with [WARNING], [ERROR], [INFO], [DEBUG] or [TEST] it's not a message I intended you to see.

Here is a list of error message and how to respond to them :

### In the VLC configuration

Thoses error is the "expected" error if you choose the VLC configuration (you shouldn't) 

#### [h264 @ 0d2818c0] get_buffer() failed

__Often followed by:__
`[h264 @ 0d2818c0] thread_get_buffer() failed`
`[h264 @ 0d2818c0] decode_slice_header error`
`[h264 @ 0d2818c0] no frame!`

This is a normal error message if you choose the VLC configuration. It happen a lot during my testing, but it deosn't seam to interact in any way with the program.

It's happen -I think- because when I set the time of the video it's not exacly at the frame perfect.

#### [049f9058] main decoder error: buffer deadlock prevented

This error happen if the program is trying to read a fram that doesn't exist. That can happen if you have precise a starting position that is behind the file limit or if the file is finished.

#### [049f9058] avcodec decoder: Using D3D11VA (Intel(R) UHD Graphics 630, vendor 8086(Intel), device 3e9b, revision 0) for hardware decoding

Or similar : That is not a error, it just appear when the VLC renderer is called.

#### [06762190] direct3d11 vout display error: Could not create the depth stencil texture. (hr=0x80070057)

That happen if some video file are baddly formatted. I don't exacly have the spec of why this happen, but it depend using the file.

This is a deadly error as it just stop the program.

#### [0513e0d8] http stream error: local stream 1 error: Cancellation (0x8)

Always happen on start-up for some links. Doesn't really affect the program. It's often followed by multiple error of the same type.

#### [09be9c98] main decoder error: Timestamp conversion failed (delay 1000000, buffering 100000, bound 9000000)

[04af2b40] main decoder error: Could not convert timestamp 0 for FFmpeg

### Traceback (most recent call last):

This is totally my mistake. It's often followed by multiples lines indented.
Please send me your log file in /core/com/log.txt, the error, your conf and your programs conf you got so I can start debbuging.

if this is terminating by `KeyboardInterrupt:` then it just mean that you have done a Ctrl+C whitch is the shurtcut to close the program. Use Shift+Ctrl+C or right-click if you want to copy ^w^.

## Liscence

This code is made without any garanty. It may not work depending on your platform (Mac, MSDOS, etc..). I don't know. Don't ask me if you are not using a windows machine -_-

You are allow to make a commercial use of this program, on all his formed: compiled, sources, a part of it or the complete one.
