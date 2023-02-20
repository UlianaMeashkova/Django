Create a GitHub account

Create on GitHub a repository called "lessons"

Open bash terminal

Install git package to the system

 sudo apt install -y git
Setup your user account

  git config --global user.name "Alexander Chaika"
  git config --global user.email "manti.by@gmail.com"
Create projects directory and go to it

  mkdir projects
  cd projects/
Clone this repository and go to it

  git clone git@github.com:manti-by/lessons.git
  cd lessons/
Create an empty file and check git status, new file should be colored in red

  touch README.md
  git status
Add a new file to repository and check status, new file should be green

  git add README.md
  git status
Save (commit) a nw file to local repository and then push it to GitHub

  git commit -m "Add readme file"
  git push
FAQ
If you created keys for GitHub and still on push git asks for login/password, change your repository url from HTTPS to SSH:

  git remote set-url origin git@github.com:manti-by/lessons.git
git+ssh