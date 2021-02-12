import os

#to get the file size
@app.route('/count')
def size():
    file_stats = os.stat(filename)
    if file_stats.st_size():

        resp = jsonify({'size of each chunk is :'}) 
        return resp
    