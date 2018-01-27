import tensorflow as tf
import requests
import os
from bs4 import BeautifulSoup

image_case = [
]
#image_case.append // os.path.isfile
for i in (2015,2016,2017):
    for j in range(1,13):
        for k in range(1,32):
            for l in range(0,24):
                if(j<10):
                    if(k<10):
                        if(l<10):
                            if(os.path.isfile(str(i)+'_0'+str(j)+'/'+str(i)+'0'+str(j)+'0'+str(k)+'/RDR_PSN_'+str(l)+'_' + str(i) + '0' + str(j) + '0' + str(k) +'/RDR_QC_PSN_'+str(i)+'0'+str(j)+'0'+str(k)+'0'+str(l)+'00.png')):
                                image_case.append((
                                str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + '0' + str(k) + '/RDR_PSN_' + str(
                                    l) + '_' + str(i) + '0' + str(j) + '0' + str(k) + '/RDR_QC_PSN_' + str(i) + '0' + str(
                                    j) + '0' + str(k) + '0' + str(l) + '00.png'))

                        else :
                            if (os.path.isfile(str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + '0' + str(k) + '/RDR_PSN_'+str(l)+'_' + str(i) + '0' + str(j) + '0' + str(k)+'/RDR_QC_PSN_'+str(i) + '0' + str(j) + '0'+str(k)+str(l) + '00.png')):
                                image_case.append((
                                str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + '0' + str(k) + '/RDR_PSN_' + str(l) + '_' + str(
                                    i) + '0' + str(j) + '0' + str(k) + '/RDR_QC_PSN_' + str(i) + '0' + str(j) + '0' + str(k) + str(
                                    l) + '00.png'))
                    else :
                        if (l < 10):
                            if (os.path.isfile(str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + str(k) + '/RDR_PSN_'+str(l)+'_' +  str(i) + '0' + str(j) +str(k)  +'/RDR_QC_PSN_'+ str(i) + '0' + str(j) + str(k) + '0' + str(l) + '00.png')):
                                image_case.append((
                                str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + str(k) + '/RDR_PSN_' + str(
                                    l) + '_' + str(i) + '0' + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + '0' + str(
                                    j) + str(k) + '0' + str(l) + '00.png'))

                        else:
                            if (os.path.isfile(str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) +str(k) + '/RDR_PSN_'+str(l)+'_' +  str(i) + '0' + str(j) +str(k)  +'/RDR_QC_PSN_'+str(i) + '0' + str(j) + str(k) + str(l) + '00.png')):
                                image_case.append((
                                str(i) + '_0' + str(j) + '/' + str(i) + '0' + str(j) + str(k) + '/RDR_PSN_' + str(l) + '_' + str(
                                    i) + '0' + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + '0' + str(j) + str(k) + str(
                                    l) + '00.png'))

                else :
                    if (k < 10):
                        if (l < 10):
                            if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) +  str(j) + '0' + str(k) + '/RDR_PSN_'+str(l)+'_' + str(i) +  str(j) + '0' + str(k)  +'/RDR_QC_PSN_'+str(i) + str(j) + '0' + str(k) + '0' + str(l) + '00.png')):
                                image_case.append((
                                str(i) + '_' + str(j) + '/' + str(i) + str(j) + '0' + str(k) + '/RDR_PSN_' + str(
                                    l) + '_' + str(i) + str(j) + '0' + str(k) + '/RDR_QC_PSN_' + str(i) + str(
                                    j) + '0' + str(k) + '0' + str(l) + '00.png'))

                        else:
                            if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) + str(j) + '0' + str(k) + '/RDR_PSN_'+str(l)+'_' + str(i) +  str(j) + '0' + str(k)  +'/RDR_QC_PSN_'+str(i) + str(j) + '0' + str(k) + str(l) + '00.png')):
                                image_case.append((str(i) + '_' + str(j) + '/' + str(i) + str(j) + '0' + str(k) + '/RDR_PSN_' + str(l) + '_' + str(i) + str(j) + '0' + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + '0' + str(k) + str(l) + '00.png'))

                    else:
                        if (l < 10):
                            if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) +'/RDR_PSN_'+str(l)+'_' + str(i) + str(j) + str(k) +'/RDR_QC_PSN_'+str(i) + str(j) + str(k) + '0' + str(l) + '00.png')):
                                image_case.append((str(i) + '_' + str(j) + '/' + str(i) + str(j) + str(k) + '/RDR_PSN_' + str(l) + '_' + str(i) + str(j) + str(k) + '/RDR_QC_PSN_' + str(i) + str(j) + str(k) + '0' + str(l) + '00.png'))

                        else:
                            if (os.path.isfile(str(i) + '_' + str(j) + '/' + str(i) +  str(j) + str(k) + '/RDR_PSN_'+str(l)+'_' + str(i) + str(j) + str(k)  +'/RDR_QC_PSN_'+str(i)+ str(j) + str(k) + str(l) + '00.png')):
                                image_case.append ((str(i) + '_' + str(j) + '/' + str(i) +  str(j) + str(k) + '/RDR_PSN_'+str(l)+'_' + str(i) + str(j) + str(k)  +'/RDR_QC_PSN_'+str(i)+ str(j) + str(k) + str(l) + '00.png'))

