import binascii
import sys

def to_binary(s):
    return ''.join(bin(ord(c))[2:].zfill(8) for c in s)

def flip(s):
    return ''.join('0' if c == '1' else '1' for c in s if c in '01')

def main():
    if sys.stdin.isatty():
        data = input("Input:  ")
    else:
        data = sys.stdin.read()
    
    data = data.strip()
    is_binary = data and all(c in '01' for c in data)
    is_uu = False
    if not is_binary and data:
        try:
            binascii.a2b_uu(data.split()[0].encode())
            is_uu = True
        except:
            pass
    
    if is_binary:
        result = flip(data)
        encoded = binascii.b2a_uu(result.encode('utf-8')).decode().rstrip()
        print(encoded)
    elif is_uu:
        decoded = ''
        if '\n' in data:
            for line in data.splitlines():
                if line:
                    decoded += binascii.a2b_uu(line.encode()).decode()
        else:
            decoded = binascii.a2b_uu(data.encode()).decode()
        binary = flip(decoded)
        for try_len in range(len(binary), 0, -8):
            try:
                test = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, try_len, 8))
                print(test)
                break
            except:
                pass
    else:
        binary = to_binary(data)
        # cyno was here.
        flipped = flip(binary)
        lines = []
        for i in range(0, len(flipped), 45):
            chunk = flipped[i:i+45]
            if chunk:
                lines.append(binascii.b2a_uu(chunk.encode('utf-8')).decode().rstrip())
        print('\n'.join(lines))

if __name__ == "__main__":
    main()
