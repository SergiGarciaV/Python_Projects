from LoggerBase import log

class User:

    def __init__(self, userId=None, nom=None, apellido=None, email=None):#Ponemos el userId en None para que no nos pida poner ningún dato ahí. No queremos pues será un autoincrementable de la BBDD. Al poner el userId en None, nos obliga a poner todos los demás en None sinó no se puede
        self._userId=userId
        self._name=nom
        self._lastName=apellido
        self._email=email


    def __str__(self):
        return f'ID={self.user_id} nombre={self.name} apellido={self.last_name} email={self.email}'




    @property
    def user_id(self):
        return self._userId

    @user_id.setter
    def user_id(self, user_id):
        self._userId=user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name=name

    @property
    def last_name(self):
        return self._lastName

    @last_name.setter
    def last_name(self, lastName):
        self._lastName=lastName

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email=email

if __name__=='__main__':
    #Simulamos un insert (no se pone el ID porque es autoincrementable)
    user=User(nom='Sergi',apellido='Garcia',email='sergi@mail.com')#Especificamos a que variable corresponde cada valor, es obligado al haber puesto las variables con =None en el __init__
    log.debug(user)#De esta forma estámos imprimiendo el detalle de Persona1 usando el log (hemos importado) que hemos configurado aparte
    #Simulamos un delete
    user1=User(userId='2')
    log.debug(user1)