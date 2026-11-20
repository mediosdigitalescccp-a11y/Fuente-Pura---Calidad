# Genera datos.js a partir de los bloques de la hoja "Data FP - Calidad 2026".
import json, collections
W12, W34 = 'W1-W2', 'W3-W4'
meta = [  # fecha, ola, alcance, impresiones, interacciones, reproducciones, thruplays, costo
("2026-11-05",W12,339098,554007,32512,445464,2958,82.54),("2026-11-06",W12,689475,1094368,66934,864901,6468,180.1),
("2026-11-07",W12,696884,1003632,63898,769164,6127,182.65),("2026-11-08",W12,627147,863900,57660,663580,5594,179.88),
("2026-11-09",W12,539342,753683,53994,572882,5491,180.9),("2026-11-10",W12,481597,662732,51537,513128,5229,181.25),
("2026-11-11",W12,438515,612412,48503,471678,5170,181.97),("2026-11-12",W12,474307,635071,47831,486375,4927,182.28),
("2026-11-13",W12,492038,644672,45580,499101,4555,180.12),("2026-11-14",W12,487643,621458,46956,476808,4769,182.54),
("2026-11-15",W12,448486,565502,43140,434929,4513,175.76),("2026-11-16",W34,222298,425420,10194,135769,919,83.98),
("2026-11-17",W34,234298,383509,3384,38264,284,83.38),("2026-11-18",W34,232110,357880,2926,30989,236,83.52),
("2026-11-19",W34,30510,37700,240,2280,11,9.09)]
yt = [  # fecha, ola, usuarios, impresiones, views, costo, clics, q25, q50, q75, q100
("2026-11-05",W12,93486,126188,25314,57.45,588,11184,7495,6032,5524),("2026-11-06",W12,276653,358297,55650,152.18,1079,19439,12794,10028,9110),
("2026-11-07",W12,342938,405922,56973,155.2,1148,17109,11548,8990,8124),("2026-11-08",W12,268679,362388,22854,153.59,1940,6507,3010,1815,1527),
("2026-11-09",W12,273780,349208,22859,154.22,1699,6023,3068,1842,1529),("2026-11-10",W12,273360,340631,21726,156.68,1954,5660,2987,1753,1473),
("2026-11-11",W12,269019,325897,26424,156.31,1347,6664,3760,2513,2122),("2026-11-12",W12,309811,385259,28010,155.28,1615,7420,4137,2529,2137),
("2026-11-13",W12,283374,348325,26076,158.75,1685,6548,3711,2334,1964),("2026-11-14",W12,280413,350433,24165,159.01,1566,6537,3431,2151,1815),
("2026-11-15",W12,286619,364800,24008,159.09,2144,6408,3440,2101,1748),("2026-11-16",W34,86956,79998,22174,36.95,98,12568,9859,8686,8025),
("2026-11-17",W34,175751,175142,38943,72.11,189,14650,11239,9712,8972),("2026-11-18",W34,172503,177430,19728,74.8,276,5305,3405,2527,2194),
("2026-11-19",W34,25069,30880,1642,11.85,72,485,238,129,109)]
gdn = [  # fecha, usuarios, impresiones, costo, clics
("2026-11-16",70685,332398,150.85,3431),("2026-11-17",51372,216712,81.87,930),("2026-11-18",60216,228699,78.3,792),("2026-11-19",35489,140155,55.45,529)]
diario=[]
for f,o,a,i,e,v,t,c in meta: diario.append(dict(canal='Meta',fecha=f,ola=o,alcance=a,impresiones=i,interacciones=e,reproducciones=v,thruplays=t,costo=c))
for f,o,u,i,v,c,k,q1,q2,q3,q4 in yt: diario.append(dict(canal='YouTube',fecha=f,ola=o,alcance=u,impresiones=i,reproducciones=v,clics=k,costo=c,q25=q1,q50=q2,q75=q3,q100=q4))
for f,u,i,c,k in gdn: diario.append(dict(canal='Display',fecha=f,ola=W34,alcance=u,impresiones=i,clics=k,costo=c))
olas=[dict(canal='Meta',ola=W12,alcance=2233025,frecuencia=3.59,cpm=0.24),dict(canal='Meta',ola=W34,alcance=321542,frecuencia=2.32,cpm=0.21),
 dict(canal='YouTube',ola=W12,alcance=1526811,frecuencia=2.8,cpm=0.44),dict(canal='YouTube',ola=W34,alcance=224117,frecuencia=1.3,cpm=0.43),
 dict(canal='Display',ola=W34,alcance=117777,frecuencia=4.7,cpm=0.42)]
