# coding: utf-8

"""
    .NOTES
    ===========================================================================
    Created with:   PyCharm v2017.3.2
    Created on:   	07/05/2019 19:25
    Created by:   	P772920 - Mardonio Silva da Costa
    Organization: 	Caixa Econômica Federal / Stefanini
    Filename:     	Verifica_Maquina_ligada.py
    ===========================================================================
    .DESCRIPTION
    Faz a verificação se um equipamento ta ligado
    .UPDATES
        08/05/2019 - P772920 - Adicionado função para abertura de notepad noar.txt ao termino da verificação.
        08/05/2019 - P772920 - Adicionado função para verificação de maquinas EF se estão ligadas.
        08/05/2019 - P772920 - Adicionado função Geração de log.

"""

import os, time, threading, subprocess
from Gerador_de_log import inicializa_log, escreve_log, finaliza_log

class Monitor(threading.Thread):
    # Classe de monitoramento de threads
    def __init__(self, nome_logico):
        # contrutor da thread
        self.nome_logico = nome_logico
        self.status = None

        # inicializador da classe Thread
        threading.Thread.__init__(self)

    def run(self):
        # codico que será executado pela thread
        # execute o ping
        if nome_logico.__contains__('EF') or nome_logico.__contains__('ef'):
            ping = os.popen('ping -n 1 %s.diretorio.caixa' % self.nome_logico).read()
        else:
            ping = os.popen('ping -n 1 %s' % self.nome_logico).read()

        if 'Resposta' in ping:
            self.status = True
        else:
            self.status = False


if __name__ == '__main__':
    # Criar arquivo de log
    print(20 * '#' + "    VERIFICA MAQUINAS LIGADAS    " + 20 * '#')
    matricula = os.environ['USERNAME']
    inicializa_log(matricula)

    # Cria uma lista com um objeto de thread para cada nome logico
    monitores = []
    if os.path.isfile('foradoar.txt'):
        os.remove('foradoar.txt')

    if os.path.isfile('noar.txt'):
        os.remove('noar.txt')

    subprocess.call(['notepad.exe', 'nomelogico.txt'])
    print(20 * '#' + "    PROCESSANDO AGUARDE...    " + 20 * '#')
    with open('nomelogico.txt', 'r') as fd:
        for line in fd:
            nome_logico = (line[:-1])
            monitores.append(Monitor(nome_logico))
        fd.close()

    # executa as Thread

    for monitor in monitores:
        monitor.start()

    # A thread principal continua enquanto as outras thread executam o ping
    # para os nomes logicos da lista

    # verifica a cada segundo se as threads acabaram

    ping = True
    while ping:
        ping = False
        for monitor in monitores:
            if monitor.status == None:
                ping = True
                break
        time.sleep(1)

    # imprimindo o resultado
    # imprima os resultados no final
    total_de_equipamentos = str(len(monitores))

    for monitor in monitores:
        if monitor.status:
            # print('%s no ar' % monitor.nome_logico)
            with open('noar.txt', 'a') as fd:
                fd.write(monitor.nome_logico + "\n")
                fd.close()
        else:
            # print('%s for da ar' % monitor.nome_logico)
            with open('foradoar.txt', 'a') as fd:
                fd.write(monitor.nome_logico + "\n")
                fd.close()
    if not os.path.isfile('noar.txt'):
        with open('noar.txt', 'a') as fd:
            fd.write('\n ####\tNENHUM EQUIPAMENTO LIGADO\t####')
            fd.close()

    escreve_log(matricula, "%s Equipamento verificados" % total_de_equipamentos)
    finaliza_log(matricula)

    print(20*'#' + "    PROCESSO FINALIZADO    " + 20*'#')
    print((20*'#' + "    TOTAL DE EQUIPAMENTO VERIFICADOS: %s    " + 20*'#') % total_de_equipamentos)
    subprocess.Popen('noar.txt', shell=True)