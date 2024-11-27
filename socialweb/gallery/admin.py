from django.contrib import admin
from .models import Gallery, Album, V_Gallery, CommentVG, CommentIMG, \
    LikedIMG, LikedCommentIMG, LikedCommentVG, LikedReplyIMG, LikedReplyVG, \
    ReplyIMG, ReplyVG, LikedVG

admin.site.register(Gallery)
admin.site.register(V_Gallery)
admin.site.register(Album)
admin.site.register(CommentIMG)
admin.site.register(ReplyIMG)
admin.site.register(LikedIMG)
admin.site.register(LikedCommentIMG)
admin.site.register(LikedReplyIMG)
admin.site.register(CommentVG)
admin.site.register(ReplyVG)
admin.site.register(LikedVG)
admin.site.register(LikedCommentVG)
admin.site.register(LikedReplyVG)


