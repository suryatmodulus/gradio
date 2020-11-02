# Demo: (File, File) -> (File)

import gradio as gr
from zipfile import ZipFile


def zip_two_files(file1, file2):
    with ZipFile('tmp.zip', 'w') as zipObj:
        zipObj.write(file1.name, "file1")
        zipObj.write(file2.name, "file2")
    return "tmp.zip"


io = gr.Interface(
    zip_two_files, 
    ["file", "file"], 
    "file",
    examples=[
        ["images/1.jpg", "images/2.jpg"],
        ["files/titanic.csv", "audio/cantina.wav"],
    ]
)

io.test_launch()
io.launch()