tiktok=[dict(ola=W12,video='Agua Mineral',views=537835,perfil=2502,seguidores=5627,costo=407,likes=13310,url='https://www.tiktok.com/@fuentepura/video/7704808335958297876'),
 dict(ola=W12,video='Agua Gasificada',views=344852,perfil=1249,seguidores=3735,costo=405,likes=6252,url='https://www.tiktok.com/@fuentepura/video/7705054811720371462'),
 dict(ola=W34,video='Agua Mineral',views=37635,perfil=114,seguidores=21,costo=16.14,likes=2139,url='https://www.tiktok.com/@fuentepura/video/7704808335958297876'),
 dict(ola=W34,video='Agua Gasificada',views=447,perfil=100,seguidores=12,costo=0.12,likes=2139,url='https://www.tiktok.com/@fuentepura/video/7705054811720371462')]
cre_rows="""19|PPV_SPOT_CALIDAD_MINERAL_48s 2216 2548 181;PPV_SPOT_CALIDAD_GASIFICADA_50s 693 739 47;PPL_CALIDAD_V1 10023 11676 6;PPL_CALIDAD_V2 18930 22776 6
18|PPV_SPOT_CALIDAD_MINERAL_48s 21719 26348 1821;PPV_SPOT_CALIDAD_GASIFICADA_50s 13179 14293 873;PPL_CALIDAD_V1 60012 70493 50;PPL_CALIDAD_V2 174808 246747 182
17|PPV_SPOT_CALIDAD_MINERAL_48s 19446 22603 1425;PPV_SPOT_CALIDAD_GASIFICADA_50s 25172 28211 1741;PPL_CALIDAD_V1 57737 66794 42;PPL_CALIDAD_V2 181749 265901 176
16|PPV_SPOT_CALIDAD_MINERAL_48s 51385 62062 3493;PPV_SPOT_CALIDAD_GASIFICADA_50s 88451 118495 6546;PPL_CALIDAD_V1 68151 86040 62;PPL_CALIDAD_V2 107343 158823 93
15|PPV_SPOT_CALIDAD_MINERAL_48s 178698 208132 15576;PPV_SPOT_CALIDAD_GASIFICADA_50s 308398 357370 27564
14|PPV_SPOT_CALIDAD_MINERAL_48s 114666 127052 9051;PPV_SPOT_CALIDAD_GASIFICADA_50s 419141 494406 37905
13|PPV_SPOT_CALIDAD_MINERAL_48s 108893 123040 8170;PPV_SPOT_CALIDAD_GASIFICADA_50s 420151 521632 37410
12|PPV_SPOT_CALIDAD_MINERAL_48s 162658 187032 14232;PPV_SPOT_CALIDAD_GASIFICADA_50s 364962 448039 33599
11|PPV_SPOT_CALIDAD_MINERAL_48s 226238 283575 22513;PPV_SPOT_CALIDAD_GASIFICADA_50s 276669 328837 25990
10|PPV_SPOT_CALIDAD_MINERAL_48s 240685 288139 22221;PPV_SPOT_CALIDAD_GASIFICADA_50s 305171 374593 29316
09|PPV_SPOT_CALIDAD_MINERAL_48s 366346 461099 32222;PPV_SPOT_CALIDAD_GASIFICADA_50s 241236 292584 21772
08|PPV_SPOT_CALIDAD_MINERAL_48s 427987 545033 35661;PPV_SPOT_CALIDAD_GASIFICADA_50s 280247 318867 21999
07|PPV_SPOT_CALIDAD_MINERAL_48s 497863 628850 38815;PPV_SPOT_CALIDAD_GASIFICADA_50s 318768 374782 25083
06|PPV_SPOT_CALIDAD_MINERAL_48s 525265 726171 42362;PPV_SPOT_CALIDAD_GASIFICADA_50s 299676 368197 24572
05|PPV_SPOT_CALIDAD_MINERAL_48s 275973 422413 23679;PPV_SPOT_CALIDAD_GASIFICADA_50s 108206 131594 8833"""
creativos=[]
for line in cre_rows.split('\n'):
    d,rest=line.split('|')
    for it in rest.split(';'):
        n,a,i,e=it.split(); creativos.append(dict(fecha='2026-11-'+d,creativo=n,alcance=int(a),impresiones=int(i),interacciones=int(e)))
