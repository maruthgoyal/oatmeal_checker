# oatmeal_checker

This is a fan-made program that checks for a new Oatmeal comic every 1 hour.   
It will create a desktop notification to notify you if it finds a new comic.    
Click on the notification to see the new comic!    

NOTE: WORKS ONLY ON OS X    

To use:    

Clone this repository to your location of choice    
    • To clone to the desktop: <br />
        Open Terminal <br />
        cd Desktop <br />
        git clone https://github.com/maruthgoyal/oatmeal_checker.git <br />
<br />
Run the install.sh script <br />
    • Open Terminal <br />
    • cd /wherever/you/have/cloned/the/project <br />
    • source install.sh <br />
    • Enter your password when prompted to do so <br />
    • Wait for the installation to finish <br />
    • Close the terminal <br />
<br />
Run the run.sh script to run the program <br />
    • Open Terminal <br />
    • cd /wherever/you/have/cloned/the/project <br />
    • screen -S oatmeal_screen <br />
    • source run.sh <br />
    • Press ctrl + a <br />
    • Press d <br />
    • Close the terminal <br />
<br />
To terminate the program (if you want to) <br />
    • Open Terminal <br />
    • screen -X -S oatmeal_screen kill <br />
    • Close the terminal <br />
<br />
And that's it! Enjoy your Oatmeal! <br />
<br />
NOTE: If your computer ever shuts down or you terminate the program, just execute the run.sh script again as specified above. <br />
No need to run install.sh again though. 
