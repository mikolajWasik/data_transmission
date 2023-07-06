# Data transmission
# Description
In this repository, I keep codes that are solutions to tasks from a university course on data transmission. In the first few tasks, several signals and their graphs versus time were generated using 'matplotlib.pyplot'. Then various, increasingly complex operations were carried out on those signals. Starting from the use of Fourier transform to change the domain of a function from time to frequency, through the use of different types of modulation and demodulation, to the use of Hamming encoders and decoders to correct interference simulated by adding white noise to the actual signal.

# Generating signals
Signal 'x' is a basic signal. Then 'y' was generated based on 'x', 'z' based on 'y' and finally, 'v' based on 'z'.

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/22abf921-e6d9-4465-b68f-f99c98df4d2c)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/da8a715a-9a46-4163-978d-9ba9c74fa1d9)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/8a9e1f32-f5a7-4376-818f-3131235360a6)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/39595bf8-62b2-44f3-b8d5-b64902274ee8)


Here b1, b2 and b3 are the same signal, but every next is more detailed.

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/102c63fc-b0a2-463d-b520-081e5f703d3b)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/dd6a423c-18fe-42b2-a71a-9ddf3099f797)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/d957b866-6e3e-462a-8b4a-b353dcc5515e)


# Fourier transform
Signal 'x' was made by adding signals 's1' and 's2' together. Signal 'M' is signal's 'x' Fourier transform.

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/7ceb8aee-1403-424c-9fb1-bd1b05c74b87)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/23635482-c51d-4617-b918-7251d4a68ed8)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/5dc60892-ccc7-4f21-b4c4-17917904e99f)
![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/2bfba109-c9c0-4a8e-995c-ddb33a4df479)


# Different types of modulation
Here's a short sequence of zeros and ones that represents a sample message. The message is then converted to a sine function whose parts are modulated appropriately depending on whether they represent zeros or ones. From the top, under the message there is an amplitude modulation, a phase modulation and a frequency modulation.

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/fd3fdb6c-493f-47b6-bfd0-eb763cc48cf9)


Once modulated, the message should be demodulated in a manner depending on the type of modulation it has undergone.
Amplitude demodulation:

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/07f55dc7-6bfc-4203-9923-4a06156f19d6)


Phase demodulation:

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/598b69b4-fe06-4bd8-94d8-d03fbf42179a)


Frequency demodulation:

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/d7d44275-37c8-4203-82c5-40ccd66424e6)


# Hamming's algorithm (7,4)
The algorithm is used for checking if a message was corrupted during its transmission. It takes the message written in a form of bits (0 and 1) and creates groups out of every four consecutive bits. After that, every group of bits is written in a form of template [pb, pb, mb, pb, mb, mb, mb], where 'mb' is message bit and 'pb' is parity bit. Parity bits are computed from message bits before transmission. After the transmission, algorithm decodes template and is able to indicate if any bits have been corrupted. If none of the bits were corrupted, then everything is fine. If only one bit was corrupted - algorithm will know which one it was and will fix it. If more bits were corrupted, then this part of message should be send again.

There is a word 'msg' written as bits based on every letter's ASCII value written in the binary system:

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/d6c19146-516b-444e-a903-6bc12ff1336f)

The last line means there are no errors.

Here I manually changed 6th bit after computing all parity bits:

![obraz](https://github.com/mikolajWasik/data_transmission/assets/96197911/6e746c3a-7b23-45ed-9b9d-f04e217019f8)

The algorithm fixed it on its own.
