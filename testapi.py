from flask import Flask, jsonify, request
import mysql.connector as mysql


app = Flask(__name__)

db= mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "1234",
    database = "imbd"
)

mycursor = db.cursor()
 

@app.route("/get", methods=['GET'])
def httpGET():
    mycursor.execute(f"SELECT * FROM MOVIE")
    movies = []
    
    for row in mycursor.fetchall():
        movie={
            'movie_id': row[0],
            'movie_title': row[1],
            'movie_time': row[2],
            'movie_rel': row[3],
            'movie_lang': row[4],
            'movie_mpaa': row[5]
        }
        
        movies.append(movie)
        
    return jsonify({'movies': movies})


@app.route("/post", methods=['POST'])
def httpPOST():
    data = request.get_json()
    movie_id = data['movie_id']
    movie_title = data['movie_title']
    movie_time  = data['movie_time']
    movie_rel = data['movie_rel']
    movie_lang = data['movie_lang']
    movie_mpaa = data['movie_mpaa']
    
    sql = "INSERT INTO MOVIE (movie_id,movie_title,movie_time,movie_rel,movie_lang,movie_mpaa) VALUES (%s,%s,%s,%s,%s,%s)"
    val = (movie_id,movie_title,movie_time,movie_rel,movie_lang,movie_mpaa)
    mycursor.execute(sql,val)
    db.commit()
    return jsonify({'message': 'Movie added successfully'})

@app.route("/put/<int:id>", methods=['PUT'])
def httpUPDATE(id):
    data = request.get_json()
    movie_title = data['movie_title']
    movie_time = data['movie_time']
    movie_rel = data['movie_rel']
    movie_lang = data['movie_lang']
    movie_mpaa = data['movie_mpaa']
    
    sql = "UPDATE MOVIE SET movie_title = %s, movie_time = %s, movie_rel = %s, movie_lang = %s, movie_mpaa = %s WHERE movie_id = %s"
    val = (movie_title, movie_time, movie_rel, movie_lang, movie_mpaa, id)
    
    mycursor.execute(sql, val)
    db.commit()
    
    return jsonify({'message': 'Movie updated successfully'})

@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_movie(id):
    sql = "DELETE FROM MOVIE WHERE movie_id = %s"
    mycursor.execute(sql, id)
    db.commit()
    return jsonify({'message': 'Movie deleted successfully'}), 200






if __name__ == "__main__":
    app.run(debug=True)
