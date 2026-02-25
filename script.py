from pyscript import HTML, display
from js import document
import asyncio

async def executar_elite(event):
    btn = document.getElementById("btn-iniciar")
    term = document.getElementById("terminal")
    output = document.getElementById("output")
    
    # Esconde botão e mostra o terminal neon
    btn.style.display = "none"
    term.style.visibility = "visible"
    
    # Sequência de Carregamento Hacker
    linhas = [
        "> BYPASSING SECURITY FILTERS...",
        "> ACCESSING CORE_MEMORIES.DAT...",
        "> DECRYPTING MOTHER_LOVE_PROTOCOL...",
        "> [SUCCESS] CONNECTION ESTABLISHED."
    ]
    
    for linha in linhas:
        display(HTML(f"<p style='color:#0f0'>{linha}</p>"), target="output", append=True)
        await asyncio.sleep(0.6)

    await asyncio.sleep(1)
    
    # Mensagem de Impacto
    display(HTML("<h1 class='glitch'>ALERTA: AMOR DETECTADO!</h1>"), target="output", append=True)
    await asyncio.sleep(1)
    
    display(HTML("<h2 class='text-pink'>PARABÉNS, MÃE!</h2>"), target="output", append=True)
    display(HTML("<p class='text-cyan'>Você é o núcleo do meu processamento e a luz do meu código.</p>"), target="output", append=True)

    # Bolo Hacker
    bolo = """
    <pre>
             (  )   (  )   (  )
              ||     ||     ||
          ____||_____||_____||____
         |    [  PARABÉNS  ]     |
         |_______________________|
    </pre>
    """
    display(HTML(bolo), target="output", append=True)
    await asyncio.sleep(0.5)
    display(HTML("<h1 style='color: #f00; font-size: 3rem;'>EU TE AMO!</h1>"), target="output", append=True)
