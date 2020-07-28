from ByteCPU import ByteCPU
from ByteScreen import ByteScreen
import numpy as np

"""
-> Outer loop
Wait for the next timer tick (60 ticks are generated per second).
Poll the keys and store their states as a 2-byte value at address 0.
Fetch the 3-byte program counter from address 2, and execute exactly 65536 instructions.
Send the 64-KiB pixeldata block designated by the byte value at address 5 to the display device. Send the 256-byte sampledata block designated by the 2-byte value at address 6 to the audio device.
Go back to step 1.
"""


class BytePusher:
    def __init__(self):
        self._cpu = ByteCPU()
        self._screen = ByteScreen()

    def load_rom(self, rom_location):
        self._cpu.load_rom(rom_location)

    def cycle(self):
        self._screen.blit_text("Number of Drawn Frames 0", (0, 260))
        cycles = 0
        while True:
            # Fetch the 3-byte program counter from address 2, and execute exactly 65536 instructions.
            self._cpu.reset_pc()
            for pulse in range(0x10000):
                self._cpu.cpu_cycle()

            # Send the 64-KiB pixeldata block designated by the byte value at address 5 to the display device.
            self._screen.render_frame(self._cpu.mem_to_display(
                self._cpu.read_memory(0x5) << 16))
            cycles += 1
            cycles_str = "Number of Drawn Frames " + str(cycles)
            self._screen.blit_text(cycles_str, (0, 260))
