# CHANGELOG

## v0.0.1-alpha
- Se añadió yanog:<texto>
- Se añadieron colores
- Sistema de variables
- azomazo para múltiples funciones

---

## v0.0.2-alpha
- Mejor sistema de errores
- Nuevos comandos básicos
- Soporte para archivos .mazoxpkg
- Base inicial de sistema tipo OS (store interno)

---

## v0.0.3-beta
- Sistema IF inicial agregado
- Sistema ELSE inicial agregado
- Variables globales mejoradas
- Mejor parser de sintaxis <>
- Soporte de ejecución múltiple en azomazo

---

## v0.0.4-beta
- Sistema STORE de apps (mazoel:<app=código>)
- Ejecución de apps (gastes:<app>)
- Listado de apps (dineroel)
- Mini sistema tipo MAZO STORE interno

---

## v0.0.5-beta
- Sistema de colores extendido (&r &v &a &z &m &c &b &n &0)
- Soporte de variables dentro de texto ($variable)
- Mejor manejo de errores de sintaxis
- Optimización del intérprete

---

## v0.0.6-release-candidate
- Banner inicial MAZOX OS agregado
- Base preparada para MAZO STORE online
- Estructura lista para apps .mazoxpkg
- Preparación para firma digital futura (no implementada aún)
- Lenguaje estabilizado para publicación inicial

---

## v0.0.7-release
- Mejora del sistema STORE (estructura tipo objeto con versión de app)
- Debug mode agregado (debug)
- Comando info del sistema (info)
- Mejor manejo de ejecución de apps almacenadas
- Optimización de azomazo con limpieza de espacios
- Preparación para MAZO STORE PRO (instalación desde internet)

---

## v0.0.8-hotfix
- Corrección completa del sistema IF y ELSE
- ELSE ahora depende correctamente del último IF ejecutado
- Variable global "ultimo_if" agregada
- Nueva sintaxis estable para IF:
  si:<condicion|accion>
- Corrección de conflictos con símbolos <>
- Mejor estabilidad del parser de condiciones

---

## v0.0.9-dev
- Soporte REAL para ejecución de archivos .mazoxpkg
- Sistema de lectura de scripts externos línea por línea
- Soporte para:
  python interprete.py archivo.mazoxpkg
- Validación automática de extensión .mazoxpkg
- Mejor compatibilidad con Termux
- Inicio del sistema modular MAZOX
- Preparación para comando pedir:<var=pregunta>
- Base inicial para futuros imports y paquetes
- Mejor estructura interna del intérprete
- Preparación para ejecución de proyectos completos

---

## Próximamente
- comando pedir:<var=pregunta>
- sistema de funciones reales
- bucles
- imports
- compilador
- IDE de MAZOX
- soporte para mods
- paquetes externos
- MAZO STORE ONLINE
