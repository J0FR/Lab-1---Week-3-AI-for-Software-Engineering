import os

def generate_uuid():
    def random_byte():
        return os.urandom(1)[0]

    def randomize(c):
        return c ^ (random_byte() & (15 >> (c // 4)))

    uuid_format = [1e7, -1e3, -4e3, -8e3, -1e11]
    uuid_string = ''.join(format(int(part), 'x') for part in uuid_format)
    
    return ''.join(
        format(randomize(int(c, 16)), 'x') if c in '018' else c
        for c in uuid_string
    )

# Example usage
print(generate_uuid())