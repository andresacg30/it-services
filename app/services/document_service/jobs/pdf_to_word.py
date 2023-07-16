from fastapi import UploadFile
from pathlib import Path
from pdf2docx import parse
from tempfile import TemporaryDirectory


from app.services.base_config import BaseJob


class PDFToWordJob(BaseJob):
    name = "pdf-to-word"
    file: str

    def process(self, file: UploadFile):
        print("Processing PDF to Word job")
        with TemporaryDirectory() as temp_dir:
            temp_file = Path(temp_dir) / file.filename
            docx_name = file.filename.replace(".pdf", ".docx")
            docx_file = "./app/" + docx_name
            with open(temp_file, "wb") as f:
                f.write(file.file.read())
            parse(pdf_file=temp_file, docx_file=docx_file)
            self.file = docx_file

    def finish(self):
        print("Finishing PDF to Word job")
        return self.file
