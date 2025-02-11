# A simple anime image CLI tool

## waifu-0.1.0
This tool fetches data from the danbooru API to display a random image in a compatible terminal. By default it will search images tagged with `cat_girl` under the `general` rating.

### Requirements
**waifu** uses *Term-Image* to draw the image on the terminal. Supported terminal emulators can be found from the Term-Image documentation here: https://term-image.readthedocs.io/en/stable/start/installation.html

### Commands
```
waifu
````
Runs the base command to fetch the image
```
waifu --tag [TAG]
```
Fetches an image based on your written tag. For example: `waifu --tag long_hair`
```
waifu --rating [RATING]
```
Overrides the rating (by default `general`). Valid rating options are:
```
general
sensitive
questionable
explicit
```
