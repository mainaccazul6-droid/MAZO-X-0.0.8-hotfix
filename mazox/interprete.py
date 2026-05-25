import time
import random

variables = {}
store = {}

# ==================================================
# COLORES MAZOX
# ==================================================
COLORES = {
    "&r": "\033[31m",
    "&v": "\033[32m",
    "&a": "\033[33m",
    "&z": "\033[34m",
    "&m": "\033[35m",
    "&c": "\033[36m",
    "&b": "\033[37m",
    "&n": "\033[1m",
    "&0": "\033[0m",
}

def color(txt):
    for k, v in COLORES.items():
        txt = txt.replace(k, v)
    return txt

# ==================================================
# EXTRAER <>
# ==================================================
def extraer(linea, cmd):
    try:
        data = linea.split(cmd, 1)[1].strip()
        if data.startswith("<") and data.endswith(">"):
            return data[1:-1]
    except:
        pass
    print("Error de sintaxis:", cmd)
    return None

# ==================================================
# CONDICIONES
# ==================================================
def cond(c):
    try:
        c = c.replace(" ", "")
        if "==" in c:
            a, b = c.split("==")
            return a == b
        if "!=" in c:
            a, b = c.split("!=")
            return a != b
        if ">" in c:
            a, b = c.split(">")
            return float(a) > float(b)
        if "<" in c:
            a, b = c.split("<")
            return float(a) < float(b)
    except:
        return False

# ==================================================
# EJECUTOR
# ==================================================
def ejecutar(linea):

    linea = linea.strip()
    if not linea:
        return

    # =========================
    # PRINT
    # =========================
    if linea.startswith("yanog:"):
        t = extraer(linea, "yanog:")
        if t:
            for k, v in variables.items():
                t = t.replace(f"${k}", str(v))
            print(color(t) + "\033[0m")

    # =========================
    # VARIABLES
    # =========================
    elif linea.startswith("mazo:"):
        t = extraer(linea, "mazo:")
        if t:
            try:
                n, v = t.split("=")
                variables[n.strip()] = v.strip()
                print("✔ variable guardada")
            except:
                print("error mazo")

    # =========================
    # SUMA
    # =========================
    elif linea.startswith("dinero:"):
        t = extraer(linea, "dinero:")
        try:
            a, b = t.split("+")
            print(float(a) + float(b))
        except:
            print("error dinero")

    # =========================
    # RANDOM
    # =========================
    elif linea.startswith("nogastes:"):
        t = extraer(linea, "nogastes:")
        try:
            a, b = t.split("-")
            print(random.randint(int(a), int(b)))
        except:
            print("error nogastes")

    # =========================
    # WAIT
    # =========================
    elif linea.startswith("yadinero:"):
        t = extraer(linea, "yadinero:")
        try:
            time.sleep(float(t))
        except:
            print("error wait")

    # =========================
    # MULTI (MEJORADO)
    # =========================
    elif linea.startswith("azomazo:"):
        t = extraer(linea, "azomazo:")
        if t:
            for x in t.split("|"):
                ejecutar(x.strip())

    # =========================
    # IF
    # =========================
    elif linea.startswith("si:"):
        t = extraer(linea, "si:")
        try:
            c, act = t.split("->")
            if cond(c):
                ejecutar(act)
        except:
            print("error si")

    # =========================
    # ELSE
    # =========================
    elif linea.startswith("sino:"):
        t = extraer(linea, "sino:")
        if t:
            ejecutar(t)

    # =========================
    # STORE AVANZADO
    # ==================================================
    elif linea.startswith("mazoel:"):
        t = extraer(linea, "mazoel:")
        try:
            name, code = t.split("=", 1)

            store[name] = {
                "code": code,
                "version": "1.0"
            }

            print("📦 app guardada:", name)

        except:
            print("error store")

    # =========================
    # RUN APP
    # =========================
    elif linea.startswith("gastes:"):
        t = extraer(linea, "gastes:")
        if t in store:
            ejecutar(store[t]["code"])
        else:
            print("app no existe")

    # =========================
    # LIST APPS
    # =========================
    elif linea == "dineroel":
        print("📦 APPS INSTALADAS:")
        for k in store:
            print("-", k)

    # =========================
    # INFO SYSTEM
    # =========================
    elif linea == "info":
        print("MAZOX SYSTEM")
        print("Apps:", len(store))
        print("Variables:", len(variables))

    # =========================
    # DEBUG MODE
    # =========================
    elif linea == "debug":
        print("STORE RAW:")
        print(store)
        print("VARIABLES:")
        print(variables)

    # =========================
    # AYUDA
    # =========================
    elif linea == "ayuda":
        print("""
================= MAZOX HELP =================

mazo:<nombre=valor>
yanog:<texto>
dinero:<5+10>
nogastes:<1-100>
yadinero:<2>
azomazo:<cmd1|cmd2>

si:<5>3->yanog:<Mayor>
sino:<yanog:<No>>

mazoel:<app=code>
gastes:<app>
dineroel

info
debug

🎨 COLORES:
&r &v &a &z &m &c &b &n &0

============================================
YA NO GASTES DINERO EN EL MAZO
============================================
""")

    # =========================
    # ERROR
    # =========================
    else:
        print("El mazo no reconoce el comando.")
        print("Escribe 'ayuda'")

# ==================================================
# MAIN
# ==================================================
def main():

    print("\033[1;36m===================================================\033[0m")
    print("               █▀▄▀█ █▀█ ▀█ █▀█ ▄▄ ▀▄▀")
    print("               █ ▀ █ █▀█ █▄ █▄█    █ █")
    print("")
    print("      MAZOX LANGUAGE / OS EXPERIMENT")
    print("      YA NO GASTES DINERO EN EL MAZO")
    print("")
    print("     Escribe 'salir'")
    print("     Escribe 'ayuda'")
    print("\033[1;36m===================================================\033[0m")

    while True:
        try:
            cmd = input("\033[1;35m>> \033[0m")
            if cmd == "salir":
                break
            ejecutar(cmd)
        except:
            break

if __name__ == "__main__":
    main()