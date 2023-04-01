import time
import mido

from mido import MidiFile

def extract(mid:MidiFile,trackID:int,outFileName:str):
    file=open(outFileName,'w')
    tempo=500000
    for msg in mid.tracks[trackID]:
        if(not msg.is_meta):
            sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,tempo)

            print(msg)
        elif(msg.type=='set_tempo'):
            tempo=msg.tempo
            print('tempo set'+str(tempo))

def playTrack(mid:MidiFile,trackID:int):
    outport = mido.open_output()
    tempo=500000
    for msg in mid.tracks[trackID]:
        if(not msg.is_meta):
            sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,tempo)
            if(sleepTime<10):
                time.sleep(mido.tick2second(msg.time,mid.ticks_per_beat,tempo))
            outport.send(msg)
            print(msg)
        elif(msg.type=='set_tempo'):
            tempo=msg.tempo
            print('tempo set'+str(tempo))

def saveSheetToFile(noteList:list,outFileName:str):
    
    pass

def outputToFile():
    file=open('output2.txt','w')
    tempo=500000
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if(not msg.is_meta):
                if(msg.channel==3):
                    print(msg)
                    file.write(str(msg)+'\n')
                    sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,tempo)
                    print(sleepTime)
                    if(sleepTime<10):
                        time.sleep(mido.tick2second(msg.time,mid.ticks_per_beat,tempo))
            elif(msg.type=='set_tempo'):
                tempo=msg.tempo
                print('tempo set'+str(tempo))


def getList():
    noteList=[]
    tempo=500000
    lstMsg=0
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if(not msg.is_meta):
                if(msg.channel==3):
                    sleepTime=mido.tick2second(msg.time,mid.ticks_per_beat,tempo)
                    print(lstMsg)
                    if((lstMsg is not 0) and  lstMsg.type=='note_on' and lstMsg.velocity != 0):
                        noteList.append([lstMsg.note,sleepTime])
                    lstMsg=msg.copy()
            elif(msg.type=='set_tempo'):
                tempo=msg.tempo
                print('tempo set'+str(tempo))
    print(noteList)
    return noteList


mid = mido.MidiFile('D:/Dev/STM32/Final/Midi/HotelCalifornia.mid')



outputToFile()
exit()


noteList=getList()

file=open('loads.txt','w')
file.write('a['+str(len(noteList))+']={')
for note in noteList:
    file.write(str(note[0])+',')
file.write('};\n')
file.write('b['+str(len(noteList))+']={')
for note in noteList:
    file.write(str(note[1])+',')
file.write('};\n')

