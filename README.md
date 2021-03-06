# Hello World

Project to practice making installers, running Pygame and configuring Flask servers on AWS. There are three 'hello world' programs,

`hello-world` : Write some output to console. To check that the installer includes multiple Python script files, it includes a file in a folder called `modules.`

`hello-pygame` : Runs a Pygame window.

`hello-flask` : Runs a flask server.

#### Installation
```
pip install pygame
pip install pyinstaller
pip install flask
```
#### To build the executable
For example, to build the Pygame .EXE,
```
> pyinstaller --hidden-import pkg_resources.py2_warn --onefile -w hello-pygame.py
```
`--hidden-import` : Avoids an error message, as described [here](https://stackoverflow.com/questions/37815371/pyinstaller-failed-to-execute-script-pyi-rth-pkgres-and-missing-packages)

`--onefile` : Create a one-file bundled executable.

`-w` : Do not provide a console window. We don't need a console, as Pygame opens its own window.
#### To make an installation file
1. Put all files to be installed into a Zip file.
2. Use [NSIS](https://nsis.sourceforge.io/Download) to make the installation file.

#### EC2 Service

To run NGINX,
```
sudo systemctl restart nginxdfs
```

#### Useful Resources
[YouTube - How to Convert any Python File to .EXE
](https://youtu.be/UZX5kH72Yx4)
