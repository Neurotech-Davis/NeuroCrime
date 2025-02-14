from psychopy import visual, core, event
from pylsl import StreamInfo, StreamOutlet
from pathlib import Path

root = Path(__file__).resolve().parent / "Display"

trials = [
    {
        "video": root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "Leemet-Bockler-High-Clip1.mp4",
        "images": [
            root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "2-Kasper-Surorg.png",
            root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "33-Martin-Meiers.png",
            root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "9-Severi-Kaukiainen.png",
            root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "$11-Leemet-Bockler.png",
            root / "11-Leemet-Bockler-(BC-Kalev)-selected" / "15-Anrijs-Miska.png",
        ],
    },
    {
        "video": root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "Cooper-Flag-Clip.mp4",
        "images": [
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "$2-Cooper-Flagg.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "52-Stanley-Borden.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "55-Spencer-Hubbard.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "7-Kon-Knueppel.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "8-Darren-Harris.png",
        ],
    },
    {
        "video": root / "23-Stephanie-Mavunga-(Poland)-selected" / "Stephanie-Mavunga-Clip1.mp4",
        "images": [
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "$23-Stephanie-Mavunga.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "12-Liliana-Banaszak.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "13-Weronika-Gajda.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "15-Klaudia-Gertchen.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "4-Julia-Niemojewska.png",
        ],
    },
    {
        "video": root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "Marcelinho-Huertas-Clip1.mp4",
        "images": [
            root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "$9-Marcelinho-Huertas.png",
            root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "15-Joan-Sastre.png",
            root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "3-Jaime-Fernandez.png",
            root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "35-Fran-Guerra.png",
            root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "42-Aaron-Doornekamp.png",
        ],
    },
    {
        "video": root / "9-Terezia-Palenikova-(Slovakia)-selected" / "Terezia-Palenikova-Clip1.mp4",
        "images": [
            root / "9-Terezia-Palenikova-(Slovakia)-selected" / "$9-Terezia-Palenikova.png",
            root / "9-Terezia-Palenikova-(Slovakia)-selected" / "15-Nikola-Kovacikova.png",
            root / "9-Terezia-Palenikova-(Slovakia)-selected" / "3-Ivana-Jakubcova.png",
            root / "9-Terezia-Palenikova-(Slovakia)-selected" / "4-Veronika-Remenarova.png",
            root / "9-Terezia-Palenikova-(Slovakia)-selected" / "88-Natalia-Martiskova.png",
        ],
    },
]


def createDisplay(trial):
    video = trials[trial]["video"]
    return visual.MovieStim(win, video, size=(640,480))

def createImages(trial):
    relevant_images=[]
    for i in range(len(trials[trial]["images"])):
        image =  visual.ImageStim(win, image=trials[trial]["images"][i], size =(640,480),pos=(0,0))
        relevant_images.append(image)
    return relevant_images

def sendMarker(marker):
    outlet.push_sample([marker])


info = StreamInfo("NeuroCrimeMarkerStream", "Markers", 1, 0, "int32")
outlet = StreamOutlet(info)

win = visual.Window(size=(800,600), color=(0,0,0), units='pix')

fixation_point = visual.ImageStim(win, image=root / "gray-dot.png", pos=(0,0))
fixation_point.draw()
win.flip()
core.wait(2.5)

for trial in range(len(trials)):
    display = createDisplay(trial)
    images = createImages(trial)

    display.play()

    while not display.getIsFinished():
        display.draw()
        win.flip()

    core.wait(1)
    for img in images:
        img.draw()
        win.flip()
        keys = event.waitKeys(maxWait=3, keyList=['f','j'])
        if keys:
            keyInt = {"f": 0, "j": 1}
            sendMarker(keyInt[keys[0]])
            continue

    core.wait(3)



win.close()
core.quit()

