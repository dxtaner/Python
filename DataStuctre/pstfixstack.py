def postfix_hesaplama(postfix_ifade):
    stack = []

    for eleman in postfix_ifade.split():
        if eleman.isdigit():
            stack.append(int(eleman))
        else:
            sayi2 = stack.pop()
            sayi1 = stack.pop()
            if eleman == '+':
                stack.append(sayi1 + sayi2)
            elif eleman == '-':
                stack.append(sayi1 - sayi2)
            elif eleman == '*':
                stack.append(sayi1 * sayi2)
            elif eleman == '/':
                stack.append(sayi1 / sayi2)

    return stack.pop()


postfix_ifade = "3 4 +"
sonuc = postfix_hesaplama(postfix_ifade)
print(f"'{postfix_ifade}' ifadesinin sonucu: {sonuc}")
