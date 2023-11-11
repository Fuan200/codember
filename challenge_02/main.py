def get_input():
    with open('input.txt', 'r') as f:
        return f.read()
    
def separate(input):
    list_uwu = [ char for char in input]
    return list_uwu

def main(input):
    value = 0
    output = ""

    for symbol in input:
        if symbol == "#":
            value += 1
        elif symbol == "@":
            value -= 1
        elif symbol == "*":
            value *= value
        elif symbol == "&":
            output += str(value)

    return output

if __name__ == '__main__':
    print(main(separate(get_input())))

""""#" Incrementa el valor numérico en 1.
"@" Decrementa el valor numérico en 1.
"*" Multiplica el valor numérico por sí mismo.
"&" Imprime el valor numérico actual."""