from Helpers import *

class Segment:
    def __init__(self, length, file_id):
        # self.index = index
        self.length = length
        self.file_id = file_id

    def __repr__(self):
        return f"Segment(length={self.length}, file_id={self.file_id})"
    
    def expand(self):
        return [self.file_id] * self.length if self.file_id != -1 else ['.'] * self.length
    
    def calc_checksum(self, index):
        if self.file_id == -1:
            return 0, index + self.length
        check = 0
        for i in range(self.length):
            # print(f"adding {index + i} * {self.file_id} = {(index + i) * self.file_id}")
            check += (index + i) * self.file_id
        # check = sum((index + i) * self.file_id for i in range(self.length))
        index += self.length
        # print(self)
        # print(f"Checksum: {check}")
        # print(f"new index: {index}")
        return check, index


def build_segments():
    segments = []
    id = 0
    for i, num in enumerate(input):
        if int(num) == 0:
            continue
        if i % 2 == 0:
            segments.append(Segment(int(num), id))
            id += 1
        else:
            segments.append(Segment(int(num), -1))
    return segments, id - 1

def expand_map_v2(strings_only=False):
    segments, _ = build_segments()
    disk = []
    if strings_only:
        for seg in segments:
            disk.extend(map(str, seg.expand()))
    else:
        for seg in segments:
            disk.extend(seg.expand())
    return disk

# def expand_map():
#     blocks = []
#     is_free = False
#     blockId = 0
#     idx = 0
#     for num in input:
#         if not is_free:
#             blocks.extend([str(blockId)] * int(num))
#             idx += int(num)
#             blockId += 1
#         else:
#             blocks.extend(['.'] * int(num))
#             idx += int(num)
#         is_free = not is_free
#     return blocks

def print_blocks(blocks):
    print(str.join('', map(str, blocks)))

def print_segments(segments):
    disk = []
    for seg in segments:
            disk.extend(map(str, seg.expand()))
    print_blocks(disk)

def calc_checksum(blocks):
    checksum = sum(i * int(c) for i, c in enumerate(blocks) if c.isdigit())
    return checksum

def part1():
    blocks = expand_map_v2(True)
    dots = set(i for i, c in enumerate(blocks) if c == '.')

    min_idx = min(dots)

    for i in range(len(blocks) - 1, 0, -1):
        if min_idx > i:
            break
        if i not in dots:
            min_idx = min(dots)
            blocks[i], blocks[min_idx] = blocks[min_idx], blocks[i]
            dots.remove(min_idx)
            dots.add(i)
        min_idx = min(dots)
        
    blocks = blocks[:min_idx]
    return calc_checksum(blocks)

def part2():
    segments, highest_id = build_segments()
    pindx = len(segments) - 1

    # print("Initial State")
    # print_segments(segments)

    for i in range(highest_id, 0, -1):
        # print("Looking for segment", i)
        move = None
        move_idx = None

        # look for next lowest segment to move, starting from the index of the previous move
        pindx = min(pindx, len(segments) - 1)
        for seg_idx in range(pindx, 0, -1):
            if segments[seg_idx].file_id == i:
                move = segments[seg_idx]
                move_idx = seg_idx
                pindx = seg_idx
                # print(f"Found segment {move.file_id} at index {move_idx}")
                break

        #  Move segment to left most free space that is big enough
        for free_index, seg in enumerate(segments):
            if free_index >= move_idx:
                break
            if seg.file_id == -1 and seg.length >= move.length:
                # free_index = segments.index(seg)
                # print(f"Moving segment {move.file_id} to index {free_index}")

                # calculate space to use
                difference = seg.length - move.length

                # resize segment
                seg.length = move.length
                # print("resized seg")
                # print_segments(segments)

                # insert new free segment
                if difference > 0:
                    segments.insert(free_index + 1, Segment(difference, -1))
                    move_idx += 1
                # print("added free space")
                # print_segments(segments)

                # move segment
                seg.file_id = move.file_id
                # print("changed file id")
                # print_segments(segments)

                # free up segment
                segments[move_idx].file_id = -1
                # print("set moveid to free")
                # print_segments(segments)

                # attempt to combine free space to the right
                if move_idx + 1 < len(segments) and segments[move_idx + 1].file_id == -1:
                    segments[move_idx].length += segments[move_idx + 1].length
                    segments.pop(move_idx + 1)
                # attempt to combine free space to the left
                if move_idx > 0 and segments[move_idx - 1].file_id == -1:
                    segments[move_idx - 1].length += segments[move_idx].length
                    segments.pop(move_idx)
                break
    # print_segments(segments)
    checksum = 0
    i = 0
    for seg in segments:
        check, i = seg.calc_checksum(i)
        # print(f"adding {check} to {checksum} for {checksum + check}")
        checksum += check
    return checksum


    # disk = []
    # for seg in segments:
    #     disk.extend(map(str, seg.expand()))
    # print_blocks(disk)
    # return calc_checksum(disk)





example = False
input = read_input(9, example, True)

# execute(part1, "Day 9 - Part 1" + (" - Example" if example else ""))
# Exmpale Output: 1928
# Output: 6448989155953 - 38.84 sec

execute(part2, "Day 9 - Part 2" + (" - Example" if example else ""))
# Output: 6476642796832 - 14.32 sec
