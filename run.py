from app import create_app

# Creating main app
app = create_app()

# Handling error for not found routes
@app.errorhandler(404)
def service_not_found(e):
    return 'service not found'


# Handling error for server error
@app.errorhandler(500)
def service_error(e):
    return 'server error'


if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
