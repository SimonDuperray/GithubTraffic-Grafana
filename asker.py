to_fill = {
   'auth_token': None,
   'author': None,
   'host': None,
   'port': None,
   'user': None,
   'pwd': None,
   'dbname': None,
   'measurement': None
}

to_fill['auth_token'] = input('Auth Token: \n')
to_fill['author'] = input('Author: \n')
to_fill['host'] = input('Host: \n')
to_fill['port'] = input('Port: \n')
to_fill['user'] = input('User: \n')
to_fill['pwd'] = input('Password: \n')
to_fill['dbname'] = input('DBName: \n')
to_fill['measurement'] = input('Measurement: \n')

text_file = open("./.env", "w")

content = ""
for key, val in to_fill.items():
   content+=key.upper()+"="+str(val)+"\n"

text_file.write(content)

text_file.close()