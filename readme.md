

Sharing utility code for neurocrime


---

Replace the block builder code with this

```
new_face = data.TrialHandler2(
    name='new_face',
    nReps=2.0, 
    method='sequential', 
    extraInfo=expInfo, 
    originPath=-1, 
    trialList=data.importConditions(
    'NeuroCrime/stim-faces.xlsx', 
    selection=f'{start_index} : {end_index}'
)
```