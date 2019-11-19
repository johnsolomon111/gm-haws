from api import server

# if __name__ == '__main__':
# 	server.run(debug=True,port=5050)

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    server.run(host='0.0.0.0', port=port)