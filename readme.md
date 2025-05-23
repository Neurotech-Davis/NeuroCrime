
# NeuroCrime GitHub Repo

This repo consists of:
1) The PsychoPy stimulus procedure, and its associated stimulus.
2) A script to create the stimulus excel sheets.
3) A script to combine EEG data recorded via OpenBCI with the Pyschopy procedure data files.
4) A script to download YT videos to use as stimulus.

Project Description:
The Neurocrime project was designed to analyze the accuracy of a participants recollection of an event. Our goal was to be able to distinguish if someone could accurately identify the correct suspect among innocent people. Due to the ethical constraints and difficutly of finding reliable crime videos, we had to switch our media to basketball clips. This made us switch our experimental design to make the participants identify the individual who scored in the basketball clip.
---
### Note 1:
The downloader script needs to download .webm files in order to maintain as high quality as possible. Converting to mp4 with high resolution can take a while, so we suggest clipping the .webm file before converting.

Clipping webm:
1) Clip the webm file with audio
```
ffmpeg -i input.webm -ss 00:01:30 -to 00:02:00 -c copy clip.webm
```

2) Clip the webm file without audio. -an flag means no audio.
```
ffmpeg -i input.webm -ss 00:01:30 -to 00:02:00 -c:v copy -an clip.webm
```

Converting to mp4:

3) Fast, but a little loss. 
```
ffmpeg -i input.webm -c:v copy -an output.mp4
```

4) Slower, but less loss 
```
ffmpeg -i input.webm -c:v libx264 -crf 18 -preset slow -an output.mp4
```
