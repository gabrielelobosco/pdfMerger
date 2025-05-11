from pypdf import PdfReader, PdfWriter
import os
import argparse
import sys

def get_sorted_pdfs_from(directory, separator):
    items = os.listdir(directory)
    try:
        sorted_pdfs = sorted(items, key=lambda x: int(x.split(separator)[0]))
    except (ValueError):
        print("Invalid file naming format!\nTo work correctly, the script requires files to be named as:\n\t[number][separator][file_name]")
        sys.exit(1)
    return sorted_pdfs

def merge_pdf(separator, input_dir, output_dir, file_name, preview=False):
    if not file_name.endswith(".pdf"):
        file_name += ".pdf"
    pdfs = get_sorted_pdfs_from(input_dir, separator)
    
    if preview:
        print("Preview mode enabled: the following files would be merged, but no file will be created.\n")
        for pdf in pdfs:
            print("\t- ", pdf)
        print("\nOutput file name:", file_name)
        print("\tOutput directory:", output_dir)
        return
    
    writer = PdfWriter()
    for i in range(len(pdfs)):
        try:
            reader = PdfReader(os.path.join(input_dir, pdfs[i]))
            writer.append(reader)
        except Exception as e:
            print("[!] Cannot read (corrupted or incorrect file):", pdfs[i])
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, "wb") as f:
        writer.write(f)
    print("Merged pdf saved to:", output_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge a set of PDF files from a folder into a single PDF, ordered either by their name or by a numeric value separated from the file name by a custom delimiter.")
    parser.add_argument("--separator", default=" ", help="Filename separator, e.g., in '1-FirstPdf.pdf', the separator is '-' (default: space ' ').")
    parser.add_argument("input_dir", help="Directory containing the PDF files to merge. NOTE: files must be numerically ordered in the format [number][separator][file_name]!")
    parser.add_argument("--output-dir", default=os.getcwd(), help="Directory where the merged PDF will be saved (default: " + os.getcwd() + ")")
    parser.add_argument("--file-name", default="MergedPdf.pdf", help="Name of the resulting merged PDF file (default: MergedPdf.pdf)")
    parser.add_argument("--preview", action="store_true", help="Display the list of PDF files to be merged and their order without creating the output file.")

    args = parser.parse_args()
    merge_pdf(args.separator, args.input_dir, args.output_dir, args.file_name, args.preview)