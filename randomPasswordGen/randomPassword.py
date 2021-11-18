import secrets
import string



def random_password(length_of_password):
  
  password =''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for i in range(length_of_password))
  return password
print(random_password(12))
print(random_password(6))
print(random_password(8))
