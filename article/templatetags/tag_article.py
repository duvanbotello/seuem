from django import template

from article.models import Post

register = template.Library()


@register.simple_tag()
def get_post():
    post = Post.objects.filter(id=1).first()
    return post.content
