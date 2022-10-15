from config.moduls import Post
from Repositories.PostRepository import PostRepository
class PostController:
    def __init__(self, PostRepo = PostRepository(Post)):
        self.PostRepo = PostRepo

    def index(self, take, skip):
        return self.PostRepo.getList(take, skip)

    def show(self, id):
        return self.PostRepo.show(id)

    def create(self, request, response, user_id):
        newData = Post(title=request.title,body=request.body, image=request.image, creator_id=user_id)
        return self.PostRepo.store(newData, response)

    def updated(self, id, request, response):
        return self.PostRepo.updated(id, request, response)

    def delete(self, id):
        return self.PostRepo.delete(id)

