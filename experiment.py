from psychopy import visual, core, event
import serial

trials = [
    {"video":, "images": []},  #contains filepaths like "stimuli/video/video.mp4"
    {"video":, "images": []},
    {"video":, "images": []},
    {"video":, "images": []},
    {"video":, "images": []},
    {"video":, "images": []}
]

def createDisplay(trials, trial):
    video = trials[trial]["video"]
    return visual.MovieStim3(win, video, size=(640,480))

def createImages(trials, trial):
    relevant_images=[]
    for i in range(trials[trial]["images"]):
        relevant_images.append(trials[trial]["images"][i])
    return relevant_images

def sendMarker(marker):
    ser.write(f"{marker}\n".encode())


port = "myport"
ser = serial.Serial(port, 115200, timeout=1)

win = visual.Window(size=(800,600), color=(0,0,0), units='pix')

for trial in range(trials):
    display = createDisplay(trials, trial)
    images = createImages(trials, trial)

    while display.status != visual.FINISHED:
        display.draw()
        win.flip()

    core.wait(5) #edit waiting period

    for img in images:
        img.draw()
        win.flip()
        keys = event.waitKeys(maxWait=3, keyList=['f','j'])
        if keys:
            sendMarker(f"User_Response_{keys[0]}")
            continue

    core.wait(10)




ser.close()
win.close()
core.quit()
