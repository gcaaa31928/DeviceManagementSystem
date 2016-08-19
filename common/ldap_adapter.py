import ldap

from DeviceManagementSystem import settings


class LDAPAdapter:

    def __init__(self, username, password):
        self.ldap_server = settings.LDAP_SERVER
        self.username=username
        self.password=password


    def try_login(self):
        user_dn = "uid=" + self.username + "," + settings.USER_DN
        search_filter = "uid=" + self.username
        base_dn = settings.BASE_DN
        connect = ldap.initialize(self.ldap_server)
        try:
            connect.bind_s(user_dn, self.password)
            self.result = connect.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
            connect.unbind_s()
            return True
        except ldap.LDAPError:
            connect.unbind_s()
            return False

    def get_result(self):
        name = self.result[0][1]['cn'][0].decode('utf-8')
        mail = self.result[0][1]['mail'][0].decode('utf-8')
        id = self.result[0][1]['uid'][0].decode('utf-8')
        return id, name, mail