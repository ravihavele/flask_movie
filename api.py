from movies import *

# route to get all Movies
@app.route("/movies", methods=["GET"])
def get_movies():
    '''Function to get all the movies in the database'''
    return jsonify({'Movies': Movie.get_all_movies()})

# route to get movie by id
@app.route("/movies/<int:id>",methods=["GET"])
def get_movie_by_id(id):
    return_value = Movie.get_movie(id)
    return jsonify(return_value)

#route to add movie
@app.route("/movies", methods=["POST"])
def add_movies():
    '''Function to add new movie to our database'''
    request_data = request.get_json() #getting data from client
    Movie.add_movie(request_data["title"], request_data["year"], request_data["genre"])
    responce = Response("Movie Added", status= 201, mimetype="application/json")
    return responce

#route to update movie with PUT Method
@app.route("/movies/<int:id>", methods=["PUT"])
def update_movie(id):
    '''Function to edit movie in our database using movie id'''
    request_data = request.get_json() # getting data from client
    Movie.update_movie(id, request_data["title"], request_data["year"], request_data["genre"])
    responce = Response("Movie Updated", status=200, mimetype="application/json")
    return responce

# route to delete movie using the DELETE method
@app.route("/movies/<int:id>",methods=["DELETE"])
def delete_movie(id):
    '''Function to delete movie from our database'''
    Movie.delete_movie(id)
    responce = Response("Movie Deleted", status=200, mimetype="application/json")
    return responce

if __name__=="__main__":
    app.run(port=5000, debug=True)



