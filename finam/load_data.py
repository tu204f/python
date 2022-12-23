# Программа скачание данных технического анализа с сайта finam.ru
import requests

token = "03AGdBq25UAIq4NLAQ-jGiCAA8_\
cbgkv5vXCiBFdO6lFhkhzsw7SnkhdByusOuho82a9t2yMIRB-K-k_tLjiPfVGfy0QNhNu3Bco\
5cV2dr_QZ5OOkfIrmuBOBfdbVRvTS_Q5XLGIqkg6Kw8v4bTZcBmQBDZXBNfDMpH5jbetssee_\
I_jz_BDlNWuyJFD0ylv64Gdqc03q9gHAMMgcCuN5pwlNr3-xYgvpQuAyV0rxQT_yT9wtkEMx7--\
biq_WQ4Ad2H6qJfizhFCstwHPCYpmhUpYxNBf5Hp6ZynAD4c7Q2Z117-Cers_\
KOUnFMDZjGIHhfHvFFf8dFKwb3zi21rV7ClCOVQuXiUbEr4r1hjVuwwpR-\
LuiPcJlpplSV2wzoM2RS-lQ-gkhIMDLo_9N4pbX9cEa_\
oCknGNGiPHjcuHt9rxi2Kku1D76XRc1KFIu1FqLdqTgL9BVNx1IJ--\
TygzrdEvOzfgqVu5F2X4zJbCy7tDaf4Et6dkvmkZdPVQb24GmQrPtDl125-n\
"

url = """https://export.finam.ru/export9.out?
         market=14&
         em=17456&
         token={token}&
         code=SPFB.SBRF&
         apply=0&
         df=4&
         mf=3&
         yf=2022&
         from=04.04.2022&
         dt=4&
         mt=3&
         yt=2022&
         to=04.04.2022&
         p=2&
         f=SPFB.SBRF_220404_220404&e=.csv&
         cn=SPFB.SBRF&
         dtf=1&
         tmf=1&
         MSOR=1&
         mstime=on&
         mstimever=1&
         sep=3&
         sep2=1&
         datf=5&
         at=1"""


def get_url():
    url = 'https://export.finam.ru/export9.ou?'
    
    url = url + 'market=14&'
    url = url + 'em=17456&'
    url = url + 'token=' + token + '&'
    url = url + 'code=SPFB.SBRF&'
    url = url + 'apply=0&'
    url = url + 'df=4&'
    url = url + 'mf=3&'
    url = url + 'yf=2022&'
    url = url + 'from=04.04.2022&'
    url = url + 'dt=4&'
    url = url + 'mt=3&'
    url = url + 't=2022&'
    url = url + 'to=04.04.2022&'
    url = url + 'p=2&'
    url = url + 'f=SPFB.SBRF_220404_220404&e=.csv&'
    url = url + 'cn=SPFB.SBRF&'
    url = url + 'dtf=1&'
    url = url + 'tmf=1&'
    url = url + 'MSOR=1&'
    url = url + 'mstime=on&'
    url = url + 'mstimever=1&'
    url = url + 'sep=3&'
    url = url + 'sep2=1&'
    url = url + 'datf=5&'
    url = url + 'at=1'

    return url

url = get_url()
print(url)

res = requests.get(get_url())


print(res)