yt_vid_raw="""19 G4YsEIWVi2Y 3203 94 10 5 2 2;aiHWi4r6b4w 11780 189 49 21 8 6;dyWARNUkFYs 11041 696 269 133 76 65;zcWM8awGdFc 4856 663 248 169 135 120
18 G4YsEIWVi2Y 25399 803 54 26 13 9;aiHWi4r6b4w 45094 1301 212 110 50 37;dyWARNUkFYs 59707 9062 3622 2380 1869 1647;zcWM8awGdFc 47230 8562 3718 2682 2259 2013
17 G4YsEIWVi2Y 25951 895 55 25 14 11;aiHWi4r6b4w 41042 1517 201 92 45 33;dyWARNUkFYs 58403 19091 11355 9118 8087 7543;zcWM8awGdFc 49746 17440 11364 9402 8493 7930
16 G4YsEIWVi2Y 1634 81 17 9 4 3;aiHWi4r6b4w 6572 182 40 18 8 5;dyWARNUkFYs 37345 11322 7086 5634 5048 4688;zcWM8awGdFc 34447 10589 6811 5545 4996 4634
15 G4YsEIWVi2Y 44712 1154 124 64 24 18;aiHWi4r6b4w 140453 2496 501 226 99 73;dyWARNUkFYs 107544 9873 3830 2058 1355 1154;zcWM8awGdFc 72091 10485 4148 2838 2192 1919
14 G4YsEIWVi2Y 56267 1427 185 95 39 28;aiHWi4r6b4w 106132 1971 389 155 68 51;dyWARNUkFYs 106960 10319 4117 2177 1471 1271;zcWM8awGdFc 81074 10448 3961 2642 2001 1760
13 G4YsEIWVi2Y 60977 1710 221 125 45 31;aiHWi4r6b4w 104950 2356 396 175 77 57;dyWARNUkFYs 100733 10934 4099 2360 1631 1408;zcWM8awGdFc 81665 11076 4276 2888 2185 1915
12 G4YsEIWVi2Y 36967 1144 114 52 25 18;aiHWi4r6b4w 137926 3274 631 296 121 90;dyWARNUkFYs 122895 11545 4236 2420 1520 1315;zcWM8awGdFc 87471 12047 4881 3342 2702 2379
11 G4YsEIWVi2Y 39641 1206 94 43 20 14;aiHWi4r6b4w 109927 3091 561 256 117 85;dyWARNUkFYs 99777 10946 4065 2358 1657 1432;zcWM8awGdFc 76552 11181 4402 3039 2479 2190
10 G4YsEIWVi2Y 38508 1112 100 49 22 17;aiHWi4r6b4w 137274 2674 538 248 104 80;dyWARNUkFYs 104599 8965 3342 1772 1078 922;zcWM8awGdFc 60250 8975 3496 2343 1861 1650
09 G4YsEIWVi2Y 42476 1450 139 69 33 23;aiHWi4r6b4w 133097 3580 762 326 144 106;dyWARNUkFYs 104478 8810 3310 1709 1070 920;zcWM8awGdFc 69157 9019 3620 2419 1925 1696
08 G4YsEIWVi2Y 49097 1309 129 63 25 19;aiHWi4r6b4w 137844 2699 622 235 101 75;dyWARNUkFYs 108528 9160 3797 1688 1099 948;zcWM8awGdFc 66919 9686 3852 2557 1953 1731
07 G4YsEIWVi2Y 65914 2215 303 149 56 41;aiHWi4r6b4w 107927 3930 514 212 108 80;dyWARNUkFYs 96936 24735 12768 9318 7952 7309;zcWM8awGdFc 135145 26093 12629 9701 8021 7395
06 G4YsEIWVi2Y 74141 2443 329 174 67 50;aiHWi4r6b4w 74379 2217 412 157 81 61;dyWARNUkFYs 112173 26608 14491 10122 8658 7985;zcWM8awGdFc 97604 24382 13547 10240 8582 7944
05 G4YsEIWVi2Y 28224 777 205 90 38 27;aiHWi4r6b4w 15185 600 132 58 29 22;dyWARNUkFYs 38046 11938 7226 5567 4912 4581;zcWM8awGdFc 44733 11999 6770 4851 4165 3888"""
videos=[]
for line in yt_vid_raw.split('\n'):
    d,rest=line.split(' ',1)
    for it in rest.split(';'):
        v,i,vw,a,b,c,e=it.split(); videos.append(dict(fecha='2026-11-'+d,video=v,impresiones=int(i),views=int(vw),q25=int(a),q50=int(b),q75=int(c),q100=int(e)))
