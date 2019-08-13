# Fusion

## Project Description

Fusion is one of the most awesome projects I have thought of until now. It is going to combine two of the most influential parts of my life both of which I am very passionate about: music and programming.

During the summer I was exposed more and more to electronic music and DJs. A big part of their job is transitioning between songs. The way transitioning works currently is by overlapping two songs, letting them play at the same time for a while, and then isolate the song you want to play next.

That is where __*Fusion*__ comes in. Fusion will be able to create a unique piece of music according to the two songs that need to be connected. The piece of music will be the mathematically perfect transition between those two songs. The end goal is for a DJ to play song A, followed by their fusion, followed by song B and the experience to be seamless.

## Implementation Steps

- Converting music to processable files (What is the best format?)
- Extract sound for bass, mids and highs.
- For each, figure out a note sequence.
- Use the interpolation feature of MusicVAE to interpolate between two sequences.
- Combine all those to create the fusion.

## Manual Transitions

Characteristics of manual transitions between songs that will be taken into account by fusion.
- Matching BPM of two songs
- The rule of 4s. Transition after a number of bars that is a multiple of 4.
- EQ
  - Tune B bass goes down (Mids and Highs as well but less)
  - Fade
  - Back up

## Resources

- [Magenta](https://github.com/tensorflow/magenta) is an Open Source project by Google and offers _MusicVAE_, a model that will probably be of use.
