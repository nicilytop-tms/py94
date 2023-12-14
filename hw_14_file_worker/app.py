from hw_14_file_worker.file_worker import FileWorker


def app():
    fw = FileWorker('data.json')
    content = fw.read()
    print(content)

    fw.append('obj1')
    fw.append('obj2')
    fw.close()


app()
