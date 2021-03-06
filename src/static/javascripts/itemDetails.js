'use strict'

var pushRequestForNewComments = function(uid, content) {
    // 请后端同学在这里对接...
    // uid是后端提供的用户id
    // content是新评论的内容
}

var detailsVM = new Vue({
    el: "#details",
    data: {
        "comments": commentsData,
        "newCommentContent": "",
    },
    methods: {
        "pushNewComment": function(event) {
            var newComment = {
                "user": {
                    "avatar": myAvatar,
                    "nickname": myNickname,
                },
                "content": this.newCommentContent,
                "subcomments": [],
                "time": "刚刚",
            };
            this.comments.push(newComment);
            pushRequestForNewComments(myUid, this.newCommentContent);
            this.newCommentContent = "";
        },
    },
});