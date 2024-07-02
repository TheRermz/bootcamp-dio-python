
import re



def validate_numero_telefone(phone_number):

    pattern = r'^\(\d{2}\) 9\d{4}-\d{4}$'

    if re.match(pattern, phone_number):

        return f'Número de telefone válido.'

    else:
        return f'Número de telefone inválido.'

def main():
    phone_number = input()
    result = validate_numero_telefone(phone_number)
    print(result)

main()
