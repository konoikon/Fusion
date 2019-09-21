import numpy as np
import librosa

HOP = 512


def crop_wav_file(filename, outfile, from_second, to_second):
    y, sr = librosa.load(filename)
    yt, index = librosa.effects.trim(y)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_samples = HOP * beat_frames

    start = (np.abs(beat_samples - (from_second*sr))).argmin()
    end = (np.abs(beat_samples - (to_second*sr))).argmin()

    yt = yt[beat_samples[start]:beat_samples[end]]
    librosa.output.write_wav(outfile, yt, sr=sr)


def combine_waveforms(y1, sr1, y2, sr2):
    if sr1 == sr2:
        return np.append(y1, y2), sr1
    else:
        raise ValueError("Sample rates do not match")


def switch_harmonics_percussive(y1, y2):

    tempo1, beat_frames1 = librosa.beat.beat_track(y=y1)
    tempo2, beat_frames2 = librosa.beat.beat_track(y=y2)

    assert(tempo1 == tempo2)

    # find the first beat in each song
    beat1 = HOP * beat_frames1[0]
    beat2 = HOP * beat_frames2[0]
    # trim the song to the start of its first beat
    y1 = y1[beat1:]
    y2 = y2[beat2:]

    y1_harmonics = librosa.effects.harmonic(y1)
    y2_percussive = librosa.effects.percussive(y2)

    # if the waveform arrays are not the same size, we keep the shortest
    min_size = min(len(y1_harmonics), len(y2_percussive))

    y1_harmonics = y1_harmonics[len(y1_harmonics)-min_size:]
    y2_percussive = y2_percussive[len(y2_percussive)-min_size:]

    return np.add(y1_harmonics, y2_percussive)


def put_percussive_together(y1, y2):
    tempo1, beat_frames1 = librosa.beat.beat_track(y=y1)
    tempo2, beat_frames2 = librosa.beat.beat_track(y=y2)

    assert (tempo1 == tempo2)

    # find the first beat in each song
    beat1 = HOP * beat_frames1[0]
    beat2 = HOP * beat_frames2[0]
    # trim the song to the start of its first beat
    y1 = y1[beat1:]
    y2 = y2[beat2:]

    y1_percussive = librosa.effects.percussive(y1)
    y2_percussive = librosa.effects.percussive(y2)

    # if the waveform arrays are not the same size, we keep the shortest
    min_size = min(len(y1_percussive), len(y2_percussive))

    y1_harmonics = y1_percussive[len(y1_percussive) - min_size:]
    y2_percussive = y2_percussive[len(y2_percussive) - min_size:]

    return np.add(y1_harmonics, y2_percussive)
