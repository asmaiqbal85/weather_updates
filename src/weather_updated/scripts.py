import subprocess
def run():
    subprocess.run(["chainlit", "run", ".//src//weather_updated//chatbot.py", "-w"])