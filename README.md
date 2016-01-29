# Reddit Wallpapers
#### Beta

Automagically sets the top trending, good resolution images on reddit as your desktop wallpapers, in a loop !!


<img src="http://i.imgur.com/a0EpxUI.jpg"/>

### Installation:
```bash
$ pip install redditwallpapers
```


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

To select `top hot` `40` wallpapers from `r/EarthPorn` subreddit, and set duration for `10` mins

```bash
$ redditwallpapers -sr EarthPorn -sort get_hot -count 40 -t 10
```

##### Sort methods:
 * 'get_controversial'
 * 'get_controversial_from_all'
 * 'get_controversial_from_day'
 * 'get_controversial_from_hour'
 * 'get_controversial_from_month'
 * 'get_controversial_from_week'
 * 'get_controversial_from_year'
 * 'get_hot'
 * 'get_new'
 * 'get_random_submission'
 * 'get_rising'
 * 'get_top'
 * 'get_top_from_all'
 * 'get_top_from_day'
 * 'get_top_from_hour'
 * 'get_top_from_month'
 * 'get_top_from_week'
 * 'get_top_from_year'

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

then run: 
```bash
$ kill PID_NO
```
## Requirements
* OSX or Windows (Above Windows XP) or Linux (Unity and Gnome Shell (Gnome 3) )
* Python
* Pillow
* Praw

## The MIT License
> Copyright (c) 2015 Yask Srivastava http://iyask.me

> Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

> The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
