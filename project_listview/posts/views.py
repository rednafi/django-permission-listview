# posts/views.py
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import HasGroupPermission


class PostListByGroup(ListAPIView):
    permission_classes = (IsAuthenticated, HasGroupPermission)
    # required_groups = None
    # queryset = None
    serializer_class = PostSerializer

    # Set the filter based on condition
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Post.objects.all()
        elif user.groups.filter(name="group_1").exists():
            PostListByGroup.required_groups = {"GET": ["group_1",]}
            return Post.objects.filter(id__lte=3)
        elif user.groups.filter(name="group_2").exists():
            PostListByGroup.required_groups = {"GET": ["group_2",]}
            return Post.objects.filter(id__gt=3)
