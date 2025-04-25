## Git: Software/Code Versioning Tool. 

- Git is a version control tool that runs locally!
- Github is a interface/UI that allows users to interact with their code base. 
- Each codebase is called a repository. Git repo = A project with version control. 

### Use Cases: 
- Tool for tracking different versions of your code base. 
- Applies each individual file and helps you revert back incase of any issues. 
- Allows users to work collaboratively using "branches" 
    - A Branch - is a seperated version of the code base and allows edits/commits that are seperate from the main branch. 

### Basic Usage (Terminal Commands): 
- `git init`: This will start the version control process - this tells git that this is a project I want to track. (Only need to run this once!) 
- `git add`: This will add files into the save point. (Staging is the set of files that you add to your save point.)
- `git commit -m "<MESSSAGE NAME>`": Is a save point, that way you can revert your code back to incase of any bugs/issues. Message Name is usually a brief description of the changes you've made. 
- `git checkout -b <BRANCH NAME>`: Create a branch with a particular name. 
- `git push -u origin <BRANCH NAME>`: Pushes changes to Github. 