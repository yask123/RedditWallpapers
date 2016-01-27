# Reddit Wallpapers

Automatically sets the top trending, good resolution images on reddit as your desktop wallpapers, in a loop!

### Usage:
```bash
$ redditwallpapers
```

#### What it does ?
##### Default Behavior

* It would collect the top 20 rated wallpapers from `/r/EarthPorn` 
* Select only the high resolutions images one by one and sets them as desktop wallpaper (For a duration of 5 mins)
* Keep looping untill you kill the script



#### Customizations:

To select `top hot` `40` wallpapers from `[r/xyz]()` subreddit, and set duration for `10` mins

```bash
$ redditwallpaper -c xyz -sort get_hot -count 40 -time 10
```
#### Run it on startup

Type following command on terminal

```bash
$ @reboot redditwallpapers
```

#### Stop the script
Get the `PID_NO` by running: 

```bash
$ ps aux | grep redditwallpapers
```

then
```bash
$ kill PID_NO
```
