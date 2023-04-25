# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users_schema').query_db(query)
        # Create an empty list to append our instances of users
        users = []
        # Iterate over the db results and create instances of users with cls.
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_single_user(cls,id):
        query  = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL('users_schema').query_db(query, {'id':id})
        return cls(result[0])
    
    @classmethod
    def update(cls,data, id):
        query = f"UPDATE users SET first_name= %(fname)s,last_name=%(lname)s,email=%(email)s WHERE id = {id};"
        return connectToMySQL('users_schema').query_db(query,data)
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email) VALUES ( %(fname)s , %(lname)s , %(email)s);"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def get_max_id(cls):
        query = "SELECT MAX(id) FROM users;"
        return connectToMySQL('users_schema').query_db( query )


    @classmethod
    def delet(cls,id):
        query = f"DELETE FROM users WHERE id = {id};"  
        return connectToMySQL('users_schema').query_db( query)