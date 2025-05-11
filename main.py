from pypdf import PdfReader, PdfWriter
import os
import argparse
import sys

def get_sorted_pdfs_from(directory, separator):
    items = os.listdir(directory)
    try:
        sorted_pdfs = sorted(items, key=lambda x: int(x.split(separator)[0]))
    except (ValueError):
        print("Errore nell'organizzazione dei file da unire!\n\tRicorda che il programma, per funzionare, richiede che i file siano organizzati nel seguente modo:\n\t\t[numero_crescente] [separatore] [nome_file]")
        sys.exit(1)
    return sorted_pdfs

def merge_pdf(separator, input_dir, output_dir, file_name, preview=False):
    if not file_name.endswith(".pdf"):
        file_name += ".pdf"
    pdfs = get_sorted_pdfs_from(input_dir, separator)
    
    if preview:
        print("Ecco i PDF che verrebbero uniti:\n")
        for pdf in pdfs:
            print("\t- ", pdf)
        print("\nVerrebbero salvati con il nome", file_name)
        print("\tNella directory", output_dir)
        return
    
    writer = PdfWriter()
    for i in range(len(pdfs)):
        try:
            reader = PdfReader(os.path.join(input_dir, pdfs[i]))
            writer.append(reader)
        except Exception as e:
            print("[!] Impossibile leggere:", pdfs[i])
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, "wb") as f:
        writer.write(f)
    print("Pdf unito e salvato in " + output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unisci un set di PDF da una cartella, in un unico PDF ordinato secondo il loro nome, oppure secondo un valore numerico crescente, che divide tramite un separatore il valore in questione dal nome del file!")
    parser.add_argument("--separator", default=" ", help="Separatore nome file, es. 1-PrimoPdf.pdf, dove \"-\" è il separatore (default: \" \")")
    parser.add_argument("input_dir", help="Directory in cui si trovano tutti i pdf da unire, (NOTA BENE: i pdf devono essere ordinati numericamente, ovvero devono essere del tipo [numero_crescente] [separatore] [nome_file]!)")
    parser.add_argument("--output-dir", default=os.getcwd(), help="Directory in cui salvare il pdf risultante dal merger (default: " + os.getcwd() +")")
    parser.add_argument("--file-name", default="MergedPdf.pdf", help="Nome del file risultante dal merger (default: MergedPdf.pdf)")
    parser.add_argument("--preview", action="store_true", help="Visualizza i pdf che verranno uniti e il loro ordine");

    args = parser.parse_args()
    merge_pdf(args.separator, args.input_dir, args.output_dir, args.file_name, args.preview)