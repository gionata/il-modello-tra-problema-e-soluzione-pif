import qrcode
import qrcode.image.svg

# --- Configurazione e Generazione dell'Immagine QR Code ---

# Definisci il metodo di generazione SVG.
# Lasciandolo vuoto, verrà usato 'SvgPathImage', che è consigliato 
# perché utilizza un singolo percorso SVG per i moduli, migliorando
# la resa quando si effettua lo zoom.
method = '' 

if method == 'basic':
    # Simple factory (solo un insieme di rettangoli).
    factory = qrcode.image.svg.SvgImage
elif method == 'fragment':
    # Fragment factory (simile a basic, ma usa frammenti SVG).
    factory = qrcode.image.svg.SvgFragmentImage
else:
    # Combined path factory (Usa un singolo percorso SVG, risolve gli spazi bianchi).
    factory = qrcode.image.svg.SvgPathImage

# URL da codificare nel QR code
url_to_encode = 'https://gionata.github.io/il-modello-tra-problema-e-soluzione-pif/'

# Genera l'oggetto QR Code SVG.
# L'oggetto 'img' è un'istanza della factory selezionata (es. SvgPathImage)
img = qrcode.make(url_to_encode, image_factory=factory)

# --- Salvataggio del file SVG ---

# L'oggetto immagine SVG generato ha un metodo .save() che salva
# il contenuto nella variabile 'img' nel file specificato.
try:
    img.save('../assets/qr.svg')
    print(f"QR Code SVG salvato con successo in 'qr.svg' per l'URL: {url_to_encode}")
except Exception as e:
    print(f"Errore durante il salvataggio del file: {e}")
