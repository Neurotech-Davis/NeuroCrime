import pandas as pd
from pathlib import Path

import random

# This code SHOULD work on all machines, but theres some weirdness on mine because of WSL
# root = Path(__file__).resolve().parent / "Display"
root = Path(r"C:\Users\diego\OneDrive\Documents\Coding\Neurotech\Neurocrime\Display")

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
        "video": root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "Cooper-Flag-Clip2.mp4",
        "images": [
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "$2-Cooper-Flagg.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "52-Stanley-Borden.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "55-Spencer-Hubbard.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "7-Kon-Knueppel.png",
            root / "2-Cooper-Flagg-(Duke-Blue-Devils)-selected" / "8-Darren-Harris.png",
        ],
    },
    {
        "video": root / "23-Stephanie-Mavunga-(Poland)-selected" / "Stephanie-Mavunga-Clip4.mp4",
        "images": [
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "$23-Stephanie-Mavunga.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "12-Liliana-Banaszak.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "13-Weronika-Gajda.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "15-Klaudia-Gertchen.png",
            root / "23-Stephanie-Mavunga-(Poland)-selected" / "4-Julia-Niemojewska.png",
        ],
    },
    {
        "video": root / "9-Marcelinho-Huertas-(La-Laguna-Tenerife)-selected" / "Marcelinho-Huertas-Clip2.mp4",
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

vid_list = [] 
stim_list = []
culprit_list = []
times_face_shown = 10
shuffled_index = [0,1,2,3,4]
shuffled_index_next = [0,1,2,3,4]

# for clip_struct in trials:
#   vid_list.append(clip_struct["video"])
#   for i in range(times_face_shown):
#     while (True):
#       random.shuffle(shuffled_index_next)
#       if (shuffled_index_next[0] != shuffled_index[4]):
#         break
#     for k in range(5):
#       stim_list.append(clip_struct["images"][shuffled_index_next[k]])
#       culprit_list.append(clip_struct["images"][shuffled_index_next[k]].name[0] == '$') # Are they the culprit? Culprits labeled with $
      

for clip_struct in trials:
  vid_list.append(clip_struct["video"])
  for i in range(5):
      stim_list.append(clip_struct["images"][shuffled_index_next[i]])
      culprit_list.append(clip_struct["images"][shuffled_index_next[i]].name[0] == '$') # Are they the culprit? Culprits labeled with $

    
start_list = []
end_list = []
for i in range(5):
    start_list.append(i*(5)) # starts indexing at 0, and header row doesn't count
    end_list.append((i+1)*(5))


    

# Create a DataFrame
stim_faces = {
    "stim_faces": stim_list,
    "culprit": culprit_list 
}
df = pd.DataFrame(stim_faces)
df.to_excel("stim-faces.xlsx", index=False)
print("Data written to 'stim-faces.xlsx'")

stim_vids = {
    "stim_vids": vid_list,
    "start_index": start_list,
    "end_index": end_list,
}
df = pd.DataFrame(stim_vids)
df.to_excel("stim-vids.xlsx", index=False)
print("Data written to 'stim-vids.xlsx'")



