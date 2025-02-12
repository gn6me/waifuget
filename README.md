# A simple anime image CLI tool
<p align="center">
<img src="https://github.com/user-attachments/assets/7f5dae5c-1451-43a3-972b-db54f598a665" />
</p>

## waifu-v1.0
This tool fetches data from the danbooru API to display a random image in a compatible terminal. By default it will search images tagged with `cat_girl` under the `general` rating.

### Requirements
**Term-Image** is used to draw the image on the terminal. Supported terminal emulators can be found from the Term-Image documentation here: https://term-image.readthedocs.io/en/stable/start/installation.html

### Installation

I recommend installing the package via **pipx**. If you do not have pipx installed on your system, instructions for Windows, MacOS, and Linux can be found here: https://github.com/pypa/pipx

#### 1. Clone the repo
You can either download the repo as a zip file or clone it locally via ``git``.
```
git clone https://github.com/gn6me/waifuget.git
```
*If you downloaded the zip file, don't forget to extract it!*

#### 2. Install via pipx
Navigate to the downloaded repo via your terminal and type the command:
```
pipx install .
```
Make sure you are in the directory with the `setup.py` file.
pipx should install the package on your system and you can now use the command ``waifu`` globally.

### Commands
```
waifu
````
Runs the base command to fetch the image
```
waifu --tag [TAG]
waifu -t # shorthand
```
Fetches an image based on your written tag. For example: `waifu --tag long_hair`
```
waifu --rating [RATING]
waifu -r # shorthand
```
Overrides the rating (by default `general`). Valid rating options are:
```
general
sensitive
questionable
explicit
```
