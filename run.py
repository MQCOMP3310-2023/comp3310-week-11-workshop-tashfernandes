from project import create_app

# Adding some whitespace
# adding some more stuff in dev
if __name__ == '__main__':
  app = create_app()
  app.run(host = '0.0.0.0', port = 8001, debug=True) 

