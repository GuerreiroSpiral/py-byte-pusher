import numpy as np

"""
Specifications
Framerate: 	60 frames per second
CPU: 	ByteByteJump with 3-byte addresses
CPU speed: 	65536 instructions per frame (3932160 instructions per second, ~3.93 MHz).
Byte ordering: 	Big-endian
Memory: 	16 MiB RAM 
Program Counter starts at address 2.
Inner loop and program counter initialization described on https://esolangs.org/wiki/BytePusher
"""


class ByteCPU:
    def __init__(self):
        self._memory = np.array([0] * 0x1000000, dtype='uint8')
        self._program_counter = np.uint32(self.read_memory(
            0x2) << 0x10 | self.read_memory(0x3) << 0x08 | self.read_memory(0x4))

    def read_memory(self, address):
        return self._memory[address]

    def write_on_memory(self, address, data):
        self._memory[address] = data

    def reset_pc(self):
        self._program_counter = np.uint32(self.read_memory(
            0x2) << 0x10 | self.read_memory(0x3) << 0x08 | self.read_memory(0x4))

    def load_rom(self, rom):
        buffer = open(rom, "rb").read()

        if len(buffer) <= len(self._memory):
            for i in range(len(buffer)):
                self.write_on_memory(i, buffer[i])
        else:
            print("That's some weird ROM you have there. It's to big to fit into memory.")

    def mem_to_display(self, address):
        display_memory = np.array([0] * (256*256), dtype="uint8")

        for i in range((256*256)):
            display_memory[i] = self._memory[address + i]

        return display_memory

    def cpu_cycle(self):
        A = self.read_memory(self._program_counter) << 0x10 | self.read_memory(
            self._program_counter + 0x1) << 0x8 | self.read_memory(self._program_counter + 0x2)
        B = self.read_memory(self._program_counter + 0x3) << 0x10 | self.read_memory(
            self._program_counter + 0x4) << 0x8 | self.read_memory(self._program_counter + 0x5)

        self.write_on_memory(B, self.read_memory(A))
        self._program_counter = self.read_memory(self._program_counter + 0x8) | self.read_memory(
            self._program_counter + 0x7) << 0x8 | self.read_memory(self._program_counter + 0x6) << 0x10
