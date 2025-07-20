comandos = {
    "hi": "¡Hola! ¿Cómo estás?",
    "info": "Soy un bot impulsado por GPT. Usa `!senku <mensaje>` para preguntarme algo.",
    "help": "Puedes usar `!senku <mensaje>` para interactuar conmigo, o `!commands` para ver esta lista.",
    "commands": "Muestra la lista de comandos disponibles.",
}

def get_comandos():
    """Devuelve todos los comandos disponibles en formato de lista de texto."""
    return "\n".join([f"• `!{cmd}` – {desc}" for cmd, desc in comandos.items()])

def ejecutar_comando(nombre):
    """Ejecuta un comando si existe."""
    nombre = nombre.lower()
    if nombre in comandos:
        return comandos[nombre]
    return None
