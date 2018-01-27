import tensorflow as tf
import requests
import time as t
import os
import urllib.request
from bs4 import BeautifulSoup

from tkinter import *
import tkinter.messagebox

from PIL import Image, ImageTk
import numpy as np

np.random.seed(20160704)
tf.set_random_seed(20160704)

def op2Numpy(op):
    sess = tf.InteractiveSession()
    init = tf.global_variables_initializer()
    sess.run(init)
    ret = sess.run(op)
    sess.close()

    return ret

def GetNowImage():
    url = 'http://www.kma.go.kr/repositary/image/rdr/site/RDR_PSN_latest.png'

    urllib.request.urlretrieve(url, './latest/latest.png')

    image_case = []
    image_case.append('./latest/latest.png')

    f = open('prediction.csv', 'w', encoding='UTF8')
    f2 = open('prediction2.csv', 'w', encoding='UTF8')
    sess = tf.InteractiveSession()

    f.write('1')
    f.write(',')
    f.write('9216' + ',')
    for i in range(0, 9215):
        f.write(''.join("0") + ',')
    f.write('\n')

    f2.write('1')
    f2.write(',')
    f2.write('5' + ',')
    for i in range(0, 4):
        f2.write(''.join("0") + ',')
    f2.write('\n')

    # 파일이름, 파일용도, for문범위, 처음 한줄 쓸것인가, case에 담길 이미지의 for문 범위, 강수량0도 포함할것인가, 그림+25
    k = 0
    for imagee in range(0, 1):  # 여기여기
        image = sess.run(tf.image.decode_png(tf.read_file(image_case[imagee]), channels=3))
        now = t.localtime()
        time = "%04d%02d%02d%02d00" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour)

        url = 'http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?' + time + '&0&MINDB_60M&159&b'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        # 기온
        soup1 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(8)')
        inp1 = ((str(soup1)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍향10
        soup2 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(13)')
        inp2 = ((str(soup2)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍속
        soup3 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(14)')
        inp3 = ((str(soup3)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 습도
        soup4 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(15)')
        inp4 = ((str(soup4)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 해면기압
        soup5 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(16)')
        inp5 = ((str(soup5)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))

        k = k + 1

        if (1):  # ~2000까지는 49
            for i in range(0, 96):
                for j in range(0, 96):
                    arr = (str.split((str(image[236 + i][209 + j])).strip('[').strip(']')), ' ')[0]  # 자료개방포털에서 받아온건 기존꺼에서 [+25][]
                    if arr[0] == "255" and arr[1] == "255" and arr[2] == "255":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "80" and arr[1] == "80" and arr[2] == "80":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "0" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "255" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "135" and arr[1] == "217" and arr[2] == "255":
                        f.write(''.join("0.2") + ',')
                    elif arr[0] == "62" and arr[1] == "193" and arr[2] == "255":
                        f.write(''.join("0.4") + ',')
                    elif arr[0] == "7" and arr[1] == "171" and arr[2] == "255":
                        f.write(''.join("0.6") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "222":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "255":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "179":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "255":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "105" and arr[1] == "252" and arr[2] == "105":
                        f.write(''.join("1.5") + ',')
                    elif arr[0] == "30" and arr[1] == "242" and arr[2] == "105":
                        f.write(''.join("2.0") + ',')
                    elif arr[0] == "0" and arr[1] == "213" and arr[2] == "0":
                        f.write(''.join("3.0") + ',')
                    elif arr[0] == "0" and arr[1] == "164" and arr[2] == "0":
                        f.write(''.join("4.0") + ',')
                    elif arr[0] == "0" and arr[1] == "128" and arr[2] == "0":
                        f.write(''.join("5.0") + ',')
                    elif arr[0] == "255" and arr[1] == "242" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "241" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "226" and arr[2] == "86":
                        f.write(''.join("7.0") + ',')
                    elif arr[0] == "255" and arr[1] == "208" and arr[2] == "57":
                        f.write(''.join("8.0") + ',')
                    elif arr[0] == "255" and arr[1] == "188" and arr[2] == "30":
                        f.write(''.join("9.0") + ',')
                    elif arr[0] == "255" and arr[1] == "170" and arr[2] == "9":
                        f.write(''.join("10.0") + ',')
                    elif arr[0] == "255" and arr[1] == "156" and arr[2] == "0":
                        f.write(''.join("12.0") + ',')
                    elif arr[0] == "255" and arr[1] == "139" and arr[2] == "27":
                        f.write(''.join("14.0") + ',')
                    elif arr[0] == "255" and arr[1] == "128" and arr[2] == "81":
                        f.write(''.join("16.0") + ',')
                    elif arr[0] == "255" and arr[1] == "110" and arr[2] == "110":
                        f.write(''.join("18.0") + ',')
                    elif arr[0] == "246" and arr[1] == "94" and arr[2] == "103":
                        f.write(''.join("20.0") + ',')
                    elif arr[0] == "232" and arr[1] == "74" and arr[2] == "86":
                        f.write(''.join("25.0") + ',')
                    elif arr[0] == "217" and arr[1] == "52" and arr[2] == "62":
                        f.write(''.join("30.0") + ',')
                    elif arr[0] == "201" and arr[1] == "31" and arr[2] == "37":
                        f.write(''.join("35.0") + ',')
                    elif arr[0] == "188" and arr[1] == "13" and arr[2] == "15":
                        f.write(''.join("40.0") + ',')
                    elif arr[0] == "179" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("50.0") + ',')
                    elif arr[0] == "197" and arr[1] == "90" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "197" and arr[1] == "125" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "194" and arr[1] == "52" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "194" and arr[1] == "62" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "173" and arr[1] == "7" and arr[2] == "255":
                        f.write(''.join("80.0") + ',')
                    elif arr[0] == "146" and arr[1] == "0" and arr[2] == "228":
                        f.write(''.join("90.0") + ',')
                    elif arr[0] == "127" and arr[1] == "0" and arr[2] == "191":
                        f.write(''.join("100.0") + ',')
                    else:
                        f.write(''.join(str(arr[0])))
                        f.write(''.join(str(arr[1])))
                        f.write(''.join(str(arr[2])) + ',')
            deg_case = [0, 0, 0, 0]
            deg = list(inp2)
            for kk in deg:
                if (kk == 'E'):
                    deg_case[0] = deg_case[0] + 1
                elif (kk == 'W'):
                    deg_case[1] = deg_case[1] + 1
                elif (kk == 'S'):
                    deg_case[2] = deg_case[2] + 1
                elif (kk == 'N'):
                    deg_case[3] = deg_case[3] + 1

            f2.write(''.join(str(deg_case[0])) + ',')
            f2.write(''.join(str(deg_case[1])) + ',')
            f2.write(''.join(str(deg_case[2])) + ',')
            f2.write(''.join(str(deg_case[3])) + ',')
            f2.write(''.join(str(inp3)) + ',')

            gang = float(str(gangsu))
            if (gang == 0):
                gangsu = 0
            elif (gang < 10 and gang > 0):
                gangsu = 10
            elif (gang < 20 and gang >= 10):
                gangsu = 20
            else:
                gangsu = 30
            f.write(''.join(str(0)) + ',')
            f2.write(''.join(str(0)) + ',')
            f.write('\n')
            f2.write('\n')
    f.close()
    f2.close()
    print("dataset 완성")


def GetImageWeb(i, j, k, l):
    if (int(j) < 10) : j = '0' + str(j)
    if (int(k) < 10) : k = '0' + str(k)
    if (int(l) < 10) : l = '0' + str(l)
    time = i + j + k + l + '00'

    try : urllib.request.urlretrieve('http://www.kma.go.kr/DATA/OPENAPI/RDR/IMG/PSN/' + i + j + '/' + k +
                                     '/RDR_PSN_' + i + j + k + l + '00.png','./latest/latest.png')
    except Exception :
        return 1

    image_case = []
    image_case.append('./latest/latest.png')

    f = open('prediction.csv', 'w', encoding='UTF8')
    f2 = open('prediction2.csv', 'w', encoding='UTF8')
    sess = tf.InteractiveSession()

    f.write('1')
    f.write(',')
    f.write('9216' + ',')
    for i in range(0, 9215):
        f.write(''.join("0") + ',')
    f.write('\n')

    f2.write('1')
    f2.write(',')
    f2.write('5' + ',')
    for i in range(0, 4):
        f2.write(''.join("0") + ',')
    f2.write('\n')

    # 파일이름, 파일용도, for문범위, 처음 한줄 쓸것인가, case에 담길 이미지의 for문 범위, 강수량0도 포함할것인가, 그림+25
    k = 0
    for imagee in range(0, 1):  # 여기여기
        image = sess.run(tf.image.decode_png(tf.read_file(image_case[imagee]), channels=3))
        si = (int(time) / 100) % 100 + 1
        namegy = int(time) / 10000
        if (si >= 10):
            time2 = str(int(namegy)) + str(int(si)) + '00'
        else:
            time2 = str(int(namegy)) + '0' + str(int(si)) + '00'

        url = 'http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?' + time2 + '&0&MINDB_60M&159&b'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        # 강수(15분전:제일단기간동안 내린 강수량값)
        soup6 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(4)')
        gangsu = ((str(soup6)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))

        url = 'http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?' + time + '&0&MINDB_60M&159&b'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        # 기온
        soup1 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(8)')
        inp1 = ((str(soup1)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍향10
        soup2 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(13)')
        inp2 = ((str(soup2)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍속
        soup3 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(14)')
        inp3 = ((str(soup3)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 습도
        soup4 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(15)')
        inp4 = ((str(soup4)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 해면기압
        soup5 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(16)')
        inp5 = ((str(soup5)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))

        k = k + 1

        if (1):  # ~2000까지는 49
            for i in range(0, 96):
                for j in range(0, 96):
                    arr = (str.split((str(image[236 + i][209 + j])).strip('[').strip(']')), ' ')[0]  # 자료개방포털에서 받아온건 기존꺼에서 [+25][]
                    if arr[0] == "255" and arr[1] == "255" and arr[2] == "255":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "80" and arr[1] == "80" and arr[2] == "80":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "0" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "255" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "135" and arr[1] == "217" and arr[2] == "255":
                        f.write(''.join("0.2") + ',')
                    elif arr[0] == "62" and arr[1] == "193" and arr[2] == "255":
                        f.write(''.join("0.4") + ',')
                    elif arr[0] == "7" and arr[1] == "171" and arr[2] == "255":
                        f.write(''.join("0.6") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "222":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "255":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "179":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "255":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "105" and arr[1] == "252" and arr[2] == "105":
                        f.write(''.join("1.5") + ',')
                    elif arr[0] == "30" and arr[1] == "242" and arr[2] == "105":
                        f.write(''.join("2.0") + ',')
                    elif arr[0] == "0" and arr[1] == "213" and arr[2] == "0":
                        f.write(''.join("3.0") + ',')
                    elif arr[0] == "0" and arr[1] == "164" and arr[2] == "0":
                        f.write(''.join("4.0") + ',')
                    elif arr[0] == "0" and arr[1] == "128" and arr[2] == "0":
                        f.write(''.join("5.0") + ',')
                    elif arr[0] == "255" and arr[1] == "242" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "241" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "226" and arr[2] == "86":
                        f.write(''.join("7.0") + ',')
                    elif arr[0] == "255" and arr[1] == "208" and arr[2] == "57":
                        f.write(''.join("8.0") + ',')
                    elif arr[0] == "255" and arr[1] == "188" and arr[2] == "30":
                        f.write(''.join("9.0") + ',')
                    elif arr[0] == "255" and arr[1] == "170" and arr[2] == "9":
                        f.write(''.join("10.0") + ',')
                    elif arr[0] == "255" and arr[1] == "156" and arr[2] == "0":
                        f.write(''.join("12.0") + ',')
                    elif arr[0] == "255" and arr[1] == "139" and arr[2] == "27":
                        f.write(''.join("14.0") + ',')
                    elif arr[0] == "255" and arr[1] == "128" and arr[2] == "81":
                        f.write(''.join("16.0") + ',')
                    elif arr[0] == "255" and arr[1] == "110" and arr[2] == "110":
                        f.write(''.join("18.0") + ',')
                    elif arr[0] == "246" and arr[1] == "94" and arr[2] == "103":
                        f.write(''.join("20.0") + ',')
                    elif arr[0] == "232" and arr[1] == "74" and arr[2] == "86":
                        f.write(''.join("25.0") + ',')
                    elif arr[0] == "217" and arr[1] == "52" and arr[2] == "62":
                        f.write(''.join("30.0") + ',')
                    elif arr[0] == "201" and arr[1] == "31" and arr[2] == "37":
                        f.write(''.join("35.0") + ',')
                    elif arr[0] == "188" and arr[1] == "13" and arr[2] == "15":
                        f.write(''.join("40.0") + ',')
                    elif arr[0] == "179" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("50.0") + ',')
                    elif arr[0] == "197" and arr[1] == "90" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "197" and arr[1] == "125" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "194" and arr[1] == "52" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "194" and arr[1] == "62" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "173" and arr[1] == "7" and arr[2] == "255":
                        f.write(''.join("80.0") + ',')
                    elif arr[0] == "146" and arr[1] == "0" and arr[2] == "228":
                        f.write(''.join("90.0") + ',')
                    elif arr[0] == "127" and arr[1] == "0" and arr[2] == "191":
                        f.write(''.join("100.0") + ',')
                    else:
                        f.write(''.join(str(arr[0])))
                        f.write(''.join(str(arr[1])))
                        f.write(''.join(str(arr[2])) + ',')
            deg_case = [0, 0, 0, 0]
            deg = list(inp2)
            for kk in deg:
                if (kk == 'E'):
                    deg_case[0] = deg_case[0] + 1
                elif (kk == 'W'):
                    deg_case[1] = deg_case[1] + 1
                elif (kk == 'S'):
                    deg_case[2] = deg_case[2] + 1
                elif (kk == 'N'):
                    deg_case[3] = deg_case[3] + 1

            f2.write(''.join(str(deg_case[0])) + ',')
            f2.write(''.join(str(deg_case[1])) + ',')
            f2.write(''.join(str(deg_case[2])) + ',')
            f2.write(''.join(str(deg_case[3])) + ',')
            f2.write(''.join(str(inp3)) + ',')

            gang = float(str(gangsu))
            if (gang == 0):
                gangsu = 0
            elif (gang < 10 and gang > 0):
                gangsu = 10
            elif (gang < 20 and gang >= 10):
                gangsu = 20
            else:
                gangsu = 30
            f.write(''.join(str(gangsu)) + ',')
            f.write('\n')
            f2.write(''.join(str(gangsu)) + ',')
            f2.write('\n')
    f.close()
    f2.close()
    print("dataset 완성")

def GetImageFile(i, j, k, l):
    # image crowling
    image_case = []
    if (int(j) < 10) : j = '0' + str(j)
    if (int(k) < 10) : k = '0' + str(k)
    if (int(l) < 10) :
        if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) + '/RDR_PSN_' + str(l) + '_' +
                               str(i) + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + str(k) + '0' + str(l) + '00.png')):
            image_case.append((str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) + '/RDR_PSN_' + str(l) +
                               '_' + str(i) + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + str(k) + '0' + str(l) + '00.png'))
    else :
        if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) + '/RDR_PSN_' + str(l) + '_' +
                               str(i) + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + str(k) + str(l) + '00.png')):
            image_case.append((str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) + '/RDR_PSN_' + str(l) +
                               '_' + str(i) + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + str(k) + str(l) + '00.png'))

    if (len(image_case)==0) : return 1 #이미지가 없을 경우 중단

    f = open('prediction.csv', 'w', encoding='UTF8')
    f2 = open('prediction2.csv', 'w', encoding='UTF8')
    sess = tf.InteractiveSession()

    f.write('1')
    f.write(',')
    f.write('9216' + ',')
    for i in range(0, 9215):
        f.write(''.join("0") + ',')
    f.write('\n')

    f2.write('1')
    f2.write(',')
    f2.write('5' + ',')
    for i in range(0, 4):
        f2.write(''.join("0") + ',')
    f2.write('\n')

    # 파일이름, 파일용도, for문범위, 처음 한줄 쓸것인가, case에 담길 이미지의 for문 범위, 강수량0도 포함할것인가, 그림+25
    if (int(l) < 10): l = '0' + str(l)
    time = str(i) + str(j) + str(k) + str(l) + str('00')
    k = 0
    for imagee in range(0, 1):  # 여기여기
        image = sess.run(tf.image.decode_png(tf.read_file(image_case[imagee]), channels=3))
        si = (int(time) / 100) % 100 + 1
        namegy = int(time) / 10000
        if (si >= 10):
            time2 = str(int(namegy)) + str(int(si)) + '00'
        else:
            time2 = str(int(namegy)) + '0' + str(int(si)) + '00'

        url = 'http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?' + time2 + '&0&MINDB_60M&159&b'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        # 강수(15분전:제일단기간동안 내린 강수량값)
        soup6 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(4)')
        gangsu = ((str(soup6)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))

        url = 'http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?' + time + '&0&MINDB_60M&159&b'

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')

        # 기온
        soup1 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(8)')
        inp1 = ((str(soup1)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍향10
        soup2 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(13)')
        inp2 = ((str(soup2)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 풍속
        soup3 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(14)')
        inp3 = ((str(soup3)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 습도
        soup4 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(15)')
        inp4 = ((str(soup4)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))
        # 해면기압
        soup5 = soup.select('body > table > tr > td > table > tr:nth-of-type(2) > td:nth-of-type(16)')
        inp5 = ((str(soup5)).strip('[').strip(']').strip('<td>').strip('</').strip(' class="textb">'))

        k = k + 1

        if (1):  # ~2000까지는 49
            for i in range(0, 96):
                for j in range(0, 96):
                    arr = (str.split((str(image[211 + i][209 + j])).strip('[').strip(']')), ' ')[0]  # 자료개방포털에서 받아온건 기존꺼에서 [+25][]
                    if arr[0] == "255" and arr[1] == "255" and arr[2] == "255":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "80" and arr[1] == "80" and arr[2] == "80":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "0" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "255" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "224" and arr[1] == "224" and arr[2] == "224":
                        f.write(''.join("0") + ',')
                    elif arr[0] == "135" and arr[1] == "217" and arr[2] == "255":
                        f.write(''.join("0.2") + ',')
                    elif arr[0] == "62" and arr[1] == "193" and arr[2] == "255":
                        f.write(''.join("0.4") + ',')
                    elif arr[0] == "7" and arr[1] == "171" and arr[2] == "255":
                        f.write(''.join("0.6") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "222":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "141" and arr[2] == "255":
                        f.write(''.join("0.8") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "179":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "0" and arr[1] == "119" and arr[2] == "255":
                        f.write(''.join("1.0") + ',')
                    elif arr[0] == "105" and arr[1] == "252" and arr[2] == "105":
                        f.write(''.join("1.5") + ',')
                    elif arr[0] == "30" and arr[1] == "242" and arr[2] == "105":
                        f.write(''.join("2.0") + ',')
                    elif arr[0] == "0" and arr[1] == "213" and arr[2] == "0":
                        f.write(''.join("3.0") + ',')
                    elif arr[0] == "0" and arr[1] == "164" and arr[2] == "0":
                        f.write(''.join("4.0") + ',')
                    elif arr[0] == "0" and arr[1] == "128" and arr[2] == "0":
                        f.write(''.join("5.0") + ',')
                    elif arr[0] == "255" and arr[1] == "242" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "241" and arr[2] == "111":
                        f.write(''.join("6.0") + ',')
                    elif arr[0] == "255" and arr[1] == "226" and arr[2] == "86":
                        f.write(''.join("7.0") + ',')
                    elif arr[0] == "255" and arr[1] == "208" and arr[2] == "57":
                        f.write(''.join("8.0") + ',')
                    elif arr[0] == "255" and arr[1] == "188" and arr[2] == "30":
                        f.write(''.join("9.0") + ',')
                    elif arr[0] == "255" and arr[1] == "170" and arr[2] == "9":
                        f.write(''.join("10.0") + ',')
                    elif arr[0] == "255" and arr[1] == "156" and arr[2] == "0":
                        f.write(''.join("12.0") + ',')
                    elif arr[0] == "255" and arr[1] == "139" and arr[2] == "27":
                        f.write(''.join("14.0") + ',')
                    elif arr[0] == "255" and arr[1] == "128" and arr[2] == "81":
                        f.write(''.join("16.0") + ',')
                    elif arr[0] == "255" and arr[1] == "110" and arr[2] == "110":
                        f.write(''.join("18.0") + ',')
                    elif arr[0] == "246" and arr[1] == "94" and arr[2] == "103":
                        f.write(''.join("20.0") + ',')
                    elif arr[0] == "232" and arr[1] == "74" and arr[2] == "86":
                        f.write(''.join("25.0") + ',')
                    elif arr[0] == "217" and arr[1] == "52" and arr[2] == "62":
                        f.write(''.join("30.0") + ',')
                    elif arr[0] == "201" and arr[1] == "31" and arr[2] == "37":
                        f.write(''.join("35.0") + ',')
                    elif arr[0] == "188" and arr[1] == "13" and arr[2] == "15":
                        f.write(''.join("40.0") + ',')
                    elif arr[0] == "179" and arr[1] == "0" and arr[2] == "0":
                        f.write(''.join("50.0") + ',')
                    elif arr[0] == "197" and arr[1] == "90" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "197" and arr[1] == "125" and arr[2] == "255":
                        f.write(''.join("60.0") + ',')
                    elif arr[0] == "194" and arr[1] == "52" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "194" and arr[1] == "62" and arr[2] == "255":
                        f.write(''.join("70.0") + ',')
                    elif arr[0] == "173" and arr[1] == "7" and arr[2] == "255":
                        f.write(''.join("80.0") + ',')
                    elif arr[0] == "146" and arr[1] == "0" and arr[2] == "228":
                        f.write(''.join("90.0") + ',')
                    elif arr[0] == "127" and arr[1] == "0" and arr[2] == "191":
                        f.write(''.join("100.0") + ',')
                    else:
                        f.write(''.join(str(arr[0])))
                        f.write(''.join(str(arr[1])))
                        f.write(''.join(str(arr[2])) + ',')
            deg_case = [0, 0, 0, 0]
            deg = list(inp2)
            for kk in deg:
                if (kk == 'E'):
                    deg_case[0] = deg_case[0] + 1
                elif (kk == 'W'):
                    deg_case[1] = deg_case[1] + 1
                elif (kk == 'S'):
                    deg_case[2] = deg_case[2] + 1
                elif (kk == 'N'):
                    deg_case[3] = deg_case[3] + 1

            f2.write(''.join(str(deg_case[0])) + ',')
            f2.write(''.join(str(deg_case[1])) + ',')
            f2.write(''.join(str(deg_case[2])) + ',')
            f2.write(''.join(str(deg_case[3])) + ',')
            f2.write(''.join(str(inp3)) + ',')

            gang = float(str(gangsu))
            if (gang == 0):
                gangsu = 0
            elif (gang < 10 and gang > 0):
                gangsu = 10
            elif (gang < 20 and gang >= 10):
                gangsu = 20
            else:
                gangsu = 30
            f.write(''.join(str(gangsu)) + ',')
            f.write('\n')
            f2.write(''.join(str(gangsu)) + ',')
            f2.write('\n')
    f.close()
    f2.close()
    print("dataset 완성")

def resultLink() :
    i = txtYear1.get()
    j = txtMonth1.get()
    k = txtDay1.get()
    l = txtTime1.get()

def PrintResult():
    '''top = Toplevel()
    top.title("결과")
    top.geometry("200x300+600+200")

    top_frame = Frame(top)
    top_frame.pack()'''
    #testing start

    # 프레임영역#
    base_frame = Frame(root)
    base_frame.pack()

    score = tf.Variable(initial_value=0.0, name="score", dtype=tf.float32)

    # 데이터셋을 불러옵니다.
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename="prediction.csv",
        target_dtype=np.int,
        features_dtype=np.float32)

    plus_test = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename="prediction2.csv",
        target_dtype=np.int,
        features_dtype=np.float32)

    # 모든 특성이 실수값을 가지고 있다고 지정합니다


    x = tf.placeholder(tf.float32, [None, 9216])

    x_image = tf.reshape(x, [-1, 96, 96, 1])

    num_filters1 = 32
    W_conv1 = tf.Variable(
        tf.truncated_normal([5, 5, 1, num_filters1], stddev=0.1))  # [5,5]:커널크기, 1:입력값x의 특성수, num_filter1: 필터갯수
    h_conv1 = tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding='SAME')  # SAME옵션 : 크기를 패딩값을 이용해 보존
    b_conv1 = tf.Variable(tf.constant(0.1, shape=[num_filters1]))
    h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)
    h_pool1 = tf.nn.max_pool(h_conv1_cutoff, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define second layer
    num_filters2a = 64
    W_conv2a = tf.Variable(tf.truncated_normal([5, 5, num_filters1, num_filters2a], stddev=0.1))
    h_conv2a = tf.nn.conv2d(h_pool1, W_conv2a, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2a = tf.Variable(tf.constant(0.1, shape=[num_filters2a]))
    h_conv2_cutoffa = tf.nn.relu(h_conv2a + b_conv2a)
    h_pool2a = tf.nn.max_pool(h_conv2_cutoffa, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 3th layer
    num_filters2b = 32
    W_conv2b = tf.Variable(tf.truncated_normal([5, 5, num_filters2a, num_filters2b], stddev=0.1))
    h_conv2b = tf.nn.conv2d(h_pool2a, W_conv2b, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2b = tf.Variable(tf.constant(0.1, shape=[num_filters2b]))
    h_conv2_cutoffb = tf.nn.relu(h_conv2b + b_conv2b)
    h_pool2b = tf.nn.max_pool(h_conv2_cutoffb, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 4th layer
    num_filters2c = 32
    W_conv2c = tf.Variable(tf.truncated_normal([5, 5, num_filters2b, num_filters2c], stddev=0.1))
    h_conv2c = tf.nn.conv2d(h_pool2b, W_conv2c, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2c = tf.Variable(tf.constant(0.1, shape=[num_filters2c]))
    h_conv2_cutoffc = tf.nn.relu(h_conv2c + b_conv2c)
    h_pool2c = tf.nn.max_pool(h_conv2_cutoffc, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 5th layer
    num_filters2 = 64
    W_conv2 = tf.Variable(tf.truncated_normal([5, 5, num_filters2c, num_filters2], stddev=0.1))
    h_conv2 = tf.nn.conv2d(h_pool2c, W_conv2, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2 = tf.Variable(tf.constant(0.1, shape=[num_filters2]))
    h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
    h_pool2 = tf.nn.max_pool(h_conv2_cutoff, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define fully connected layer
    pl = tf.placeholder(tf.float32, [None, 5])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 3 * 3 * num_filters2])

    h_pool2_flat = tf.concat([h_pool2_flat, pl], 1)
    num_units1 = 3 * 3 * num_filters2 + 5
    num_units2 = 1024
    w2 = tf.Variable(tf.truncated_normal([num_units1, num_units2]))
    b2 = tf.Variable(tf.constant(0.1, shape=[num_units2]))

    hidden2 = tf.nn.relu(tf.matmul(h_pool2_flat, w2) + b2)
    keep_prob = tf.placeholder(tf.float32)
    hidden2_drop = tf.nn.dropout(hidden2, keep_prob)
    w0 = tf.Variable(tf.zeros([num_units2, 4]))
    b0 = tf.Variable(tf.zeros([4]))
    k = tf.matmul(hidden2_drop, w0) + b0
    p = tf.nn.softmax(k)

    # define loss (cost) function
    t = tf.placeholder(tf.float32, [None, 4])
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=k, labels=t))
    train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)
    # correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 경사하강법으로 모델을 학습한다.
    init = tf.global_variables_initializer()

    print("Training")



    with tf.Session() as sess:
        sess.run(init)
        # 학습된 모델이 얼마나 정확한지를 출력한다.
        saver = tf.train.Saver()
        saver.restore(sess, './5layer_400data')

        y = tf.nn.softmax(k)
        res = tf.argmax(y, 1)
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        score = tf.assign(score, score + accuracy)

        for i in range(0, 1):
            if((sess.run(res[0], feed_dict={x: np.reshape(test_set.data[i], (-1, 9216)),
                                                               t: np.reshape(op2Numpy(
                                                                   tf.one_hot(int(int((test_set.target[i])) / 10), 4,
                                                                              on_value=1, off_value=0, axis=-1)),
                                                                             (-1, 4)),
                                                               pl: np.reshape(plus_test.data[i], (-1, 5)),
                                                               keep_prob: 0.5})) == 0) :

                reslabel = Label(base_frame, text="-----------------------------------------------------------------------------------------\n\n해가 쨍쨍")
                reslabel.grid(row=2, column=0, columnspan=7)
                reslabel.columnconfigure(0, weight=1)
                resized = Image.open("imgSun.png").resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized)

                resultLabel = Label(base_frame, image=photo)
                resultLabel.image = photo
                resultLabel.grid(row=3, column=0, columnspan=10)
                resultLabel.columnconfigure(0, weight=1)
            else :
                reslabel = Label(base_frame, text="-----------------------------------------------------------------------------------------\n\n비가 주룩주룩")
                reslabel.grid(row=2, column=0, columnspan=7)
                reslabel.columnconfigure(0, weight=1)
                resized = Image.open("imgRain.png").resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized)

                resultLabel = Label(base_frame, image=photo)
                resultLabel.image = photo
                resultLabel.grid(row=3, column=0, columnspan=10)
                resultLabel.columnconfigure(0, weight=1)
            '''if ((sess.run(accuracy, feed_dict={x: np.reshape(test_set.data[i], (-1, 9216)),
                                             t: np.reshape(op2Numpy(
                                                 tf.one_hot(int(int((test_set.target[i])) / 10), 4,
                                                            on_value=1, off_value=0, axis=-1)),
                                                 (-1, 4)),
                                             pl: np.reshape(plus_test.data[i], (-1, 5)),
                                             keep_prob: 0.5})) == 1.0):
                reslabel2 = Label(base_frame, text="예측 SUCCESS")
                reslabel2.grid(row=4, column=0, columnspan=7)
                reslabel2.columnconfigure(0, weight=1)
            else :
                reslabel2 = Label(base_frame, text="예측 FAILED")
                reslabel2.grid(row=4, column=0, columnspan=7)
                reslabel2.columnconfigure(0, weight=1)'''
    sess.close()

def PrintResult2():
    '''top = Toplevel()
    top.title("결과")
    top.geometry("200x300+600+200")

    top_frame = Frame(top)
    top_frame.pack()'''
    #testing start

    # 프레임영역#
    base_frame = Frame(root)
    base_frame.pack()

    score = tf.Variable(initial_value=0.0, name="score", dtype=tf.float32)

    # 데이터셋을 불러옵니다.
    test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename="prediction.csv",
        target_dtype=np.int,
        features_dtype=np.float32)

    plus_test = tf.contrib.learn.datasets.base.load_csv_with_header(
        filename="prediction2.csv",
        target_dtype=np.int,
        features_dtype=np.float32)

    # 모든 특성이 실수값을 가지고 있다고 지정합니다


    x = tf.placeholder(tf.float32, [None, 9216])

    x_image = tf.reshape(x, [-1, 96, 96, 1])

    num_filters1 = 32
    W_conv1 = tf.Variable(
        tf.truncated_normal([5, 5, 1, num_filters1], stddev=0.1))  # [5,5]:커널크기, 1:입력값x의 특성수, num_filter1: 필터갯수
    h_conv1 = tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding='SAME')  # SAME옵션 : 크기를 패딩값을 이용해 보존
    b_conv1 = tf.Variable(tf.constant(0.1, shape=[num_filters1]))
    h_conv1_cutoff = tf.nn.relu(h_conv1 + b_conv1)
    h_pool1 = tf.nn.max_pool(h_conv1_cutoff, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define second layer
    num_filters2a = 64
    W_conv2a = tf.Variable(tf.truncated_normal([5, 5, num_filters1, num_filters2a], stddev=0.1))
    h_conv2a = tf.nn.conv2d(h_pool1, W_conv2a, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2a = tf.Variable(tf.constant(0.1, shape=[num_filters2a]))
    h_conv2_cutoffa = tf.nn.relu(h_conv2a + b_conv2a)
    h_pool2a = tf.nn.max_pool(h_conv2_cutoffa, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 3th layer
    num_filters2b = 32
    W_conv2b = tf.Variable(tf.truncated_normal([5, 5, num_filters2a, num_filters2b], stddev=0.1))
    h_conv2b = tf.nn.conv2d(h_pool2a, W_conv2b, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2b = tf.Variable(tf.constant(0.1, shape=[num_filters2b]))
    h_conv2_cutoffb = tf.nn.relu(h_conv2b + b_conv2b)
    h_pool2b = tf.nn.max_pool(h_conv2_cutoffb, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 4th layer
    num_filters2c = 32
    W_conv2c = tf.Variable(tf.truncated_normal([5, 5, num_filters2b, num_filters2c], stddev=0.1))
    h_conv2c = tf.nn.conv2d(h_pool2b, W_conv2c, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2c = tf.Variable(tf.constant(0.1, shape=[num_filters2c]))
    h_conv2_cutoffc = tf.nn.relu(h_conv2c + b_conv2c)
    h_pool2c = tf.nn.max_pool(h_conv2_cutoffc, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define 5th layer
    num_filters2 = 64
    W_conv2 = tf.Variable(tf.truncated_normal([5, 5, num_filters2c, num_filters2], stddev=0.1))
    h_conv2 = tf.nn.conv2d(h_pool2c, W_conv2, strides=[1, 1, 1, 1], padding='SAME')
    b_conv2 = tf.Variable(tf.constant(0.1, shape=[num_filters2]))
    h_conv2_cutoff = tf.nn.relu(h_conv2 + b_conv2)
    h_pool2 = tf.nn.max_pool(h_conv2_cutoff, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

    # define fully connected layer
    pl = tf.placeholder(tf.float32, [None, 5])

    h_pool2_flat = tf.reshape(h_pool2, [-1, 3 * 3 * num_filters2])

    h_pool2_flat = tf.concat([h_pool2_flat, pl], 1)
    num_units1 = 3 * 3 * num_filters2 + 5
    num_units2 = 1024
    w2 = tf.Variable(tf.truncated_normal([num_units1, num_units2]))
    b2 = tf.Variable(tf.constant(0.1, shape=[num_units2]))

    hidden2 = tf.nn.relu(tf.matmul(h_pool2_flat, w2) + b2)
    keep_prob = tf.placeholder(tf.float32)
    hidden2_drop = tf.nn.dropout(hidden2, keep_prob)
    w0 = tf.Variable(tf.zeros([num_units2, 4]))
    b0 = tf.Variable(tf.zeros([4]))
    k = tf.matmul(hidden2_drop, w0) + b0
    p = tf.nn.softmax(k)

    # define loss (cost) function
    t = tf.placeholder(tf.float32, [None, 4])
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=k, labels=t))
    train_step = tf.train.AdamOptimizer(0.0001).minimize(loss)
    # correct_prediction = tf.equal(tf.argmax(p, 1), tf.argmax(t, 1))
    # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    # 경사하강법으로 모델을 학습한다.
    init = tf.global_variables_initializer()

    print("Training")



    with tf.Session() as sess:
        sess.run(init)
        # 학습된 모델이 얼마나 정확한지를 출력한다.
        saver = tf.train.Saver()
        saver.restore(sess, '/tmp/5layer_400data')

        y = tf.nn.softmax(k)
        res = tf.argmax(y, 1)
        correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(t, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        score = tf.assign(score, score + accuracy)

        for i in range(0, 1):
            if((sess.run(res[0], feed_dict={x: np.reshape(test_set.data[i], (-1, 9216)),
                                                               t: np.reshape(op2Numpy(
                                                                   tf.one_hot(int(int((test_set.target[i])) / 10), 4,
                                                                              on_value=1, off_value=0, axis=-1)),
                                                                             (-1, 4)),
                                                               pl: np.reshape(plus_test.data[i], (-1, 5)),
                                                               keep_prob: 0.5})) == 0) :

                reslabel = Label(base_frame, text="-----------------------------------------------------------------------------------------\n\n해가 쨍쨍")
                reslabel.grid(row=2, column=0, columnspan=7)
                reslabel.columnconfigure(0, weight=1)
                resized = Image.open("imgSun.png").resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized)

                resultLabel = Label(base_frame, image=photo)
                resultLabel.image = photo
                resultLabel.grid(row=3, column=0, columnspan=10)
                resultLabel.columnconfigure(0, weight=1)
            else :
                reslabel = Label(base_frame, text="-----------------------------------------------------------------------------------------\n\n비가 주룩주룩")
                reslabel.grid(row=2, column=0, columnspan=7)
                reslabel.columnconfigure(0, weight=1)
                resized = Image.open("imgRain.png").resize((200, 200), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(resized)

                resultLabel = Label(base_frame, image=photo)
                resultLabel.image = photo
                resultLabel.grid(row=3, column=0, columnspan=10)
                resultLabel.columnconfigure(0, weight=1)
    sess.close()

def Msgbox():
    GetNowImage()
    root = Tk()
    Button(root, text='두근두근', command=PrintResult2).pack()
    root.mainloop()
def Msgbox1():
    i = txtYear1.get()
    j = txtMonth1.get()
    k = txtDay1.get()
    l = txtTime1.get()

    #2017.8.10 이후 레이더영상
    isExist = GetImageWeb(i, j, k, l)
    # 크롤링한 데이터가 없으면 경고창 출력
    if isExist :
        tkinter.messagebox.showinfo("경고", "기간초과 및 데이터 없음")
    # 크롤링한 데이터가 있으면 강수여부 출력
    else :
        root = Tk()
        Button(root, text='두근두근', command=PrintResult).pack()
        root.mainloop()

def Msgbox2():
    i = txtYear2.get()
    j = txtMonth2.get()
    k = txtDay2.get()
    l = txtTime2.get()

    #2015~2017.8.10일까지 레이더영상
    isExist = GetImageFile(i, j, k, l)
    # 데이터가 없으면 경고창 출력
    if isExist:
        tkinter.messagebox.showinfo("경고", "보유 데이터 없음")
    # 데이터가 있으면 csv파일 생성, 결과출력
    else:
        root = Tk()
        Button(root, text='두근두근', command=PrintResult).pack()
        root.mainloop()


#기본영역#
root = Tk()
root.title("강우예측시스템")
root.geometry("+500+200")

#프레임영역#
base_frame = Frame(root)
base_frame.pack()

#입력영역#

#현재 시간부터 1시간 뒤
label = Label(base_frame, text="지금")
label.grid(row=0, column=0, columnspan=7)
label.columnconfigure(0, weight=1)

btnSearch1 = Button(base_frame, text="부터 1시간 뒤 비가올까요", command=Msgbox) #GetNowImage함수로 이미지 받기 및 scv파일로 저장
btnSearch1.grid(row=1, column=0, columnspan=7) #columnspan = 셀병합
btnSearch1.columnconfigure(0, weight=1)

#2017.8.10 이후 중 이 시간부터 1시간뒤
label = Label(base_frame, text="2017.08.11부터")
label.grid(row=2, column=0, columnspan=7)
label.columnconfigure(0, weight=1)

txtYear1 = Entry(base_frame)
txtYear1.grid(row=3, column=0)

labelY = Label(base_frame, text="년")
labelY.grid(row=3,column=1)

txtMonth1 = Entry(base_frame)
txtMonth1.grid(row=3, column=2)

labelM = Label(base_frame, text="월")
labelM.grid(row=3,column=3)

txtDay1 = Entry(base_frame)
txtDay1.grid(row=3, column=4)

labelD = Label(base_frame, text="일")
labelD.grid(row=3,column=5)

txtTime1 = Entry(base_frame)
txtTime1.grid(row=3, column=6)

labelT = Label(base_frame, text="시")
labelT.grid(row=3,column=7)

btnSearch2 = Button(base_frame, text="부터 1시간 뒤 비가올까요", command=Msgbox1) #Msgbox1함수로 이미지 받기 및 scv파일로 저장
btnSearch2.grid(row=4, column=0, columnspan=7) #columnspan = 셀병합
btnSearch2.columnconfigure(0, weight=1)

#2015~2017.08.10 중 이 시간부터 1시간뒤
label = Label(base_frame, text="2015.01.01 ~ 2017.08.10")
label.grid(row=5, column=0, columnspan=7)
label.columnconfigure(0, weight=1)

txtYear2 = Entry(base_frame)
txtYear2.grid(row=6, column=0)

labelY = Label(base_frame, text="년")
labelY.grid(row=6,column=1)

txtMonth2 = Entry(base_frame)
txtMonth2.grid(row=6, column=2)

labelM = Label(base_frame, text="월")
labelM.grid(row=6,column=3)

txtDay2 = Entry(base_frame)
txtDay2.grid(row=6, column=4)

labelD = Label(base_frame, text="일")
labelD.grid(row=6,column=5)

txtTime2 = Entry(base_frame)
txtTime2.grid(row=6, column=6)

labelT = Label(base_frame, text="시")
labelT.grid(row=6,column=7)

btnSearch3 = Button(base_frame, text="부터 1시간 뒤 비가올까요", command=Msgbox2) #Msgbox2함수로 이미지 받기 및 scv파일로 저장
btnSearch3.grid(row=7, column=0, columnspan=7) #columnspan = 셀병합
btnSearch3.columnconfigure(0, weight=1)

root.mainloop()