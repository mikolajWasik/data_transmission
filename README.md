# Data transmission
# Description
In this repository, codes are stored that are solutions to tasks from a course on data transmission studies. In the first few tasks, various signals and their graphs versus time were generated using 'matplotlib.pyplot'. Then various, increasingly complex operations were carried out on these signals. Starting from the use of Fourier transforms to change the domain of a function from time to frequency, through the use of various types of modulation and demodulation, to the use of Hamming encoders and decoders to correct interference simulated by adding white noise to the actual signal.

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
