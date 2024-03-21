from setuptools import find_packages,setup
from typing import List

HYPHAN_DOT = '-e .'
def get_requirment(file_parth:str)->List[str]:
    """
          this function will return the list of requirments
    """
    requierments = []
    with open(file_parth) as file_obj:
        requierments= file_obj.readlines()
        requierments = [red.replace('\n'," ") for red in requierments]
        
        if HYPHAN_DOT in requierments:
            requierments.remove(HYPHAN_DOT)
    
    return requierments
             
    

setup(name="mlproject1",
      version="0.0.1",
      author="kunal patil",
      author_email="kunal15cr@gmail.com",
      password=find_packages(),
      install_requires=get_requirment("requierments.txt"))