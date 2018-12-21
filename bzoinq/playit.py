import subprocess
from pkg_resources import resource_filename


def playit(file):
    """
    Function used to play a sound file
    """
    filepath = resource_filename(__name__, 'sound/' + file)
    subprocess.Popen(["paplay", filepath])
