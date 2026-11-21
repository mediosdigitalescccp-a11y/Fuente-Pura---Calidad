# Genera datos.js a partir de datos/hoja.py y datos/gdn_ads.txt.  Uso: python3 datos/build_data.py
import json, collections, os, sys
D0 = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D0)
import hoja as H
W12, W34 = H.W12, H.W34
ola = lambda f: W12 if f <= '2026-11-15' else W34
L = lambda t: [l.split() for l in t.strip().split('\n')]
diario = []
for f, a, i, e, v, t, c in L(H.META): diario.append(dict(canal='Meta', fecha=f, ola=ola(f), alcance=int(a), impresiones=int(i), interacciones=int(e), reproducciones=int(v), thruplays=int(t), costo=float(c)))
for f, u, i, v, c, k, q1, q2, q3, q4 in L(H.YT): diario.append(dict(canal='YouTube', fecha=f, ola=ola(f), alcance=int(u), impresiones=int(i), reproducciones=int(v), clics=int(k), costo=float(c), q25=int(q1), q50=int(q2), q75=int(q3), q100=int(q4)))
for f, u, i, c, k in L(H.GDN): diario.append(dict(canal='Display', fecha=f, ola=W34, alcance=int(u), impresiones=int(i), clics=int(k), costo=float(c)))
olas = [dict(canal=c, ola=o, alcance=a, frecuencia=f, cpm=m) for c, o, a, f, m in H.OLAS]
tiktok = [dict(ola=o, video=v, views=vw, perfil=p, seguidores=s, costo=c, likes=l, url=H.TT_URL[v]) for o, v, vw, p, s, c, l in H.TIKTOK]
creativos = []
for line in H.META_CRE.split('\n'):
    d, rest = line.split('|')
    for it in rest.split(';'):
        n, a, i, e, *v = it.split(); creativos.append(dict(fecha='2026-11-' + d, creativo=n, alcance=int(a), impresiones=int(i), interacciones=int(e), reproducciones=int(v[0]) if v else None))
videos = []
for line in H.YT_VID.split('\n'):
    d, rest = line.split('|')
    for vid, it in zip(H.YT_IDS, rest.split(';')):
        i, vw, a, b, c, e = map(int, it.split()); videos.append(dict(fecha='2026-11-' + d, video=vid, impresiones=i, views=vw, q25=a, q50=b, q75=c, q100=e))
# Display por banner: nombre en Google Ads -> archivo de imagen en img/display
IMG = {'120x600_1': '160x600', '120x600_3': '160x600_2', '120x600_5': '160x600_4', '930x90': '970x90'}
tot = collections.OrderedDict()
for line in open(os.path.join(D0, 'gdn_ads.txt'), encoding='utf-8'):
    for it in line.strip().split(';'):
        if not it: continue
        a, i, c = it.split(); x = tot.setdefault(a, [0, 0]); x[0] += int(i); x[1] += int(c)
imgdir = os.path.join(D0, '..', 'img', 'display')
display = []
for a, (i, c) in tot.items():
    base = a.rsplit('.', 1)[0]; f = IMG.get(base, base)
    display.append(dict(nombre=base, img=f if os.path.exists(os.path.join(imgdir, f + '.jpg')) else None, impresiones=i, clics=c))
display.sort(key=lambda r: -r['impresiones'])
G = {'male': 'Hombre', 'female': 'Mujer', 'unknown': 'Desconocido', 'MALE': 'Hombre', 'FEMALE': 'Mujer', 'UNDETERMINED': 'Desconocido'}
R = {'Región Autónoma del Atlántico Norte': 'RACCN', 'Región Autónoma del Atlántico Sur': 'RACCS', 'North Caribbean Coast Autonomous Region': 'RACCN', 'South Caribbean Coast Autonomous Region': 'RACCS', 'Leon': 'León', 'Esteli': 'Estelí', 'Rio San Juan': 'Río San Juan', 'Unknown': 'Desconocido'}
reg = lambda x: R.get(x.replace(' Department', ''), x.replace(' Department', ''))
age = lambda x: {'65_UP': '65+', 'UNDETERMINED': 'Desconocido', 'Unknown': 'Desconocido'}.get(x, x.replace('_', '-'))
aud = []
aud += [dict(canal='Meta', dimension='Género', segmento=G[k], valor=v, extra=0) for k, v in H.META_GEN]
aud += [dict(canal='Meta', dimension='Edad', segmento=age(k), valor=v, extra=0) for k, v in H.META_EDAD]
aud += [dict(canal='Meta', dimension='Región', segmento=reg(k), valor=v, extra=0) for k, v in H.META_REG]
for dim, rows, fn in (('Género', H.YT_GEN, G.get), ('Edad', H.YT_EDAD, age), ('Región', H.YT_REG, reg)): aud += [dict(canal='YouTube', dimension=dim, segmento=fn(k), valor=im, extra=vw) for k, vw, im in rows]
for dim, rows, fn in (('Género', H.GDN_GEN, G.get), ('Edad', H.GDN_EDAD, age), ('Región', H.GDN_REG, reg)): aud += [dict(canal='Display', dimension=dim, segmento=fn(k), valor=im, extra=ck) for k, im, ck in rows]
ult = max(r['fecha'] for r in diario)
out = dict(actualizado=ult, diario=diario, olas=olas, tiktok=tiktok, creativos=creativos, videos=videos, display=display, audiencia=aud, tiktok_aud=dict(edad=H.TT_EDAD, region=H.TT_REG))
open(os.path.join(D0, '..', 'datos.js'), 'w', encoding='utf-8').write('window.FP_DATA = ' + json.dumps(out, ensure_ascii=False) + ';\n')
print('diario', len(diario), 'creativos', len(creativos), 'videos', len(videos), 'display', len(display), 'sin imagen', [d['nombre'] for d in display if not d['img']])
