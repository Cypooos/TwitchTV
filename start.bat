@echo off
echo ---------------------------------
echo [ME] hi, i'm here to help   ^w^  
echo ---------------------------------

if not exist venv (
    echo -------------------------------------
    echo [ME] He seam that you didn't install 
    echo  the virtual environnement    OwO    
    echo -------------------------------------
    pause 2
    echo -------------------------------------
    echo [ME] I'll try to do it          ^w^  
    echo -------------------------------------
    pause 2
    python -m pip install virtualenv
    python -m virtualenv venv --python=python3 
    call venv\Scripts\activate.bat
    python -m pip install -r requirements.txt
    echo -------------------------------------
    echo [ME] It's ok brother, i think I've   
    echo  just done it :D                     
    echo -------------------------------------
    pause 2
    echo -------------------------------------
    echo                               (°v°)  
    echo [ME] If I'm a bit stupid contact my  
    echo  creator on discord : @Cypooos#9514  
    echo -------------------------------------
    pause 2
)

echo -------------------------------------
echo [ME] Well, bye brother          UwU  
echo -------------------------------------
call venv\Scripts\activate.bat
python main.py