f=open('new2.csv','a', encoding='UTF8')
sess = tf.InteractiveSession()

print(len(image_case))
print('9216'+',')
'''
f.write((str(len(image_case))).strip('\0'))
f.write(',')
f.write('9216'+',')
for i in range(0,9215):
    f.write(''.join("0") + ',')
f.write('\n')
'''

#파일이름, 파일용도, for문범위, 처음 한줄 쓸것인가, case에 담길 이미지의 for문 범위, 강수량0도 포함할것인가, 그림+25
k = 0
for imagee in range(1500,3000): #여기여기
    image = sess.run(tf.image.decode_png(tf.read_file(image_case[imagee]), channels=3))
    time = str.split((str(image_case[imagee])).strip('.png'),'_')
    time = time[7]
    #print(time)
    print(str(imagee) + " " + str(k))
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


    #if ((inp1) == ' ' or str(inp1) == '.' or str(inp2) == str(' ') or str(inp2) == '.' or str(inp3) == str(' ') or str(inp3) == '.' or str(inp4) == ' ' or str(inp4) == '.' or str(inp5) == ' ' or str(inp5) == '.' or str(gangsu) == str(' ') or str(gangsu) == '.'
    #    or inp1=='\xa0'  or str(inp2)=='\xa0'  or str(inp3)=='\xa0'  or inp4=='\xa0'  or inp5=='\xa0' or gangsu=='\xa0'):
    #    continue
    if (str(inp2) == str(' ') or str(inp2) == '.' or str(inp3) == str(' ') or str(inp3) == '.' or str(gangsu) == str(' ') or str(gangsu) == '.'
        or str(inp2)=='\xa0'  or str(inp3)=='\xa0' or gangsu=='\xa0') :
        continue

    print(inp1+'/'+inp2+'/' +inp3+'/' +inp4+'/' +inp5 +'/' +str(gangsu))

    k = k + 1

    if(1): # ~2000까지는 49
        for i in range(0,96):
            for j in range(0, 96):
                arr = (str.split((str(image[211+i][209+j])).strip('[').strip(']')), ' ')[0] #자료개방포털에서 받아온건 기존꺼에서 [+25][]
                if arr[0]=="255" and arr[1]=="255" and arr[2]=="255" :
                    f.write(''.join("0")+',')
                elif arr[0]=="224" and arr[1]=="224" and arr[2]=="224" :
                    f.write(''.join("0")+',')
                elif arr[0]=="80" and arr[1]=="80" and arr[2]=="80" :
                    f.write(''.join("0")+',')
                elif arr[0]=="0" and arr[1]=="0" and arr[2]=="0" :
                    f.write(''.join("0")+',')
                elif arr[0]=="255" and arr[1]=="0" and arr[2]=="0" :
                    f.write(''.join("0")+',')
                elif arr[0]=="224" and arr[1]=="224" and arr[2]=="224" :
                    f.write(''.join("0")+',')
                elif arr[0]=="135" and arr[1]=="217" and arr[2]=="255" :
                    f.write(''.join("0.2")+',')
                elif arr[0]=="62" and arr[1]=="193" and arr[2]=="255" :
                    f.write(''.join("0.4")+',')
                elif arr[0]=="7" and arr[1]=="171" and arr[2]=="255" :
                    f.write(''.join("0.6")+',')
                elif arr[0]=="0" and arr[1]=="141" and arr[2]=="222" :
                    f.write(''.join("0.8")+',')
                elif arr[0]=="0" and arr[1]=="141" and arr[2]=="255" :
                    f.write(''.join("0.8")+',')
                elif arr[0]=="0" and arr[1]=="119" and arr[2]=="179" :
                    f.write(''.join("1.0")+',')
                elif arr[0]=="0" and arr[1]=="119" and arr[2]=="255" :
                    f.write(''.join("1.0")+',')
                elif arr[0]=="105" and arr[1]=="252" and arr[2]=="105" :
                    f.write(''.join("1.5")+',')
                elif arr[0]=="30" and arr[1]=="242" and arr[2]=="105" :
                    f.write(''.join("2.0")+',')
                elif arr[0]=="0" and arr[1]=="213" and arr[2]=="0" :
                    f.write(''.join("3.0")+',')
                elif arr[0]=="0" and arr[1]=="164" and arr[2]=="0" :
                    f.write(''.join("4.0")+',')
                elif arr[0]=="0" and arr[1]=="128" and arr[2]=="0" :
                    f.write(''.join("5.0")+',')
                elif arr[0]=="255" and arr[1]=="242" and arr[2]=="111" :
                    f.write(''.join("6.0")+',')
                elif arr[0]=="255" and arr[1]=="241" and arr[2]=="111" :
                    f.write(''.join("6.0")+',')
                elif arr[0]=="255" and arr[1]=="226" and arr[2]=="86" :
                    f.write(''.join("7.0")+',')
                elif arr[0]=="255" and arr[1]=="208" and arr[2]=="57" :
                    f.write(''.join("8.0")+',')
                elif arr[0]=="255" and arr[1]=="188" and arr[2]=="30" :
                    f.write(''.join("9.0")+',')
                elif arr[0]=="255" and arr[1]=="170" and arr[2]=="9" :
                    f.write(''.join("10.0")+',')
                elif arr[0]=="255" and arr[1]=="156" and arr[2]=="0" :
                    f.write(''.join("12.0")+',')
                elif arr[0]=="255" and arr[1]=="139" and arr[2]=="27" :
                    f.write(''.join("14.0")+',')
                elif arr[0]=="255" and arr[1]=="128" and arr[2]=="81" :
                    f.write(''.join("16.0")+',')
                elif arr[0]=="255" and arr[1]=="110" and arr[2]=="110" :
                    f.write(''.join("18.0")+',')
                elif arr[0]=="246" and arr[1]=="94" and arr[2]=="103" :
                    f.write(''.join("20.0")+',')
                elif arr[0]=="232" and arr[1]=="74" and arr[2]=="86" :
                    f.write(''.join("25.0")+',')
                elif arr[0]=="217" and arr[1]=="52" and arr[2]=="62" :
                    f.write(''.join("30.0")+',')
                elif arr[0]=="201" and arr[1]=="31" and arr[2]=="37" :
                    f.write(''.join("35.0")+',')
                elif arr[0]=="188" and arr[1]=="13" and arr[2]=="15" :
                    f.write(''.join("40.0")+',')
                elif arr[0]=="179" and arr[1]=="0" and arr[2]=="0" :
                    f.write(''.join("50.0")+',')
                elif arr[0]=="197" and arr[1]=="90" and arr[2]=="255" :
                    f.write(''.join("60.0")+',')
                elif arr[0]=="197" and arr[1]=="125" and arr[2]=="255" :
                    f.write(''.join("60.0")+',')
                elif arr[0]=="194" and arr[1]=="52" and arr[2]=="255" :
                    f.write(''.join("70.0")+',')
                elif arr[0]=="194" and arr[1]=="62" and arr[2]=="255" :
                    f.write(''.join("70.0")+',')
                elif arr[0]=="173" and arr[1]=="7" and arr[2]=="255" :
                    f.write(''.join("80.0")+',')
                elif arr[0]=="146" and arr[1]=="0" and arr[2]=="228" :
                    f.write(''.join("90.0")+',')
                elif arr[0]=="127" and arr[1]=="0" and arr[2]=="191" :
                    f.write(''.join("100.0")+',')
                else:
                    f.write(''.join(str(arr[0])))
                    f.write(''.join(str(arr[1])))
                    f.write(''.join(str(arr[2]))+',')
        deg_case = [0,0,0,0]
        deg = list(inp2)
        for kk in deg:
            if(kk=='E'):
                deg_case[0] = deg_case[0] + 1
            elif(kk=='W'):
                deg_case[1] = deg_case[1] + 1
            elif (kk == 'S'):
                deg_case[2] = deg_case[2] + 1
            elif (kk == 'N'):
                deg_case[3] = deg_case[3] + 1

        f.write(''.join(str(deg_case[0])) + ',')
        f.write(''.join(str(deg_case[1])) + ',')
        f.write(''.join(str(deg_case[2])) + ',')
        f.write(''.join(str(deg_case[3])) + ',')
        f.write(''.join(str(inp3)) + ',')

        gang = float(str(gangsu))
        if(gang==0) : gangsu = 0
        elif(gang<10 and gang>0) : gangsu = 10
        elif (gang < 20 and gang >= 10): gangsu = 20
        else : gangsu = 30
        f.write(''.join(str(gangsu)) + ',')
        #f.write(''.join(str(int(round(float(gangsu)+0.5)))) + ',')
        #print(str(gangsu)+"  "+str(int(round(float(gangsu)+0.5))))
        f.write('\n')

f.close()