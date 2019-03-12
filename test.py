from goodreads import client
key = 'VXaVHi1hT5aknGPr6JHSQ'
secret = 'W3JuVx1hhxEzDaOdsRjoPlIj9T1Ny0uhbEunxNtq56Y'
gc = client.GoodreadsClient(key, secret)
gc.authenticate()
