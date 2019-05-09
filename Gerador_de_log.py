# coding: utf-8

from datetime import datetime, timezone, timedelta

SERVIDOR_LOG = "\\\\df7562nt713\log_msc$\Log_"

def dia_hora_atual(opcao=1):
    data_e_hora_atuais = datetime.now()
    diferenca = timedelta(hours=-3)
    fuso_horario = timezone(diferenca)
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    # print(data_e_hora_sao_paulo)
    if opcao == 1:
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("%d-%m-%Y %H_%M_%S")
        return data_e_hora_sao_paulo_em_texto
    else:
        data_e_hora_sao_paulo_em_texto = data_e_hora_sao_paulo.strftime("\n%d/%m/%Y %H:%M:%S")
        return data_e_hora_sao_paulo_em_texto

def data_hora_log():
    DATA_HORA_LOG = dia_hora_atual(2)
    return DATA_HORA_LOG

DATA_HORA = dia_hora_atual()
DATA_HORA_LOG = dia_hora_atual(2)


# iniciando o arquivo de log
def inicializa_log(matricula):
    with open('%s\%s_%s.log' % (SERVIDOR_LOG, matricula, DATA_HORA), 'a') as fd:
        fd.write(DATA_HORA_LOG + " - Iniciando processo!")
        fd.close()

def escreve_log(matricula, log):
    with open('%s\%s_%s.log' % (SERVIDOR_LOG, matricula, DATA_HORA), 'a') as fd:
        fd.write(data_hora_log() + " - " + log)
        fd.close()

def finaliza_log(matricula):
    with open('%s\%s_%s.log' % (SERVIDOR_LOG, matricula, DATA_HORA), 'a') as fd:
        fd.write(data_hora_log() + " - Processo finalizado!\n.")
        fd.close()