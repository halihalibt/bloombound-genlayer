"""Render the original, quiet piano miniature 'A Garden Between Words'."""
from pathlib import Path
import tempfile
import numpy as np
from scipy.io.wavfile import write
from scipy.signal import butter, sosfilt
SR=24000
BEAT=60/70
BAR=4*BEAT
BARS=32
LENGTH=BARS*BAR
track=np.zeros((int((LENGTH+6)*SR),2),dtype=np.float64)
def note(midi,start,duration=3.4,gain=.12,pan=0):
    n=int(duration*SR);t=np.arange(n)/SR;f=440*2**((midi-69)/12)
    # Soft struck partials: high harmonics decay faster than the fundamental.
    wave=np.zeros(n)
    for k,amp in enumerate([1,.32,.105,.041,.014],1):
        wave+=amp*np.sin(2*np.pi*f*k*t+0.001*k*t)*np.exp(-t*(1.2+.68*k))
    wave*=np.minimum(t/.018,1)*(1-np.exp(-(duration-t)/.08))*gain
    ix=int(start*SR);end=min(len(track),ix+n);wave=wave[:end-ix]
    track[ix:end,0]+=wave*np.sqrt((1-pan)/2)
    track[ix:end,1]+=wave*np.sqrt((1+pan)/2)
chords=[[48,55,60,64,71],[45,52,57,60,67],[41,48,53,57,64],[43,50,55,60,62],[48,55,59,64,67],[45,52,57,60,64],[41,48,53,57,60],[43,50,55,59,62]]
melodies=[[76,79,81,79],[76,72,71,72],[69,72,76,74],[71,74,72,67],[76,79,83,79],[81,79,76,72],[77,76,72,69],[71,74,72,71]]
for bar in range(BARS):
    chord=chords[bar%8];start=bar*BAR
    note(chord[0],start,4.8,.105,-.3)
    for j in range(8):
        pitch=chord[[1,2,3,4,3,2,4,3][j]]+12
        note(pitch,start+j*BEAT/2,2.5,.047+(j%3)*.004,(-1 if j%2 else 1)*.24)
    melody=melodies[bar%8]
    for j,pitch in enumerate(melody):
        if bar%8==7 and j==3: pitch=72
        if bar>=16 and j==1:pitch-=12
        note(pitch,start+(j+.08)*BEAT,3.5,.084 if j%2==0 else .067,.12)
# Gentle room reflections rather than a constant electronic drone.
dry=track.copy()
for delay,level in [(.11,.15),(.23,.10),(.37,.075),(.61,.045),(.91,.025)]:
    offset=int(delay*SR);track[offset:]+=dry[:-offset,::-1]*level
track=sosfilt(butter(2,3800,fs=SR,output='sos'),track,axis=0)
length=int(LENGTH*SR)
# Wrap the tail into the opening to keep the repeating room decay continuous.
track[:len(track)-length]+=track[length:]
track=track[:length]
peak=np.max(np.abs(track));track*=.72/peak
Path('public/audio').mkdir(parents=True,exist_ok=True)
write(str(Path(tempfile.gettempdir())/'bloombound-garden-piano.wav'),SR,(track*32767).astype(np.int16))
print({'seconds':round(LENGTH,2),'sample_peak':float(np.max(np.abs(track))),'rms':float(np.sqrt(np.mean(track**2))),'clipped_samples':int(np.sum(np.abs(track)>=1))})
