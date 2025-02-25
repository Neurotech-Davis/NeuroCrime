#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on February 22, 2025, at 22:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'MyProcedure'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1440, 960]
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\diego\\OneDrive\\Documents\\Coding\\Neurotech\\MyProcedure.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='pix',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'pix'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "baseline_recording" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Align your hands with: \nYour left index finger on f\nYour right index finger on j\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "aligning_text" ---
    aligning_data_text = visual.TextStim(win=win, name='aligning_data_text',
        text="On the onset of the red figure, quickly clench your jaw.\n\nAct quickly to align it!\n\nThis is to align data, we're intentionally creating this noise.\n\n",
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=1000.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "aligning_image" ---
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(3000, 3000)[0], height=(3000, 3000)[1],
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='red', fillColor='red',
        opacity=None, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "explaining_task_text_2" ---
    explaining_task_text = visual.TextStim(win=win, name='explaining_task_text',
        text='For this task you will be asked to facially identify the culprit vs. the innocents. The culprit will be the player who scores.',
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=1000.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    explaining_text_2 = visual.TextStim(win=win, name='explaining_text_2',
        text='You will identify them by pressing \nf  (left hand key)   or    j  (right hand key) \non your keyboard.',
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=1000.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    button_clarification_text = visual.TextStim(win=win, name='button_clarification_text',
        text="Get ready to pay attention to a basketball clip! Remember the scorer's face.",
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=1000.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "showing_movie" ---
    clips = visual.MovieStim(
        win, name='clips',
        filename=None, movieLib='ffpyplayer',
        loop=False, volume=1.0, noAudio=False,
        pos=(0, 0), size=(2880, 1920), units=win.units,
        ori=0.0, anchor='center',opacity=None, contrast=1.0,
        depth=0
    )
    
    # --- Initialize components for Routine "button_refresher" ---
    text = visual.TextStim(win=win, name='text',
        text='Did this person score?\nf  (left)  = this person / culprit \nj (right) = not this person / innocent',
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=1000.0, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "showing_faces" ---
    mugshots = visual.ImageStim(
        win=win,
        name='mugshots', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    grey_dot = visual.ImageStim(
        win=win,
        name='grey_dot', 
        image='NeuroCrime/Display/smaller_black_dot.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), draggable=False, size=None,
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "break_2" ---
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='Take a little break if needed!',
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Press f, j, or space to continue to the next clip',
        font='Arial',
        pos=(0, 0), draggable=False, height=75.0, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    
    # --- Initialize components for Routine "baseline_recording" ---
    text_4 = visual.TextStim(win=win, name='text_4',
        text='Align your hands with: \nYour left index finger on f\nYour right index finger on j\n',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "baseline_recording" ---
    # create an object to store info about Routine baseline_recording
    baseline_recording = data.Routine(
        name='baseline_recording',
        components=[text_4, key_resp_3],
    )
    baseline_recording.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for baseline_recording
    baseline_recording.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    baseline_recording.tStart = globalClock.getTime(format='float')
    baseline_recording.status = STARTED
    thisExp.addData('baseline_recording.started', baseline_recording.tStart)
    baseline_recording.maxDuration = None
    # keep track of which components have finished
    baseline_recordingComponents = baseline_recording.components
    for thisComponent in baseline_recording.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "baseline_recording" ---
    baseline_recording.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            baseline_recording.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baseline_recording.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "baseline_recording" ---
    for thisComponent in baseline_recording.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for baseline_recording
    baseline_recording.tStop = globalClock.getTime(format='float')
    baseline_recording.tStopRefresh = tThisFlipGlobal
    thisExp.addData('baseline_recording.stopped', baseline_recording.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "baseline_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "aligning_text" ---
    # create an object to store info about Routine aligning_text
    aligning_text = data.Routine(
        name='aligning_text',
        components=[aligning_data_text],
    )
    aligning_text.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for aligning_text
    aligning_text.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    aligning_text.tStart = globalClock.getTime(format='float')
    aligning_text.status = STARTED
    thisExp.addData('aligning_text.started', aligning_text.tStart)
    aligning_text.maxDuration = None
    # keep track of which components have finished
    aligning_textComponents = aligning_text.components
    for thisComponent in aligning_text.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "aligning_text" ---
    aligning_text.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *aligning_data_text* updates
        
        # if aligning_data_text is starting this frame...
        if aligning_data_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aligning_data_text.frameNStart = frameN  # exact frame index
            aligning_data_text.tStart = t  # local t and not account for scr refresh
            aligning_data_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aligning_data_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'aligning_data_text.started')
            # update status
            aligning_data_text.status = STARTED
            aligning_data_text.setAutoDraw(True)
        
        # if aligning_data_text is active this frame...
        if aligning_data_text.status == STARTED:
            # update params
            pass
        
        # if aligning_data_text is stopping this frame...
        if aligning_data_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > aligning_data_text.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                aligning_data_text.tStop = t  # not accounting for scr refresh
                aligning_data_text.tStopRefresh = tThisFlipGlobal  # on global time
                aligning_data_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'aligning_data_text.stopped')
                # update status
                aligning_data_text.status = FINISHED
                aligning_data_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            aligning_text.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in aligning_text.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "aligning_text" ---
    for thisComponent in aligning_text.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for aligning_text
    aligning_text.tStop = globalClock.getTime(format='float')
    aligning_text.tStopRefresh = tThisFlipGlobal
    thisExp.addData('aligning_text.stopped', aligning_text.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if aligning_text.maxDurationReached:
        routineTimer.addTime(-aligning_text.maxDuration)
    elif aligning_text.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler2(
        name='trials',
        nReps=5.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=[None], 
        seed=None, 
    )
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            globals()[paramName] = thisTrial[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisTrial in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        # --- Prepare to start Routine "aligning_image" ---
        # create an object to store info about Routine aligning_image
        aligning_image = data.Routine(
            name='aligning_image',
            components=[polygon],
        )
        aligning_image.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for aligning_image
        aligning_image.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        aligning_image.tStart = globalClock.getTime(format='float')
        aligning_image.status = STARTED
        thisExp.addData('aligning_image.started', aligning_image.tStart)
        aligning_image.maxDuration = 3.5
        # keep track of which components have finished
        aligning_imageComponents = aligning_image.components
        for thisComponent in aligning_image.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "aligning_image" ---
        # if trial has changed, end Routine now
        if isinstance(trials, data.TrialHandler2) and thisTrial.thisN != trials.thisTrial.thisN:
            continueRoutine = False
        aligning_image.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 3.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # is it time to end the Routine? (based on local clock)
            if tThisFlip > aligning_image.maxDuration-frameTolerance:
                aligning_image.maxDurationReached = True
                continueRoutine = False
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and tThisFlip >= 1.25-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                pass
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + 1.25-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                aligning_image.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in aligning_image.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "aligning_image" ---
        for thisComponent in aligning_image.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for aligning_image
        aligning_image.tStop = globalClock.getTime(format='float')
        aligning_image.tStopRefresh = tThisFlipGlobal
        thisExp.addData('aligning_image.stopped', aligning_image.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if aligning_image.maxDurationReached:
            routineTimer.addTime(-aligning_image.maxDuration)
        elif aligning_image.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-3.500000)
        thisExp.nextEntry()
        
    # completed 5.0 repeats of 'trials'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "explaining_task_text_2" ---
    # create an object to store info about Routine explaining_task_text_2
    explaining_task_text_2 = data.Routine(
        name='explaining_task_text_2',
        components=[explaining_task_text, explaining_text_2, button_clarification_text],
    )
    explaining_task_text_2.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for explaining_task_text_2
    explaining_task_text_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    explaining_task_text_2.tStart = globalClock.getTime(format='float')
    explaining_task_text_2.status = STARTED
    thisExp.addData('explaining_task_text_2.started', explaining_task_text_2.tStart)
    explaining_task_text_2.maxDuration = None
    # keep track of which components have finished
    explaining_task_text_2Components = explaining_task_text_2.components
    for thisComponent in explaining_task_text_2.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "explaining_task_text_2" ---
    explaining_task_text_2.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 17.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *explaining_task_text* updates
        
        # if explaining_task_text is starting this frame...
        if explaining_task_text.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            explaining_task_text.frameNStart = frameN  # exact frame index
            explaining_task_text.tStart = t  # local t and not account for scr refresh
            explaining_task_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explaining_task_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explaining_task_text.started')
            # update status
            explaining_task_text.status = STARTED
            explaining_task_text.setAutoDraw(True)
        
        # if explaining_task_text is active this frame...
        if explaining_task_text.status == STARTED:
            # update params
            pass
        
        # if explaining_task_text is stopping this frame...
        if explaining_task_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > explaining_task_text.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                explaining_task_text.tStop = t  # not accounting for scr refresh
                explaining_task_text.tStopRefresh = tThisFlipGlobal  # on global time
                explaining_task_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explaining_task_text.stopped')
                # update status
                explaining_task_text.status = FINISHED
                explaining_task_text.setAutoDraw(False)
        
        # *explaining_text_2* updates
        
        # if explaining_text_2 is starting this frame...
        if explaining_text_2.status == NOT_STARTED and tThisFlip >= 6-frameTolerance:
            # keep track of start time/frame for later
            explaining_text_2.frameNStart = frameN  # exact frame index
            explaining_text_2.tStart = t  # local t and not account for scr refresh
            explaining_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(explaining_text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'explaining_text_2.started')
            # update status
            explaining_text_2.status = STARTED
            explaining_text_2.setAutoDraw(True)
        
        # if explaining_text_2 is active this frame...
        if explaining_text_2.status == STARTED:
            # update params
            pass
        
        # if explaining_text_2 is stopping this frame...
        if explaining_text_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > explaining_text_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                explaining_text_2.tStop = t  # not accounting for scr refresh
                explaining_text_2.tStopRefresh = tThisFlipGlobal  # on global time
                explaining_text_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'explaining_text_2.stopped')
                # update status
                explaining_text_2.status = FINISHED
                explaining_text_2.setAutoDraw(False)
        
        # *button_clarification_text* updates
        
        # if button_clarification_text is starting this frame...
        if button_clarification_text.status == NOT_STARTED and tThisFlip >= 11-frameTolerance:
            # keep track of start time/frame for later
            button_clarification_text.frameNStart = frameN  # exact frame index
            button_clarification_text.tStart = t  # local t and not account for scr refresh
            button_clarification_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_clarification_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'button_clarification_text.started')
            # update status
            button_clarification_text.status = STARTED
            button_clarification_text.setAutoDraw(True)
        
        # if button_clarification_text is active this frame...
        if button_clarification_text.status == STARTED:
            # update params
            pass
        
        # if button_clarification_text is stopping this frame...
        if button_clarification_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > button_clarification_text.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                button_clarification_text.tStop = t  # not accounting for scr refresh
                button_clarification_text.tStopRefresh = tThisFlipGlobal  # on global time
                button_clarification_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_clarification_text.stopped')
                # update status
                button_clarification_text.status = FINISHED
                button_clarification_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            explaining_task_text_2.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in explaining_task_text_2.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "explaining_task_text_2" ---
    for thisComponent in explaining_task_text_2.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for explaining_task_text_2
    explaining_task_text_2.tStop = globalClock.getTime(format='float')
    explaining_task_text_2.tStopRefresh = tThisFlipGlobal
    thisExp.addData('explaining_task_text_2.stopped', explaining_task_text_2.tStop)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if explaining_task_text_2.maxDurationReached:
        routineTimer.addTime(-explaining_task_text_2.maxDuration)
    elif explaining_task_text_2.forceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-17.000000)
    thisExp.nextEntry()
    
    # set up handler to look after randomisation of conditions etc
    new_clip = data.TrialHandler2(
        name='new_clip',
        nReps=1.0, 
        method='sequential', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('NeuroCrime/stim-vids.xlsx'), 
        seed=None, 
    )
    thisExp.addLoop(new_clip)  # add the loop to the experiment
    thisNew_clip = new_clip.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisNew_clip.rgb)
    if thisNew_clip != None:
        for paramName in thisNew_clip:
            globals()[paramName] = thisNew_clip[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisNew_clip in new_clip:
        currentLoop = new_clip
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisNew_clip.rgb)
        if thisNew_clip != None:
            for paramName in thisNew_clip:
                globals()[paramName] = thisNew_clip[paramName]
        
        # --- Prepare to start Routine "showing_movie" ---
        # create an object to store info about Routine showing_movie
        showing_movie = data.Routine(
            name='showing_movie',
            components=[clips],
        )
        showing_movie.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        clips.setMovie(stim_vids)
        # store start times for showing_movie
        showing_movie.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        showing_movie.tStart = globalClock.getTime(format='float')
        showing_movie.status = STARTED
        thisExp.addData('showing_movie.started', showing_movie.tStart)
        showing_movie.maxDuration = None
        # keep track of which components have finished
        showing_movieComponents = showing_movie.components
        for thisComponent in showing_movie.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "showing_movie" ---
        # if trial has changed, end Routine now
        if isinstance(new_clip, data.TrialHandler2) and thisNew_clip.thisN != new_clip.thisTrial.thisN:
            continueRoutine = False
        showing_movie.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *clips* updates
            
            # if clips is starting this frame...
            if clips.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
                # keep track of start time/frame for later
                clips.frameNStart = frameN  # exact frame index
                clips.tStart = t  # local t and not account for scr refresh
                clips.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(clips, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'clips.started')
                # update status
                clips.status = STARTED
                clips.setAutoDraw(True)
                clips.play()
            
            # if clips is stopping this frame...
            if clips.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > clips.tStartRefresh + 3-frameTolerance or clips.isFinished:
                    # keep track of stop time/frame for later
                    clips.tStop = t  # not accounting for scr refresh
                    clips.tStopRefresh = tThisFlipGlobal  # on global time
                    clips.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'clips.stopped')
                    # update status
                    clips.status = FINISHED
                    clips.setAutoDraw(False)
                    clips.stop()
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[clips]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                showing_movie.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in showing_movie.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "showing_movie" ---
        for thisComponent in showing_movie.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for showing_movie
        showing_movie.tStop = globalClock.getTime(format='float')
        showing_movie.tStopRefresh = tThisFlipGlobal
        thisExp.addData('showing_movie.stopped', showing_movie.tStop)
        clips.stop()  # ensure movie has stopped at end of Routine
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if showing_movie.maxDurationReached:
            routineTimer.addTime(-showing_movie.maxDuration)
        elif showing_movie.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler2(
            name='trials_2',
            nReps=2.0, 
            method='random', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=[None], 
            seed=None, 
        )
        thisExp.addLoop(trials_2)  # add the loop to the experiment
        thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                globals()[paramName] = thisTrial_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisTrial_2 in trials_2:
            currentLoop = trials_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
            if thisTrial_2 != None:
                for paramName in thisTrial_2:
                    globals()[paramName] = thisTrial_2[paramName]
            
            # --- Prepare to start Routine "button_refresher" ---
            # create an object to store info about Routine button_refresher
            button_refresher = data.Routine(
                name='button_refresher',
                components=[text],
            )
            button_refresher.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            # store start times for button_refresher
            button_refresher.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            button_refresher.tStart = globalClock.getTime(format='float')
            button_refresher.status = STARTED
            thisExp.addData('button_refresher.started', button_refresher.tStart)
            button_refresher.maxDuration = 5.5
            # keep track of which components have finished
            button_refresherComponents = button_refresher.components
            for thisComponent in button_refresher.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "button_refresher" ---
            # if trial has changed, end Routine now
            if isinstance(trials_2, data.TrialHandler2) and thisTrial_2.thisN != trials_2.thisTrial.thisN:
                continueRoutine = False
            button_refresher.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 5.5:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > button_refresher.maxDuration-frameTolerance:
                    button_refresher.maxDurationReached = True
                    continueRoutine = False
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    pass
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 4-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    button_refresher.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in button_refresher.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "button_refresher" ---
            for thisComponent in button_refresher.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for button_refresher
            button_refresher.tStop = globalClock.getTime(format='float')
            button_refresher.tStopRefresh = tThisFlipGlobal
            thisExp.addData('button_refresher.stopped', button_refresher.tStop)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if button_refresher.maxDurationReached:
                routineTimer.addTime(-button_refresher.maxDuration)
            elif button_refresher.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.500000)
            
            # set up handler to look after randomisation of conditions etc
            new_face = data.TrialHandler2(
                name='new_face',
                nReps=1.0, 
                method='random', 
                extraInfo=expInfo, 
                originPath=-1, 
                trialList=data.importConditions(
                'NeuroCrime/stim-faces.xlsx', 
                selection=str(start_index) + ":" + str(end_index)
            )
            , 
                seed=None, 
            )
            thisExp.addLoop(new_face)  # add the loop to the experiment
            thisNew_face = new_face.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisNew_face.rgb)
            if thisNew_face != None:
                for paramName in thisNew_face:
                    globals()[paramName] = thisNew_face[paramName]
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            
            for thisNew_face in new_face:
                currentLoop = new_face
                thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
                # abbreviate parameter names if possible (e.g. rgb = thisNew_face.rgb)
                if thisNew_face != None:
                    for paramName in thisNew_face:
                        globals()[paramName] = thisNew_face[paramName]
                
                # --- Prepare to start Routine "showing_faces" ---
                # create an object to store info about Routine showing_faces
                showing_faces = data.Routine(
                    name='showing_faces',
                    components=[mugshots, grey_dot, key_resp],
                )
                showing_faces.status = NOT_STARTED
                continueRoutine = True
                # update component parameters for each repeat
                mugshots.setImage(stim_faces)
                # create starting attributes for key_resp
                key_resp.keys = []
                key_resp.rt = []
                _key_resp_allKeys = []
                # store start times for showing_faces
                showing_faces.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
                showing_faces.tStart = globalClock.getTime(format='float')
                showing_faces.status = STARTED
                thisExp.addData('showing_faces.started', showing_faces.tStart)
                showing_faces.maxDuration = None
                # keep track of which components have finished
                showing_facesComponents = showing_faces.components
                for thisComponent in showing_faces.components:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "showing_faces" ---
                # if trial has changed, end Routine now
                if isinstance(new_face, data.TrialHandler2) and thisNew_face.thisN != new_face.thisTrial.thisN:
                    continueRoutine = False
                showing_faces.forceEnded = routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 5.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *mugshots* updates
                    
                    # if mugshots is starting this frame...
                    if mugshots.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                        # keep track of start time/frame for later
                        mugshots.frameNStart = frameN  # exact frame index
                        mugshots.tStart = t  # local t and not account for scr refresh
                        mugshots.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(mugshots, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'mugshots.started')
                        # update status
                        mugshots.status = STARTED
                        mugshots.setAutoDraw(True)
                    
                    # if mugshots is active this frame...
                    if mugshots.status == STARTED:
                        # update params
                        pass
                    
                    # if mugshots is stopping this frame...
                    if mugshots.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > mugshots.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            mugshots.tStop = t  # not accounting for scr refresh
                            mugshots.tStopRefresh = tThisFlipGlobal  # on global time
                            mugshots.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'mugshots.stopped')
                            # update status
                            mugshots.status = FINISHED
                            mugshots.setAutoDraw(False)
                    
                    # *grey_dot* updates
                    
                    # if grey_dot is starting this frame...
                    if grey_dot.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                        # keep track of start time/frame for later
                        grey_dot.frameNStart = frameN  # exact frame index
                        grey_dot.tStart = t  # local t and not account for scr refresh
                        grey_dot.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(grey_dot, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'grey_dot.started')
                        # update status
                        grey_dot.status = STARTED
                        grey_dot.setAutoDraw(True)
                    
                    # if grey_dot is active this frame...
                    if grey_dot.status == STARTED:
                        # update params
                        pass
                    
                    # if grey_dot is stopping this frame...
                    if grey_dot.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > grey_dot.tStartRefresh + 2-frameTolerance:
                            # keep track of stop time/frame for later
                            grey_dot.tStop = t  # not accounting for scr refresh
                            grey_dot.tStopRefresh = tThisFlipGlobal  # on global time
                            grey_dot.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'grey_dot.stopped')
                            # update status
                            grey_dot.status = FINISHED
                            grey_dot.setAutoDraw(False)
                    
                    # *key_resp* updates
                    waitOnFlip = False
                    
                    # if key_resp is starting this frame...
                    if key_resp.status == NOT_STARTED and tThisFlip >= 4-frameTolerance:
                        # keep track of start time/frame for later
                        key_resp.frameNStart = frameN  # exact frame index
                        key_resp.tStart = t  # local t and not account for scr refresh
                        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp.started')
                        # update status
                        key_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                    # if key_resp is stopping this frame...
                    if key_resp.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > key_resp.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            key_resp.tStop = t  # not accounting for scr refresh
                            key_resp.tStopRefresh = tThisFlipGlobal  # on global time
                            key_resp.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'key_resp.stopped')
                            # update status
                            key_resp.status = FINISHED
                            key_resp.status = FINISHED
                    if key_resp.status == STARTED and not waitOnFlip:
                        theseKeys = key_resp.getKeys(keyList=['f','j'], ignoreKeys=["escape"], waitRelease=False)
                        _key_resp_allKeys.extend(theseKeys)
                        if len(_key_resp_allKeys):
                            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                            key_resp.rt = _key_resp_allKeys[-1].rt
                            key_resp.duration = _key_resp_allKeys[-1].duration
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, win=win)
                        return
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                        )
                        # skip the frame we paused on
                        continue
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        showing_faces.forceEnded = routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in showing_faces.components:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "showing_faces" ---
                for thisComponent in showing_faces.components:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                # store stop times for showing_faces
                showing_faces.tStop = globalClock.getTime(format='float')
                showing_faces.tStopRefresh = tThisFlipGlobal
                thisExp.addData('showing_faces.stopped', showing_faces.tStop)
                # check responses
                if key_resp.keys in ['', [], None]:  # No response was made
                    key_resp.keys = None
                new_face.addData('key_resp.keys',key_resp.keys)
                if key_resp.keys != None:  # we had a response
                    new_face.addData('key_resp.rt', key_resp.rt)
                    new_face.addData('key_resp.duration', key_resp.duration)
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if showing_faces.maxDurationReached:
                    routineTimer.addTime(-showing_faces.maxDuration)
                elif showing_faces.forceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-5.000000)
                thisExp.nextEntry()
                
            # completed 1.0 repeats of 'new_face'
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            thisExp.nextEntry()
            
        # completed 2.0 repeats of 'trials_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "break_2" ---
        # create an object to store info about Routine break_2
        break_2 = data.Routine(
            name='break_2',
            components=[key_resp_2, text_2, text_3],
        )
        break_2.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # create starting attributes for key_resp_2
        key_resp_2.keys = []
        key_resp_2.rt = []
        _key_resp_2_allKeys = []
        # store start times for break_2
        break_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        break_2.tStart = globalClock.getTime(format='float')
        break_2.status = STARTED
        thisExp.addData('break_2.started', break_2.tStart)
        break_2.maxDuration = None
        # keep track of which components have finished
        break_2Components = break_2.components
        for thisComponent in break_2.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "break_2" ---
        # if trial has changed, end Routine now
        if isinstance(new_clip, data.TrialHandler2) and thisNew_clip.thisN != new_clip.thisTrial.thisN:
            continueRoutine = False
        break_2.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_2* updates
            waitOnFlip = False
            
            # if key_resp_2 is starting this frame...
            if key_resp_2.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
                # keep track of start time/frame for later
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.tStart = t  # local t and not account for scr refresh
                key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_2.started')
                # update status
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_2.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_2.getKeys(keyList=['f','j','enter','space'], ignoreKeys=["escape"], waitRelease=False)
                _key_resp_2_allKeys.extend(theseKeys)
                if len(_key_resp_2_allKeys):
                    key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                    key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                    key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_2* updates
            
            # if text_2 is starting this frame...
            if text_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_2.started')
                # update status
                text_2.status = STARTED
                text_2.setAutoDraw(True)
            
            # if text_2 is active this frame...
            if text_2.status == STARTED:
                # update params
                pass
            
            # if text_2 is stopping this frame...
            if text_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_2.tStop = t  # not accounting for scr refresh
                    text_2.tStopRefresh = tThisFlipGlobal  # on global time
                    text_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.stopped')
                    # update status
                    text_2.status = FINISHED
                    text_2.setAutoDraw(False)
            
            # *text_3* updates
            
            # if text_3 is starting this frame...
            if text_3.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                # update status
                text_3.status = STARTED
                text_3.setAutoDraw(True)
            
            # if text_3 is active this frame...
            if text_3.status == STARTED:
                # update params
                pass
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break_2.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in break_2.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "break_2" ---
        for thisComponent in break_2.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for break_2
        break_2.tStop = globalClock.getTime(format='float')
        break_2.tStopRefresh = tThisFlipGlobal
        thisExp.addData('break_2.stopped', break_2.tStop)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
            key_resp_2.keys = None
        new_clip.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            new_clip.addData('key_resp_2.rt', key_resp_2.rt)
            new_clip.addData('key_resp_2.duration', key_resp_2.duration)
        # the Routine "break_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'new_clip'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    # --- Prepare to start Routine "baseline_recording" ---
    # create an object to store info about Routine baseline_recording
    baseline_recording = data.Routine(
        name='baseline_recording',
        components=[text_4, key_resp_3],
    )
    baseline_recording.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # create starting attributes for key_resp_3
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # store start times for baseline_recording
    baseline_recording.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    baseline_recording.tStart = globalClock.getTime(format='float')
    baseline_recording.status = STARTED
    thisExp.addData('baseline_recording.started', baseline_recording.tStart)
    baseline_recording.maxDuration = None
    # keep track of which components have finished
    baseline_recordingComponents = baseline_recording.components
    for thisComponent in baseline_recording.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "baseline_recording" ---
    baseline_recording.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            baseline_recording.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baseline_recording.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "baseline_recording" ---
    for thisComponent in baseline_recording.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for baseline_recording
    baseline_recording.tStop = globalClock.getTime(format='float')
    baseline_recording.tStopRefresh = tThisFlipGlobal
    thisExp.addData('baseline_recording.stopped', baseline_recording.tStop)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "baseline_recording" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
