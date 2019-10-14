#!/bin/sh

rm "$1.wav"
rm output.txt

ffmpeg -i "$1.webm" -vn -acodec pcm_s16le -ac 1 -ar 16000  "$1.wav" > /dev/null 2>&1

deepspeech --model deepspeech-0.5.1-models/output_graph.pbmm --alphabet deepspeech-0.5.1-models/alphabet.txt --lm deepspeech-0.5.1-models/lm.binary --trie deepspeech-0.5.1-models/trie --audio "$1.wav" > output.txt

cat output.txt
