def get_input():
    with open('input.txt', 'r') as f:
        return f.readlines()

def validation_password(policy, password):
    positions, char = policy.split(' ')
    min_pos, max_pos = map(int, positions.split('-'))
    count = password.count(char)
    return min_pos <= count <= max_pos

def count_forty_two(input, invalid_index=42):
    invalid_passwords = []
    for line in input:
        policy, password = line.split(':')
        if not validation_password(policy.strip(), password.strip()):
            invalid_passwords.append(password.strip())
    return invalid_passwords[invalid_index - 1] if len(invalid_passwords) >= invalid_index else None

def main():
    input_lines = get_input()
    result = count_forty_two(input_lines)
    return result

if __name__ == '__main__':
    print(main())