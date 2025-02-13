from psychopy import visual, core, event
from pylsl import StreamInfo, StreamOutlet

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
    outlet.push_sample([marker])


info = StreamInfo("NeuroCrimeMarkerStream", "Markers", 1, 0, "int32")
outlet = StreamOutlet(info)

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


win.close()
core.quit()

