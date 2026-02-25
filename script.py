from pyscript import HTML, display
from js import document
import asyncio

async def iniciar_homenagem(event):
    btn = document.getElementById("btn-iniciar")
    output = document.getElementById("output")
    btn.style.display = "none"
    output.innerHTML = "<p style='color: #28a745;'>[INFO] Carregando banco de dados emocional...</p>"
    await asyncio.sleep(1)
    
    display(HTML("<h2 style='color: #e83e8c;'>MÃE,</h2>"), target="output", append=True)
    await asyncio.sleep(1)
    display("Este script foi compilado com 100% de amor e gratidão.", target="output", append=True)
    await asyncio.sleep(1)
    display(HTML("<b style='color: #00ffff;'>Você é a melhor versão que a vida já criou!</b>"), target="output", append=True)
    await asyncio.sleep(1)
    
    bolo = """<pre>
         (  )   (  )   (  )
          ||     ||     ||
      ____||_____||_____||____
     |    ✨ PARABÉNS ✨     |
     |_______________________|
    </pre>"""
    display(HTML(bolo), target="output", append=True)
    await asyncio.sleep(0.5)
    display(HTML("<h1 style='color: #ff0000; font-size: 2.5rem;'>FELIZ ANIVERSÁRIO!</h1>"), target="output", append=True)