G={'male':'Hombre','female':'Mujer','unknown':'Desconocido','MALE':'Hombre','FEMALE':'Mujer','UNDETERMINED':'Desconocido'}
R={'Región Autónoma del Atlántico Norte':'RACCN','Región Autónoma del Atlántico Sur':'RACCS','North Caribbean Coast Autonomous Region':'RACCN','South Caribbean Coast Autonomous Region':'RACCS','Leon':'León','Esteli':'Estelí','Rio San Juan':'Río San Juan','Unknown':'Desconocido'}
reg=lambda x: R.get(x.replace(' Department',''),x.replace(' Department',''))
age=lambda x: {'65_UP':'65+','UNDETERMINED':'Desconocido','Unknown':'Desconocido'}.get(x,x.replace('_','-'))
aud=collections.OrderedDict()
def add(canal,dim,seg,valor,extra=0):
    k=(canal,dim,seg); v=aud.get(k,[0,0]); aud[k]=[v[0]+valor,v[1]+extra]
for g,v in [('female',215626),('male',257171),('unknown',1621),('female',1105208),('male',1061923),('unknown',7955)]: add('Meta','Género',G[g],v)
for a,v in [('18-24',120289),('25-34',146787),('35-44',98136),('45-54',59490),('55-64',33716),('65+',19382),('Unknown',2),('18-24',507356),('25-34',734533),('35-44',437329),('45-54',245828),('55-64',136550),('65+',81429),('Unknown',24)]: add('Meta','Edad',age(a),v)
for r,v in [('Boaco Department',11585),('Carazo Department',15110),('Chinandega Department',31809),('Chontales Department',15930),('Estelí Department',22996),('Granada Department',17028),('Jinotega Department',16924),('León Department',35090),('Madriz Department',8777),('Managua Department',156887),('Masaya Department',35524),('Matagalpa Department',35958),('Nueva Segovia Department',19103),('Región Autónoma del Atlántico Norte',18591),('Región Autónoma del Atlántico Sur',18389),('Rivas Department',19899),('Río San Juan Department',6953),('Unknown',30),
 ('Boaco Department',52245),('Carazo Department',70689),('Chinandega Department',145157),('Chontales Department',69077),('Estelí Department',105379),('Granada Department',72286),('Jinotega Department',84295),('León Department',147175),('Madriz Department',36220),('Managua Department',824521),('Masaya Department',154358),('Matagalpa Department',165124),('Nueva Segovia Department',79439),('Región Autónoma del Atlántico Norte',91470),('Región Autónoma del Atlántico Sur',76841),('Rivas Department',77774),('Río San Juan Department',32578),('Unknown',347)]: add('Meta','Región',reg(r),v)
