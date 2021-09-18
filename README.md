# Vinx, your personal vocal assistant

Vinx, the Vocal assistant, is a fun personal project made to automatize repetitive tasks and explore the use of neural network in human languages. 

## :robot: What is Vinx ?

Vinx, the Vocal assistant, is a fun personal project made to automatize repetitive tasks and explore the use of neural network in human languages. 
Vinx can perform simple tasks such as giving the time, the latest news, the meteo or shutdown your computer. 


Python is the go-to language when dealing with deep learning and natural language processing. Vinx is a full python application with a GUI based on Tkinter. 
Since a vocal assistant needs to be able to speak and listen, the library Speech Recognition is used for Speech-To-Text while pyttsx3 is used for Text-To-Speech. 


Currently, Vinx is only able to respond to simple programmed sentences but the goal is to create an AI assistant. Making this AI is a fun challenge as Natural 
Language Processing is a very interesting yet difficult branch of computer science. I hope to implement a small chatbox AI and explore neural network algorithm.

## :star2: Vinx Skills

Vinx is taking its first steps so there is not a lot of functionalities yet. For the moment, you can : 
- Ask for date and time
- Ask for latest news
- Ask to read wikipedia
- Ask to shutdown computer
- Ask to open website

## :computer: How to install Vinx

```
# Configure environment
conda env create -f environment_vinx.yml
conda activate env

# In cmd, run the GUI
python VINX_GUI.py
```
