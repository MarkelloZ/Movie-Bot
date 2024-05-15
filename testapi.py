from flask import Flask, jsonify, request
import mysql.connector as mysql

app = Flask(__name__)

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="imbd"
)

mycursor = db.cursor()


@app.route("/get", methods=['GET'])
def httpGET():
    sql = "SELECT * FROM MOVIE WHERE 1=1"
    random = 0

    filters = {}
    for key, value in request.args.items():
        if key == "random" or key == "Random":
            random = 1
        else:
            filters[key] = value

    conditions = []
    values = []
    for key, value in filters.items():
        conditions.append(f"{key} = %s")
        values.append(value)

    if conditions:
        sql += " AND " + " AND ".join(conditions)

    if random == 1 and request.args.get("random") == "1":
        sql += " ORDER BY RAND() LIMIT 1"
    mycursor.execute(sql, tuple(values))

    movies = []
    for row in mycursor.fetchall():
        movie = {
            'movie_id': row[0],
            'movie_title': row[1],
            'movie_time': row[2],
            'movie_rel': row[3],
            'movie_lang': row[4],
            'movie_mpaa': row[5]
        }

        movies.append(movie)

    return jsonify({'movies': movies}), 200


@app.route("/post", methods=['POST'])
def httpPOST():
    data = request.get_json()

    movie_title = data.get('movie_title')
    movie_time = data.get('movie_time')
    movie_rel = data.get('movie_rel')
    movie_lang = data.get('movie_lang')
    movie_mpaa = data.get('movie_mpaa')

    if not movie_title:
        return jsonify({'message': 'No Movie Title'}), 400
    if not movie_time:
        return jsonify({'message': 'No Movie Duration'}), 400
    if not movie_rel:
        return jsonify({'message': 'No Movie Release Date'}), 400
    if not movie_lang:
        return jsonify({'message': 'No Movie Language'}), 400
    if not movie_mpaa:
        return jsonify({'message': 'No Movie mpaa'}), 400

    sql = "INSERT INTO Movie (movie_title,movie_time,movie_rel,movie_lang,movie_mpaa) VALUES (%s,%s,%s,%s,%s)"

    val = (movie_title, movie_time, movie_rel, movie_lang, movie_mpaa)
    mycursor.execute(sql, val)
    db.commit()
    return jsonify({'message': 'Movie added successfully'}), 201


@app.route("/put/<int:id>", methods=['PUT'])
def httpUPDATE(id):
    data = request.get_json()
    movie_title = data.get('movie_title')
    movie_time = data.get('movie_time')
    movie_rel = data.get('movie_rel')
    movie_lang = data.get('movie_lang')
    movie_mpaa = data.get('movie_mpaa')

    sql = "UPDATE MOVIE SET movie_title = %s, movie_time = %s, movie_rel = %s, movie_lang = %s, movie_mpaa = %s WHERE movie_id = %s"
    val = (movie_title, movie_time, movie_rel, movie_lang, movie_mpaa, id)

    mycursor.execute(sql, val)
    db.commit()

    if mycursor.rowcount == 0:
        return jsonify({'message': 'Movie not found'}), 404
    else:
        return jsonify({'message': 'Movie updated successfully'}), 200


@app.route("/delete/<int:id>", methods=['DELETE'])
def delete_movie(id):
    sql = "DELETE FROM MOVIE WHERE movie_id = %s"
    mycursor.execute(sql, (id,))
    db.commit()

    if mycursor.rowcount == 0:
        return jsonify({'message': 'Movie not found'}), 404
    else:
        return jsonify({'message': 'Movie deleted successfully'}), 200


if __name__ == "__main__":
    app.run(debug=True)
