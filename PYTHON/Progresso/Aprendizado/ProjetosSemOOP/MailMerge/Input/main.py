# cd 'PYTHON\Progresso\Projetos sem OOP\MailMerge'
# Para melhor funcionamento
with open(r'Input\Nomes\names.txt', 'r') as texto:
    for i in texto.readlines():
        nome = i[:i.find('\n')]
        try:
            txt = fr'Output\Ready\{nome}.txt'
            with open(txt, 'x') as cr:
                with open(r'Input\Texto\parabens.txt', 'r') as para:
                    for j in para.readlines():
                        if '[name]' in j:
                            cr.writelines(f'{j[:j.find('[name]')]}{nome}\n')
                        else:
                            cr.writelines(j)
        except FileExistsError:
            txt = fr'Output\Ready\{nome}.txt'
            with open(txt, 'w') as cr:
                with open(r'Input\Texto\parabens.txt', 'r') as para:
                    for j in para.readlines():
                        if '[name]' in j:
                            cr.writelines(f'{j[:j.find('[name]')]}{nome}\n')
                        else:
                            cr.writelines(j)
        