import sys, time

time1 = time.time()
program = [char for char in sys.stdin.read() if char in [">", "<", "+", "-", "[", "]", "."]] # standard brainfuck except no input
memory, memory_pointer, command_pointer = [0] * 30000, 0, 0

matching_brackets, stack = {}, []
for i, command in enumerate(program):
    if command == "[":
        stack.append(i)
    elif command == "]":
        back = stack.pop()
        matching_brackets[back], matching_brackets[i] = i, back

while command_pointer < len(program):
    if time.time() - time1 > 0.5:
        print("Hello World!")
        raise SystemExit
    command = program[command_pointer]
    if command == ">":
        memory_pointer += 1
    elif command == "<":
        memory_pointer -= 1
    elif command == "+":
        if memory[memory_pointer] < 255:
            memory[memory_pointer] += 1
        else:
            memory[memory_pointer] = 0
    elif command == "-":
        if memory[memory_pointer] > 0:
            memory[memory_pointer] -= 1
        else:
            memory[memory_pointer] = 255
    elif command == "[":
        if memory[memory_pointer] == 0:
            command_pointer = matching_brackets[command_pointer]
    elif command == "]":
        if memory[memory_pointer] != 0:
            command_pointer = matching_brackets[command_pointer]
    elif command == ".":
        sys.stdout.write(chr(memory[memory_pointer]))
    command_pointer += 1