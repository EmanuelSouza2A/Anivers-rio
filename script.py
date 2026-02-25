from pyscript import HTML, display
from js import document
import asyncio
import random

async def type_writer(text, target, color="inherit", delay=0.03):
    p = document.createElement("p")
    p.style.color = color
    p.className = "log-entry"
    document.getElementById(target).appendChild(p)
    for char in text:
        p.innerHTML += char
        await asyncio.sleep(delay)

async def start_protocol(event):
    document.getElementById("btn-master").style.display = "none"
    document.getElementById("console-container").style.visibility = "visible"
    
    stream = "output-stream"
    
    # --- FASE 1: LOGS TECNICOS (DETALHE EXTREMO) ---
    await type_writer("> INITIALIZING BIOS 4.0...", stream)
    await type_writer("> CHECKING HARDWARE INTEGRITY...", stream)
    
    for _ in range(15):
        hex_code = "".join(random.choices("ABCDEF0123456789", k=16))
        await type_writer(f"SEARCHING SECTOR {hex_code}... FOUND!", stream, delay=0.01)
    
    await type_writer("> BYPASSING EMOTIONAL FIREWALL...", stream, color="#00ffff")
    await asyncio.sleep(0.5)
    
    # --- FASE 2: A MENSAGEM ---
    await type_writer("\n[!] ACESSO CONCEDIDO: MODO ANIVERSÁRIO ATIVADO", stream, color="#00ff00")
    await asyncio.sleep(1)
    
    await type_writer("\nPARABÉNS, MÃE!", stream, color="#ff0055")
    await type_writer("Sabe, eu poderia ter escrito um bilhete comum...", stream)
    await type_writer("Mas para a mulher que me deu a vida, eu precisava de um sistema inteiro.", stream)
    await type_writer("Você é a minha maior inspiração e o melhor exemplo de força.", stream, color="#00ffff")
    
    # --- FASE 3: ARTE ASCII ---
    bolo = """
    <pre>
             .--------.
            |  ✨✨✨  |
        .---'----------'---.
       |   ❤️ PARABÉNS ❤️    |
       |     MÃE ELITE     |
       '-------------------'
    </pre>
    """
    display(HTML(bolo), target=stream, append=True)
    
    await type_writer("\n> OBRIGADO POR TUDO. EU TE AMO!", stream, color="#ff0055")
    await type_writer("> FIM DA TRANSMISSÃO.", stream)
