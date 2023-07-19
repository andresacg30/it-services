from app.services.document_service.jobs import PDFToWordJob


def test__process__creates_file(
    mocker,
    mocker_pdf_file,
    mocker_docx_file
):
    mocker.patch("app.services.document_service.jobs.pdf_to_word.parse")
    mocker.patch("app.services.document_service.jobs.pdf_to_word.TemporaryDirectory")
    mocker.patch("app.services.document_service.jobs.pdf_to_word.Path")

    job = PDFToWordJob()
    job.process(file=mocker_pdf_file)

    assert job.file == mocker_docx_file.filename
    assert job.name == "pdf-to-word"
