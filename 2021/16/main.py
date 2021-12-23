data = open("input", "r").read().strip()

from math import prod
from operator import lt, gt, eq

FN_MAP = [sum,prod,min,max,None,gt,lt,eq]


class Packet:
    def __init__(self, pack: str) -> None:
        self.__packet = pack
        self.value = 0
        self.subpackets = []
        self.ptr = 0
        
        self.version = self.__get_version()
        self.type = self.__get_type()
        
        if self.type == 4:
            self.value = self.__get_value()
        else:
            self.__get_subpackets()
        
    def __read(self, length) -> str:
        val = self.__packet[self.ptr:self.ptr+length]
        self.ptr += length
        return val
    
    def __get_int_val(self, length):
        return int(self.__read(length), 2)
    
    def __get_version(self):
        return self.__get_int_val(3)
    
    def __get_type(self):
        return self.__get_int_val(3)
    
    def __get_value(self):
        val = ""
        while self.ptr < len(self.__packet):
            has_more = self.__read(1) == "1"
            val += self.__read(4)
            if not has_more:
                break
        return int(val, 2)
    
    def __get_subpackets(self):
        length_type_id = self.__read(1)
        if length_type_id == "1":
            length = self.__get_int_val(11)
            for _ in range(length):
                pkg = Packet(self.__packet[self.ptr:])
                self.subpackets.append(pkg)
                self.ptr += pkg.ptr
        else:
            length = self.__get_int_val(15)
            while length > 0:
                pkg = Packet(self.__packet[self.ptr:self.ptr+length])
                self.subpackets.append(pkg)
                self.ptr += pkg.ptr
                length -= pkg.ptr
            
    def sum(self):
        return self.version + sum(packet.sum() for packet in self.subpackets)
    
    def compute(self):
        if self.type == 4:
            return self.value
        
        subs = [packet.compute() for packet in self.subpackets]
        # I hate myself for this
        try:
            return FN_MAP[self.type](subs)
        except:
            return FN_MAP[self.type](*subs)


# Don't forget zfill :c
pkg = Packet(bin(int(data, 16))[2:].zfill(len(data) * 4))

print("1:", pkg.sum())
print("2:", pkg.compute())
