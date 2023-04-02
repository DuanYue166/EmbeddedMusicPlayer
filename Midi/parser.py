import time
import mido
from mido import MidiFile


def extractTrack(mid:MidiFile,trackID:int):
    noteList=[]
    tempo=500000
    lstMsg=0
    for i,track in enumerate(mid.tracks):
        for msg in track:
            if(msg.type=='set_tempo'):
                tempo=msg.tempo
                print('tempo set '+str(tempo))
            elif(i==trackID and (not msg.is_meta)):
                sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,350959)
                if((lstMsg is not 0) and lstMsg.type=='note_on' and lstMsg.velocity!=0):
                    noteList.append([lstMsg.note,sleepTime])
                    print(lstMsg)
                lstMsg=msg    
    return noteList


def playTrack(mid:MidiFile,trackID:int):
    outport = mido.open_output()
    tempo=500000
    for i,track in enumerate(mid.tracks):
        for msg in track:
            if(msg.type=='set_tempo'):
                tempo=msg.tempo
                print('tempo set '+str(tempo))
            elif(i==trackID and (not msg.is_meta)):
                sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,350959)
                if(sleepTime<3):
                    time.sleep(sleepTime)
                outport.send(msg)
                print(msg)


def saveSheetToFile(noteList:list,outFileName:str):
    file=open(outFileName,'w')
    file.write(str(len(noteList))+'\n')
    for note,time in noteList:
        file.write("{} {}\n".format(note,time))
    file.close()


def readMidi(mid):
    filename='./temp/{}.log'.format(time.strftime(r'%Y%m%d_%H%M%S',time.localtime()))
    file=open(filename,'w')
    for i, track in enumerate(mid.tracks):
        file.write('Track {}: {}\n'.format(i, track.name))
        for msg in track:
            file.write(str(msg)+'\n')


if(__name__=='__main__'):
    mid = mido.MidiFile('./res/Everglow.mid')
    # readMidi(mid)
    # playTrack(mid,6)
    noteList=extractTrack(mid,6)
    saveSheetToFile(noteList,r'./res/4.txt')
