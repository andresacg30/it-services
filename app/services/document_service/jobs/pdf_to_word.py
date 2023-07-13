from app.services.base_config import BaseJob


class PDFToWordJob(BaseJob):
    file = None

    def process(self, file):
        print("Processing PDF to Word job")
        self.file = file

    def finish(self):
        print("Finishing PDF to Word job")
        return self.file
