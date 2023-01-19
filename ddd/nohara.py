# entity
class User():
    ...

# repository IF
class Repository(mataclass=ABCMeta):
    @abstractmethod
    def find(self, UserName: str) -> Optional[User]:
        pass @abstractmethod

    def save(self, User: UserClass) -> None:
        pass


# user repository
class UserRepository(Repository):
    def _init_():
        # 認証系

    def find(self, UserName: str) -> Optional[User]:
        ...
    def save(self, User: UserClass) -> None:
        ...

# domain service
class UserService():
    def _init_(UserRepository: user_repository):
        self.user_repository = user_repository

    def exist(self, user: User) -> bool:
        return self.user_repository.find(user.name) != None

# 前回の野原さんが作成してくださった。programがApplicationServiceにあたる。
class Program1():
    def _init_():
        self.user_repository = UserRepository()

    def create_user(self, user_name: str) -> None:
        user = User(user_name)
        user_domain_service = UserService(self.user_repository)
        if user_domain_service.exist(user):
            raise ValueError(f"{user_name}はすでに存在しています")
        else: self.user_repository.save(user)
