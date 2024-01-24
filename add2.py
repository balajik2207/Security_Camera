
import venv

def create_virtual_environment(directory):
    venv.create(directory, with_pip=True)

directory = 'my_virtual_environment'
create_virtual_environment(directory)