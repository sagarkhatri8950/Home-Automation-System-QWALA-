# Home-Automation-System-QWALA-
Home Automation system named Qwala that can be used to control the home devices like lights, fans with the voice command directly from being in the room or from any other place with the help of mobile device. It also includes facial recognition to detect the person and can perform operations like door open or close based on the command stored. This project is developed on Raspberry pi 3 using python. It can be implemented in a room or entire home " without " the use of any extra devices like wireless bulb,fans not required.


To run the project it requires the database to exist.\
Schema for the database tables is as: \
\
commands(id{int),command(varchar),cmdvalue(int),solution(varchar),searchcount(int),accuracy(int))\
searchdb(id(int),query(varchar);\
lightcontroldb(id(int),query(varchar);

After creating these tables, you are required to run sync file to start the system;