# YouTube: valor = impresiones, extra = views
for g,vw,im in [('MALE',32673,173662),('FEMALE',48446,258536),('UNDETERMINED',1368,31252),('MALE',133356,1552453),('FEMALE',191140,1945994),('UNDETERMINED',9563,218901)]: add('YouTube','Género',G[g],im,vw)
for a,vw,im in [('18_24',15753,83969),('25_34',26579,141734),('35_44',18191,110305),('45_54',9722,47524),('55_64',5900,27269),('65_UP',4856,19175),('UNDETERMINED',1486,33474),('18_24',59802,687892),('25_34',105331,1147279),('35_44',71317,843733),('45_54',41549,392613),('55_64',26043,242091),('65_UP',19623,161220),('UNDETERMINED',10394,242520)]: add('YouTube','Edad',age(a),im,vw)
for r,vw,im in [('Nueva Segovia',1948,9383),('Chinandega',4753,22477),('Rio San Juan',371,1881),('Leon',4685,22704),('Boaco',1212,5538),('Carazo',2072,10189),('South Caribbean Coast Autonomous Region',1930,9323),('Managua',44215,275330),('Matagalpa',4143,20499),('Jinotega',1708,8557),('Granada',2475,13095),('North Caribbean Coast Autonomous Region',1596,8660),('Rivas',2214,10628),('Masaya',3743,19782),('Chontales',1726,8354),('Esteli',3113,14061),('Madriz',566,2902),
 ('Nueva Segovia',6582,63386),('Chinandega',17105,156697),('Rio San Juan',1422,13233),('Leon',17815,166218),('Boaco',4126,36758),('Carazo',7678,71027),('South Caribbean Coast Autonomous Region',7357,67866),('Managua',192887,2411853),('Matagalpa',15074,137624),('Jinotega',6342,59155),('Granada',9125,89724),('North Caribbean Coast Autonomous Region',6084,59499),('Rivas',8062,72676),('Masaya',14251,136369),('Chontales',6507,58835),('Esteli',11372,93217),('Madriz',2143,20559)]: add('YouTube','Región',reg(r),im,vw)
# Display: valor = impresiones, extra = clics
for g,im,ck in [('MALE',297608,1713),('FEMALE',429615,2641),('UNDETERMINED',189644,1320)]: add('Display','Género',G[g],im,ck)
for a,im,ck in [('18_24',149765,696),('25_34',220018,1488),('35_44',150280,935),('45_54',79749,519),('55_64',68093,387),('65_UP',47437,291),('UNDETERMINED',201525,1358)]: add('Display','Edad',age(a),im,ck)
for r,im,ck in [('Nueva Segovia',12314,86),('Chinandega',26538,207),('Rio San Juan',2245,12),('Leon',34055,185),('Boaco',6945,47),('Carazo',14661,101),('South Caribbean Coast Autonomous Region',13127,90),('Managua',672997,4094),('Matagalpa',23499,192),('Jinotega',9843,78),('Granada',19296,113),('North Caribbean Coast Autonomous Region',9865,74),('Rivas',14938,79),('Masaya',24040,143),('Chontales',10016,57),('Esteli',16665,88),('Madriz',3768,27)]: add('Display','Región',reg(r),im,ck)
audiencia=[dict(canal=c,dimension=d,segmento=s,valor=v[0],extra=v[1]) for (c,d,s),v in aud.items()]
tiktok_aud=dict(edad={'Agua Mineral':{W12:{'18-24':26,'25-34':45,'35-44':23,'45-54':6},W34:{'18-24':47,'25-34':36,'35-44':9,'45-54':4,'55+':4}},
                      'Agua Gasificada':{W12:{'18-24':19,'25-34':42,'35-44':27,'45-54':12},W34:{'18-24':19,'25-34':38,'35-44':27,'45-54':12,'55+':4}}},
                region={'Agua Mineral':{W12:{'Managua':69,'León':5,'Matagalpa':5,'Chinandega':4,'Masaya':4,'Otros':13},W34:{'Managua':67,'León':6,'Matagalpa':4,'Chinandega':4,'Masaya':4,'Otros':15}},
                        'Agua Gasificada':{W12:{'Managua':74,'León':4,'Matagalpa':4,'Chinandega':3,'Masaya':3,'Otros':12},W34:{'Managua':60,'León':8,'Matagalpa':6,'Chinandega':7,'Masaya':4,'Otros':15}}})
import sys
display=json.load(open(sys.argv[1]))
out=dict(actualizado='2026-11-19',diario=diario,olas=olas,tiktok=tiktok,creativos=creativos,videos=videos,display=display,audiencia=audiencia,tiktok_aud=tiktok_aud)
open(sys.argv[2],'w',encoding='utf-8').write('window.FP_DATA = '+json.dumps(out,ensure_ascii=False)+';\n')
print('filas', len(diario), len(creativos), len(videos), len(display), len(audiencia))
