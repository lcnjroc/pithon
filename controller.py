import pyaudio
import wave


def playaudio(filename):
	chunk = 1024 # split our audio file into chunks
	wf = wave.open(filename, 'rb') # open the audio file as a readable file
	pa = pyaudio.pyAudio() # instantiate the pyAudio class

	stream = pa.open(
		format=pa.get_format_from_width(wf.getsampwidth()),
		channels=wf.getnchannels(),
		rate=wf.getframerate(),
		output=True
	)

	data_stream = wf.readframes(chunk)
	while data_stream:
		stream.write(data_stream)
		data_stream = wf.readframes(chunk)

	stream.close()
	pa.terminated()

playaudio('./audio/alert1.wav')
